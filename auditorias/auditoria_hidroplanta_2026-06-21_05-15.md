# Informe de Auditoría de Backup

Generado: 21/06/2026 05:16

## 1. Estructura de la Base de Datos

- **Tabla:** mvp_periodo
  - Columnas: id, codigo, fecha_inicio, fecha_fin, estado, created_at, updated_at
- **Tabla:** mvp_cajas
  - Columnas: id, nombre, tipo, user_id, created_at, updated_at
- **Tabla:** mvp_cierre_detalle
  - Columnas: id, cierre_id, caja_id, saldo_inicial, saldo_final, created_at, updated_at, total_ingresos, total_egresos, monto_dividendos, monto_transferido_tesoreria, porc_aplicado, tipo_dividendo_aplicado
- **Tabla:** mvp_cierre_resumen
  - Columnas: id, cierre_id, total_ventas, total_compras, cantidad_ventas, cantidad_compras, cantidad_productos_vendidos, cantidad_clientes_activos, cantidad_proveedores_activos, created_at, updated_at
- **Tabla:** mvp_cierres
  - Columnas: id, created_at, updated_at, periodo_id, total_cajas, cajas_cerradas, fecha_cierre, usuario_cierre
- **Tabla:** mvp_clientes
  - Columnas: id, razon_social, cuit, created_at, updated_at, activo
- **Tabla:** mvp_ctacte
  - Columnas: id, socio_id, operacion_id, tipo_mov_ctacte, monto_debe, monto_haber, fecha, descripcion, created_at, updated_at
- **Tabla:** mvp_egresos
  - Columnas: id, socio_id, proveedor_id, tipo, monto, fecha, descripcion, created_at, updated_at
- **Tabla:** mvp_movimientos_caja
  - Columnas: id, caja_id, monto, fecha, tipo_referencia, referencia_id, created_at, updated_at, operacion_id
- **Tabla:** mvp_operacion_caja
  - Columnas: id, tipo_operacion_id, fecha, usuario_id, estado, caja_origen_id, caja_destino_id, tercero_id, tipo_tercero, referencia_externa, observaciones, created_at, updated_at, documento_tipo, documento_id, operacion_relacionada_id, periodo_id
- **Tabla:** mvp_productos
  - Columnas: id, nombre, precio_lista, activo, created_at, updated_at, sigla
- **Tabla:** mvp_proveedores
  - Columnas: id, nombre, cuit_cuil, created_at, updated_at, activo
- **Tabla:** mvp_reglas_negocio
  - Columnas: id, id_base, version, titulo, modulo, estado, sustituida_por, causa_sustitucion, definicion, descripcion_completa, tags, tablas_relacionadas, rpcs_relacionadas, pantallas_relacionadas, version_doc, fecha_actualizacion, created_at, updated_at, id_version_sistema
- **Tabla:** mvp_rendiciones
  - Columnas: id, caja_id, socio_id, periodo_id, saldo_libro, efectivo_declarado, faltante, operacion_liquidacion_id, usuario_id, fecha, created_at, updated_at
- **Tabla:** mvp_repartidores
  - Columnas: id, user_id, activo, created_at, updated_at
- **Tabla:** mvp_socios
  - Columnas: id, user_id, porc_ganancia, porc_venta, created_at, updated_at
- **Tabla:** mvp_system_status
  - Columnas: id, on_line, updated_at
- **Tabla:** mvp_tipo_operaciones
  - Columnas: id, codigo, nombre, descripcion, modulo, ambito, cantidad_mov, usa_caja_origen, usa_caja_destino, usa_tercero, tipo_tercero, requiere_documento, tipo_documento, rpc_handler, roles_permitidos, metadata, activa, orden, created_at, updated_at, usa_ctacte, ctacte_efecto
- **Tabla:** mvp_users
  - Columnas: id, email, rol, cliente_id, nombre, activo, created_at, updated_at, telefono
- **Tabla:** mvp_ventas
  - Columnas: id, cliente_id, socio_id, socio_cobrador_id, created_at, fecha_entrega, estado, total, notas, updated_at, repartidor_id, nro_factura, motivo_anulacion
- **Tabla:** mvp_ventas_detalle
  - Columnas: id, venta_id, producto_id, cantidad, precio_lista, precio_real, created_at, updated_at

## 2. Funciones RPC

