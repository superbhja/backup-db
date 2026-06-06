#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
auditoria.py

Uso:

python scripts/auditoria.py \
    backups/backup_hidroplanta_2026-06-05_21-25.zip \
    auditorias/auditoria_hidroplanta_2026-06-05_21-25.md
"""

import re
import sys
import zipfile
from datetime import datetime


# ============================================================
# ANALIZADOR PRINCIPAL
# ============================================================

def analizar_datos_frescos(zip_path):

    reporte = {
        "tablas": [],
        "rpcs": [],
        "rls": [],
        "conteos": {},
        "indices": [],
        "enums": []
    }

    with zipfile.ZipFile(zip_path, "r") as z:

        sql_files = [
            f for f in z.namelist()
            if f.endswith(".sql")
        ]

        if not sql_files:
            raise RuntimeError(
                "No se encontró ningún archivo SQL dentro del ZIP."
            )

        with z.open(sql_files[0]) as f:
            content = f.read().decode(
                "utf-8",
                errors="ignore"
            )

    # ========================================================
    # TABLAS
    # ========================================================

    table_matches = re.finditer(
        r'CREATE TABLE (?:public\.)?"?(\w+)"?\s*\((.*?)\);',
        content,
        re.DOTALL
    )

    for match in table_matches:

        nombre = match.group(1)

        columnas_raw = match.group(2).strip().split("\n")

        columnas = []

        for c in columnas_raw:

            c = c.strip()

            if (
                not c
                or c.upper().startswith(
                    (
                        "CONSTRAINT",
                        "PRIMARY",
                        "FOREIGN",
                        "CHECK",
                        "--"
                    )
                )
            ):
                continue

            columna = (
                c.split(" ")[0]
                .replace('"', '')
                .replace(",", "")
            )

            columnas.append(columna)

        reporte["tablas"].append(
            {
                "nombre": nombre,
                "columnas": columnas
            }
        )

    # ========================================================
    # RPC
    # ========================================================

    rpc_names = re.findall(
        r'CREATE (?:OR REPLACE )?FUNCTION (?:public\.)?"?(\w+)"?',
        content
    )

    reporte["rpcs"] = sorted(
        list(
            set(
                [
                    r
                    for r in rpc_names
                    if r.startswith("fn_")
                ]
            )
        )
    )

    # ========================================================
    # RLS
    # ========================================================

    rls_metadata = re.finditer(
        r'^-- Name: (.*?) (.*?); Type: POLICY; Schema: (.*?); Owner: (.*?)$',
        content,
        re.MULTILINE
    )

    for m in rls_metadata:

        tabla, policy, schema, owner = m.groups()

        reporte["rls"].append(
            {
                "Table": tabla,
                "Name": f"{tabla} {policy}",
                "Schema": schema,
                "Owner": owner
            }
        )

    # ========================================================
    # CONTEO DE REGISTROS
    # ========================================================

    pattern_copy = (
        r'COPY (?:public\.)?"?(\w+)"?'
        r'\s*(?:\([^)]*\))?'
        r'\s*FROM stdin;\n'
        r'(.*?)\n\\.'
    )

    for match in re.finditer(
        pattern_copy,
        content,
        re.DOTALL
    ):

        tabla = match.group(1)

        raw_data = match.group(2)

        if (
            not raw_data
            or raw_data.isspace()
        ):
            reporte["conteos"][tabla] = 0
            continue

        rows = []

        for line in raw_data.split("\n"):

            line = line.strip()

            if not line:
                continue

            if line.startswith("--"):
                continue

            upper = line.upper()

            if upper.startswith(
                (
                    "SET ",
                    "SELECT ",
                    "ALTER ",
                    "CREATE ",
                    "DROP ",
                    "TRIGGER "
                )
            ):
                continue

            if (
                "PG_CATALOG." in upper
                or "CONSTRAINTS" in upper
            ):
                continue

            rows.append(line)

        reporte["conteos"][tabla] = len(rows)

    # ========================================================
    # ÍNDICES
    # ========================================================

    idx_matches = re.finditer(
        r'CREATE (?:UNIQUE )?INDEX "?(\w+)"? '
        r'ON (?:public\.)?"?(\w+)"? '
        r'USING \w+ '
        r'\((.*?)\);',
        content
    )

    for m in idx_matches:

        reporte["indices"].append(
            {
                "Nombre": m.group(1),
                "Tabla": m.group(2),
                "Columnas": m.group(3).replace('"', '')
            }
        )

    # ========================================================
    # ENUMS
    # ========================================================

    enum_matches = re.finditer(
        r'CREATE TYPE (?:public\.)?"?(\w+)"? '
        r'AS ENUM \((.*?)\);',
        content,
        re.DOTALL
    )

    for m in enum_matches:

        valores = (
            m.group(2)
            .replace("'", "")
            .replace("\n", "")
            .strip()
        )

        reporte["enums"].append(
            {
                "Nombre": m.group(1),
                "Valores": valores
            }
        )

    return reporte


# ============================================================
# GENERADOR MARKDOWN
# ============================================================

def generar_markdown(datos, output_file):

    timestamp = datetime.now().strftime(
        "%d/%m/%Y %H:%M"
    )

    with open(
        output_file,
        "w",
        encoding="utf-8"
    ) as f:

        f.write("# Informe de Auditoría de Backup\n\n")
        f.write(f"Generado: {timestamp}\n\n")

        # ----------------------------------------------------
        # TABLAS
        # ----------------------------------------------------

        f.write("## 1. Estructura de la Base de Datos\n\n")

        for tabla in datos["tablas"]:

            f.write(
                f"- **Tabla:** {tabla['nombre']}\n"
            )

            f.write(
                f"  - Columnas: "
                f"{', '.join(tabla['columnas'])}\n"
            )

        # ----------------------------------------------------
        # RPC
        # ----------------------------------------------------

        f.write("\n## 2. Funciones RPC\n\n")

        if datos["rpcs"]:

            for rpc in datos["rpcs"]:
                f.write(f"- {rpc}\n")

        else:

            f.write(
                "No se detectaron funciones fn_.\n"
            )

        # ----------------------------------------------------
        # RLS
        # ----------------------------------------------------

        f.write("\n## 3. Políticas RLS\n\n")

        tablas_con_rls = set(
            [
                r["Table"]
                for r in datos["rls"]
            ]
        )

        tablas_totales = set(
            [
                t["nombre"]
                for t in datos["tablas"]
            ]
        )

        tablas_sin_rls = (
            tablas_totales - tablas_con_rls
        )

        for r in datos["rls"]:

            f.write(
                f"- {r['Name']} "
                f"(Schema={r['Schema']})\n"
            )

        if tablas_sin_rls:

            f.write(
                "\n### Advertencia: Tablas sin RLS\n\n"
            )

            for t in sorted(tablas_sin_rls):

                f.write(
                    f"- {t}\n"
                )

        # ----------------------------------------------------
        # ÍNDICES
        # ----------------------------------------------------

        f.write("\n## 4. Índices\n\n")

        for idx in datos["indices"]:

            f.write(
                f"- {idx['Nombre']} "
                f"({idx['Tabla']}) "
                f"[{idx['Columnas']}]\n"
            )

        # ----------------------------------------------------
        # ENUMS
        # ----------------------------------------------------

        f.write("\n## 5. ENUMS\n\n")

        for enum in datos["enums"]:

            f.write(
                f"- {enum['Nombre']} "
                f"→ {enum['Valores']}\n"
            )

        # ----------------------------------------------------
        # CONTEOS
        # ----------------------------------------------------

        f.write(
            "\n## 6. Conteo de Registros\n\n"
        )

        f.write(
            "| Tabla | Registros |\n"
        )

        f.write(
            "|--------|-----------|\n"
        )

        for tabla, cantidad in sorted(
            datos["conteos"].items(),
            key=lambda x: x[1],
            reverse=True
        ):

            f.write(
                f"| {tabla} | {cantidad} |\n"
            )


# ============================================================
# MAIN
# ============================================================

def main():

    if len(sys.argv) != 3:

        print(
            "Uso: python auditoria.py "
            "<backup.zip> "
            "<salida.md>"
        )

        sys.exit(1)

    zip_path = sys.argv[1]
    output_md = sys.argv[2]

    datos = analizar_datos_frescos(zip_path)

    generar_markdown(
        datos,
        output_md
    )

    print(
        f"Auditoría generada: {output_md}"
    )


if __name__ == "__main__":
    main()