- fn_abrir_periodo
- fn_actualizar_mi_telefono
- fn_actualizar_usuario
- fn_anular_venta
- fn_asignar_reparto
- fn_caja_destino_cobro
- fn_cancelar_prestamo_socio
- fn_carga_rapida_venta
- fn_crear_usuario
- fn_cuenta_socio
- fn_dashboard_periodo
- fn_ejecutar_cierre
- fn_fecha_cobro
- fn_fecha_local
- fn_guard_periodo_operacion
- fn_listar_movimientos_mi_caja
- fn_listar_prestamos_socio
- fn_listar_socios_para_prestamo
- fn_nombre_socio
- fn_periodo_vigente
- fn_periodo_vigente_id
- fn_preview_cierre
- fn_registrar_adelanto
- fn_registrar_aporte
- fn_registrar_cobro_venta
- fn_registrar_egreso
- fn_registrar_entrega
- fn_registrar_prestamo_socio
- fn_registrar_retiro
- fn_registrar_transferencia
- fn_rendir_caja_socio
- fn_rendir_dia
- fn_saldo_neto_periodo
- fn_test_conexion
- fn_toggle_online
- fn_validar_operador_no_repartidor

## 3. Políticas RLS

- mvp_cajas cajas_access (Schema=public)
- mvp_cajas cajas_access_repartidor (Schema=public)
- mvp_cajas cajas_socio_ver_socios (Schema=public)
- mvp_cierre_detalle cierre_detalle_access (Schema=public)
- mvp_cierre_resumen cierre_resumen_select (Schema=public)
- mvp_cierres cierres_access (Schema=public)
- mvp_clientes clientes_insert (Schema=public)
- mvp_clientes clientes_select (Schema=public)
- mvp_clientes clientes_update (Schema=public)
- mvp_ctacte ctacte_access (Schema=public)
- mvp_egresos egresos_access_admin_tesorero (Schema=public)
- mvp_egresos egresos_access_socio (Schema=public)
- mvp_egresos egresos_delete_socio_si_huerfano (Schema=public)
- mvp_egresos egresos_insert_socio (Schema=public)
- mvp_egresos egresos_no_update (Schema=public)
- mvp_movimientos_caja movimientos_access (Schema=public)
- mvp_tipo_operaciones mvp_tipo_operaciones_select_authenticated (Schema=public)
- mvp_operacion_caja operacion_caja_access (Schema=public)
- mvp_periodo periodo_select_authenticated (Schema=public)
- mvp_productos productos_insert (Schema=public)
- mvp_productos productos_select (Schema=public)
- mvp_productos productos_update_admin (Schema=public)
- mvp_proveedores proveedores_insert (Schema=public)
- mvp_proveedores proveedores_select (Schema=public)
- mvp_proveedores proveedores_update (Schema=public)
- mvp_reglas_negocio reglas_negocio_delete_negado (Schema=public)
- mvp_reglas_negocio reglas_negocio_insert_negado (Schema=public)
- mvp_reglas_negocio reglas_negocio_select_admin_tesorero_socio (Schema=public)
- mvp_reglas_negocio reglas_negocio_update_negado (Schema=public)
- mvp_rendiciones rendiciones_access (Schema=public)
- mvp_repartidores repartidores_select_admin_tesorero (Schema=public)
- mvp_repartidores repartidores_select_self (Schema=public)
- mvp_repartidores repartidores_select_socio_activos (Schema=public)
- mvp_socios socios_admin_tesorero (Schema=public)
- mvp_socios socios_admin_update (Schema=public)
- mvp_socios socios_self (Schema=public)
- mvp_system_status system_status_block_delete (Schema=public)
- mvp_system_status system_status_block_insert (Schema=public)
- mvp_system_status system_status_block_update (Schema=public)
- mvp_system_status system_status_read (Schema=public)
- mvp_tipo_operaciones tipo_operaciones_no_delete (Schema=public)
- mvp_tipo_operaciones tipo_operaciones_no_insert (Schema=public)
- mvp_tipo_operaciones tipo_operaciones_no_update (Schema=public)
- mvp_users users_admin_only (Schema=public)
- mvp_users users_privileged_read (Schema=public)
- mvp_users users_self_select (Schema=public)
- mvp_users users_socio_update_operador (Schema=public)
- mvp_ventas ventas_access_admin_tesorero (Schema=public)
- mvp_ventas ventas_access_repartidor (Schema=public)
- mvp_ventas ventas_access_socio_todas (Schema=public)
- mvp_ventas_detalle ventas_detalle_access (Schema=public)
- mvp_ventas_detalle ventas_detalle_insert (Schema=public)
- mvp_ventas ventas_insert_admin (Schema=public)
- mvp_ventas ventas_insert_socio (Schema=public)

## 4. Índices

- idx_cajas_tipo (mvp_cajas) [tipo]
- idx_cierre_detalle_caja (mvp_cierre_detalle) [caja_id]
- idx_cierre_detalle_cierre (mvp_cierre_detalle) [cierre_id]
- idx_movimientos_caja (mvp_movimientos_caja) [caja_id]
- idx_movimientos_caja_operacion (mvp_movimientos_caja) [operacion_id]
- idx_mvp_ctacte_fecha (mvp_ctacte) [fecha]
- idx_mvp_ctacte_operacion_id (mvp_ctacte) [operacion_id]
- idx_mvp_ctacte_socio_id (mvp_ctacte) [socio_id]
- idx_mvp_proveedores_activo (mvp_proveedores) [activo]
- idx_mvp_proveedores_cuit_cuil_unique (mvp_proveedores) [cuit_cuil) WHERE (cuit_cuil IS NOT NULL]
- idx_mvp_rendiciones_caja_id (mvp_rendiciones) [caja_id]
- idx_mvp_rendiciones_periodo_id (mvp_rendiciones) [periodo_id]
- idx_mvp_rendiciones_socio_id (mvp_rendiciones) [socio_id]
- idx_operacion_caja_destino (mvp_operacion_caja) [caja_destino_id]
- idx_operacion_caja_documento (mvp_operacion_caja) [documento_id]
- idx_operacion_caja_estado (mvp_operacion_caja) [estado]
- idx_operacion_caja_origen (mvp_operacion_caja) [caja_origen_id]
- idx_operacion_caja_periodo (mvp_operacion_caja) [periodo_id]
- idx_operacion_caja_relacionada (mvp_operacion_caja) [operacion_relacionada_id]
- idx_operacion_caja_tipo (mvp_operacion_caja) [tipo_operacion_id]
- idx_operacion_caja_usuario (mvp_operacion_caja) [usuario_id]
- idx_reglas_negocio_estado (mvp_reglas_negocio) [estado]
- idx_reglas_negocio_id_base (mvp_reglas_negocio) [id_base]
- idx_reglas_negocio_modulo (mvp_reglas_negocio) [modulo]
- idx_reglas_negocio_tags (mvp_reglas_negocio) [tags]
- idx_repartidores_activo (mvp_repartidores) [activo) WHERE (activo = true]
- idx_repartidores_user_id (mvp_repartidores) [user_id]
- idx_ventas_cliente (mvp_ventas) [cliente_id]
- idx_ventas_estado (mvp_ventas) [estado]
- idx_ventas_repartidor_id (mvp_ventas) [repartidor_id) WHERE (repartidor_id IS NOT NULL]
- idx_ventas_socio (mvp_ventas) [socio_id]
- mvp_productos_nombre_norm_uniq (mvp_productos) [translate(lower(btrim((nombre)::text)), 'áàäâãéèëêíìïîóòöôõúùüûñ'::text, 'aaaaaeeeeiiiiooooouuuun'::text)) WHERE (activo = true]
- mvp_productos_sigla_uniq (mvp_productos) [lower(btrim((sigla)::text))) WHERE ((activo = true) AND (sigla IS NOT NULL)]
- mvp_users_operador_cliente_unico (mvp_users) [cliente_id) WHERE (((rol)::text = 'operador'::text) AND (activo = true)]
- uq_cierre_resumen_cierre (mvp_cierre_resumen) [cierre_id]
- uq_cierres_periodo (mvp_cierres) [periodo_id]
- uq_periodo_activo (mvp_periodo) [(true)) WHERE ((estado)::text <> 'CERRADO'::text]
- uq_periodo_codigo (mvp_periodo) [codigo]

## 5. ENUMS


## 6. Conteo de Registros

| Tabla | Registros |
|--------|-----------|
| mvp_reglas_negocio | 44 |
| mvp_proveedores | 22 |
| mvp_cierres | 19 |
| mvp_ventas_detalle | 16 |
| mvp_productos | 15 |
| mvp_tipo_operaciones | 13 |
| mvp_movimientos_caja | 10 |
| mvp_operacion_caja | 9 |
| mvp_cajas | 8 |
| mvp_ventas | 8 |
| mvp_users | 6 |
| mvp_rendiciones | 5 |
| mvp_socios | 4 |
| mvp_cierre_detalle | 2 |
| mvp_ctacte | 2 |
| mvp_periodo | 1 |
| mvp_system_status | 1 |
