# Informe de Auditoría de Backup

Generado: 19/09/2026 05:15

## 1. Estructura de la Base de Datos

- **Tabla:** mvp_periodo
  - Columnas: id, codigo, fecha_inicio, fecha_fin, estado, created_at, updated_at
- **Tabla:** mvp_cajas
  - Columnas: id, nombre, tipo, user_id, created_at, updated_at
- **Tabla:** mvp_cierre_ctacte
  - Columnas: id, cierre_id, socio_id, periodo_id, saldo_inicial, total_dividendos, total_ingresos, total_adelantos, total_retiros, total_liquidaciones, total_aportes, saldo_final, cantidad_asientos, created_at, updated_at
- **Tabla:** mvp_cierre_detalle
  - Columnas: id, cierre_id, caja_id, saldo_inicial, saldo_final, created_at, updated_at, total_ingresos, total_egresos, monto_dividendos, monto_transferido_tesoreria, porc_aplicado, tipo_dividendo_aplicado
- **Tabla:** mvp_cierre_resumen
  - Columnas: id, cierre_id, total_ventas, total_compras, cantidad_ventas, cantidad_compras, cantidad_productos_vendidos, cantidad_clientes_activos, cantidad_proveedores_activos, created_at, updated_at
- **Tabla:** mvp_cierres
  - Columnas: id, created_at, updated_at, periodo_id, total_cajas, cajas_cerradas, fecha_cierre, usuario_cierre
- **Tabla:** mvp_clientes
  - Columnas: id, razon_social, cuit, created_at, updated_at, activo, creado_por, socio_captador_id
- **Tabla:** mvp_comprobante
  - Columnas: id, tipo_id, nro_int, estado, fecha_emision, socio_id, cliente_id, venta_id, operacion_caja_id, modalidad, total, numero_anterior, motivo_anulacion, fecha_anulacion, emitido_por, reimpresiones, created_at, updated_at, nro_ext, canal_entrega, fecha_entrega_comprobante, correo_enviado_at
- **Tabla:** mvp_comprobante_linea
  - Columnas: id, comprobante_id, orden, descripcion, cantidad, precio_unitario, subtotal, created_at, updated_at
- **Tabla:** mvp_comprobante_tipo
  - Columnas: id, codigo, nombre, nombre_impreso, leyenda_pie, admite_lineas, contraparte, ultimo_numero, activa, orden, created_at, updated_at, prefijo
- **Tabla:** mvp_config_interna
  - Columnas: id, organizacion_nombre, updated_at, cliente_tester_id, proveedor_tester_id
- **Tabla:** mvp_config_seguridad
  - Columnas: id, clave_baja_venta_hash, updated_at
- **Tabla:** mvp_ctacte
  - Columnas: id, socio_id, operacion_id, tipo_mov_ctacte, monto_debe, monto_haber, fecha, descripcion, created_at, updated_at, afecta_saldo, periodo_id
- **Tabla:** mvp_egresos
  - Columnas: id, socio_id, proveedor_id, tipo, monto, fecha, descripcion, created_at, updated_at
- **Tabla:** mvp_egresos_auditoria
  - Columnas: id, accion, egreso_id, usuario_id, periodo_id, motivo, fecha_egreso, tipo_egreso, socio_id, socio_nombre, proveedor_nombre, caja_id, caja_nombre, monto_antes, monto_despues, campos_cambiados, snapshot_antes, snapshot_despues, created_at, updated_at
- **Tabla:** mvp_movimientos_caja
  - Columnas: id, caja_id, monto, fecha, tipo_referencia, referencia_id, created_at, updated_at, operacion_id
- **Tabla:** mvp_operacion_caja
  - Columnas: id, tipo_operacion_id, fecha, usuario_id, estado, caja_origen_id, caja_destino_id, tercero_id, tipo_tercero, referencia_externa, observaciones, created_at, updated_at, documento_tipo, documento_id, operacion_relacionada_id, periodo_id
- **Tabla:** mvp_productos
  - Columnas: id, nombre, precio_lista, activo, created_at, updated_at, sigla
- **Tabla:** mvp_proveedores
  - Columnas: id, nombre, cuit_cuil, created_at, updated_at, activo, creado_por
- **Tabla:** mvp_reglas_negocio
  - Columnas: id, id_base, version, titulo, modulo, estado, sustituida_por, causa_sustitucion, definicion, descripcion_completa, tags, tablas_relacionadas, rpcs_relacionadas, pantallas_relacionadas, version_doc, fecha_actualizacion, created_at, updated_at, id_version_sistema, definicion_usuario
- **Tabla:** mvp_rendiciones
  - Columnas: id, caja_id, socio_id, periodo_id, saldo_libro, efectivo_declarado, faltante, operacion_liquidacion_id, usuario_id, fecha, created_at, updated_at
- **Tabla:** mvp_repartidores
  - Columnas: id, user_id, activo, created_at, updated_at
- **Tabla:** mvp_socios
  - Columnas: id, user_id, porc_ganancia, porc_venta, created_at, updated_at
- **Tabla:** mvp_system_status
  - Columnas: id, on_line, updated_at
- **Tabla:** mvp_tipo_operaciones
  - Columnas: id, codigo, nombre, descripcion, modulo, ambito, cantidad_mov, usa_caja_origen, usa_caja_destino, usa_tercero, tipo_tercero, requiere_documento, tipo_documento, rpc_handler, roles_permitidos, metadata, activa, orden, created_at, updated_at, usa_ctacte, ctacte_efecto, mov_es_multiplo
- **Tabla:** mvp_users
  - Columnas: id, email, rol, cliente_id, nombre, activo, created_at, updated_at, telefono, rol_tesorero, es_tester
- **Tabla:** mvp_ventas
  - Columnas: id, cliente_id, socio_id, socio_cobrador_id, created_at, fecha_entrega, estado, total, notas, updated_at, repartidor_id, motivo_anulacion, fecha_asignacion, fecha_anulacion
- **Tabla:** mvp_ventas_auditoria
  - Columnas: id, accion, venta_id, usuario_id, periodo_id, motivo, campos_cambiados, modo_nro, socio_id_antes, socio_id_despues, fecha_entrega_antes, fecha_entrega_despues, cliente_id_antes, cliente_id_despues, nro_ext_antes, nro_ext_despues, comprobante_antes_id, comprobante_despues_id, cobro_resellado, total, snapshot_antes, snapshot_despues, created_at, updated_at
- **Tabla:** mvp_ventas_bajas
  - Columnas: id, venta_id, periodo_id, fecha_baja, usuario_baja_id, estado_previo, nro_factura, fecha_entrega, cliente_id, cliente_razon_social, socio_id, socio_nombre, repartidor_nombre, total, caja_afectada_id, caja_afectada_nombre, motivo, snapshot, created_at, updated_at
- **Tabla:** mvp_ventas_detalle
  - Columnas: id, venta_id, producto_id, cantidad, precio_lista, precio_real, created_at, updated_at

## 2. Funciones RPC

- fn_abrir_periodo
- fn_actualizar_config_interna
- fn_actualizar_mi_telefono
- fn_actualizar_usuario
- fn_anular_venta
- fn_asignar_reparto
- fn_baja_egreso
- fn_baja_venta
- fn_caja_actual_venta
- fn_caja_real_cobro
- fn_cancelar_prestamo_socio
- fn_carga_rapida_venta
- fn_config_interna
- fn_corregir_egreso
- fn_corregir_venta
- fn_crear_usuario
- fn_ctacte_resumen_socios
- fn_cuenta_socio
- fn_dashboard_cajas_repartidores
- fn_dashboard_delegadas_header
- fn_dashboard_periodo
- fn_definir_clave_baja_venta
- fn_ejecutar_cierre
- fn_emitir_comprobante
- fn_fecha_cobro
- fn_fecha_local
- fn_fecha_local_desde_ts
- fn_guard_periodo_operacion
- fn_haber_ctacte_a_fecha
- fn_informe_cierre
- fn_listar_movimientos_mi_caja
- fn_listar_prestamos_socio
- fn_listar_rendiciones_pendientes
- fn_listar_socios
- fn_listar_socios_para_prestamo
- fn_listar_transferencias_periodo
- fn_listar_ventas_pendientes_caja
- fn_movimientos_caja_central
- fn_movimientos_cajas_delegadas
- fn_movimientos_ctacte
- fn_movimientos_ctacte_todos
- fn_mvp_clientes_creado_por_inmutable
- fn_nombre_socio
- fn_periodo_vigente
- fn_periodo_vigente_id
- fn_precierre_estado
- fn_preview_cierre
- fn_rango_fecha_operacion
- fn_registrar_adelanto
- fn_registrar_aporte
- fn_registrar_cobro_venta
- fn_registrar_egreso
- fn_registrar_egreso_completo
- fn_registrar_entrega
- fn_registrar_ingreso
- fn_registrar_prestamo_socio
- fn_registrar_retiro
- fn_registrar_transferencia
- fn_render_rn
- fn_render_rn_jsonb
- fn_rendir_caja_socio
- fn_rendir_dia
- fn_rendir_dia_administrativo
- fn_resumen_ctacte_periodo
- fn_revocar_sesiones_tester
- fn_saldo_caja_a_fecha
- fn_saldo_neto_periodo
- fn_snapshot_ctacte
- fn_socio_actual
- fn_test_conexion
- fn_tester_invariante_egresos
- fn_tester_invariante_ventas
- fn_toggle_online
- fn_ts_desde_fecha_local
- fn_validar_operador_no_repartidor

## 3. Políticas RLS

- mvp_cajas cajas_access (Schema=public)
- mvp_cajas cajas_access_repartidor (Schema=public)
- mvp_cajas cajas_socio_ver_socios (Schema=public)
- mvp_cierre_ctacte cierre_ctacte_access (Schema=public)
- mvp_cierre_detalle cierre_detalle_access (Schema=public)
- mvp_cierre_resumen cierre_resumen_select (Schema=public)
- mvp_cierres cierres_access (Schema=public)
- mvp_clientes clientes_insert (Schema=public)
- mvp_clientes clientes_insert_tester_negado (Schema=public)
- mvp_clientes clientes_select (Schema=public)
- mvp_clientes clientes_update (Schema=public)
- mvp_clientes clientes_update_tester_negado (Schema=public)
- mvp_comprobante_linea comprobante_linea_select (Schema=public)
- mvp_comprobante comprobante_select (Schema=public)
- mvp_comprobante_tipo comprobante_tipo_select (Schema=public)
- mvp_config_interna config_interna_delete_negado (Schema=public)
- mvp_config_interna config_interna_insert_negado (Schema=public)
- mvp_config_interna config_interna_select_authenticated (Schema=public)
- mvp_config_interna config_interna_update_negado (Schema=public)
- mvp_ctacte ctacte_access (Schema=public)
- mvp_egresos egresos_access_admin_tesorero (Schema=public)
- mvp_egresos egresos_access_socio (Schema=public)
- mvp_egresos_auditoria egresos_auditoria_select_admin_tesorero (Schema=public)
- mvp_egresos egresos_delete_socio_si_huerfano (Schema=public)
- mvp_egresos egresos_no_update (Schema=public)
- mvp_movimientos_caja movimientos_access (Schema=public)
- mvp_tipo_operaciones mvp_tipo_operaciones_select_authenticated (Schema=public)
- mvp_operacion_caja operacion_caja_access (Schema=public)
- mvp_periodo periodo_select_authenticated (Schema=public)
- mvp_productos productos_insert (Schema=public)
- mvp_productos productos_insert_tester_negado (Schema=public)
- mvp_productos productos_select (Schema=public)
- mvp_productos productos_update_admin (Schema=public)
- mvp_proveedores proveedores_insert (Schema=public)
- mvp_proveedores proveedores_insert_tester_negado (Schema=public)
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
- mvp_users users_update_tester_negado (Schema=public)
- mvp_ventas ventas_access_admin_tesorero (Schema=public)
- mvp_ventas ventas_access_repartidor (Schema=public)
- mvp_ventas ventas_access_socio_todas (Schema=public)
- mvp_ventas_auditoria ventas_auditoria_select_admin_tesorero (Schema=public)
- mvp_ventas_bajas ventas_bajas_select_admin (Schema=public)
- mvp_ventas_detalle ventas_detalle_access (Schema=public)
- mvp_ventas_detalle ventas_detalle_insert (Schema=public)
- mvp_ventas ventas_insert_admin (Schema=public)
- mvp_ventas ventas_insert_socio (Schema=public)

### Advertencia: Tablas sin RLS

- mvp_config_seguridad

## 4. Índices

- idx_cajas_tipo (mvp_cajas) [tipo]
- idx_cierre_ctacte_cierre (mvp_cierre_ctacte) [cierre_id]
- idx_cierre_ctacte_periodo (mvp_cierre_ctacte) [periodo_id]
- idx_cierre_ctacte_socio (mvp_cierre_ctacte) [socio_id]
- idx_cierre_detalle_caja (mvp_cierre_detalle) [caja_id]
- idx_cierre_detalle_cierre (mvp_cierre_detalle) [cierre_id]
- idx_egresos_auditoria_accion (mvp_egresos_auditoria) [accion, created_at DESC]
- idx_egresos_auditoria_created (mvp_egresos_auditoria) [created_at DESC]
- idx_egresos_auditoria_egreso (mvp_egresos_auditoria) [egreso_id]
- idx_egresos_auditoria_periodo (mvp_egresos_auditoria) [periodo_id, created_at DESC]
- idx_movimientos_caja (mvp_movimientos_caja) [caja_id]
- idx_movimientos_caja_operacion (mvp_movimientos_caja) [operacion_id]
- idx_mvp_clientes_socio_captador (mvp_clientes) [socio_captador_id]
- idx_mvp_ctacte_fecha (mvp_ctacte) [fecha]
- idx_mvp_ctacte_operacion_id (mvp_ctacte) [operacion_id]
- idx_mvp_ctacte_periodo_id (mvp_ctacte) [periodo_id]
- idx_mvp_ctacte_socio_id (mvp_ctacte) [socio_id]
- idx_mvp_ctacte_socio_periodo (mvp_ctacte) [socio_id, periodo_id]
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
- idx_ventas_auditoria_created (mvp_ventas_auditoria) [created_at DESC]
- idx_ventas_auditoria_periodo (mvp_ventas_auditoria) [periodo_id, created_at DESC]
- idx_ventas_auditoria_usuario (mvp_ventas_auditoria) [usuario_id]
- idx_ventas_auditoria_venta (mvp_ventas_auditoria) [venta_id]
- idx_ventas_bajas_factura (mvp_ventas_bajas) [nro_factura]
- idx_ventas_bajas_periodo (mvp_ventas_bajas) [periodo_id, fecha_baja DESC]
- idx_ventas_bajas_venta (mvp_ventas_bajas) [venta_id]
- idx_ventas_cliente (mvp_ventas) [cliente_id]
- idx_ventas_estado (mvp_ventas) [estado]
- idx_ventas_repartidor_id (mvp_ventas) [repartidor_id) WHERE (repartidor_id IS NOT NULL]
- idx_ventas_socio (mvp_ventas) [socio_id]
- ix_mvp_comprobante_cliente (mvp_comprobante) [cliente_id]
- ix_mvp_comprobante_fecha (mvp_comprobante) [fecha_emision]
- ix_mvp_comprobante_operacion (mvp_comprobante) [operacion_caja_id]
- ix_mvp_comprobante_socio (mvp_comprobante) [socio_id]
- ix_mvp_comprobante_venta (mvp_comprobante) [venta_id]
- mvp_productos_nombre_norm_uniq (mvp_productos) [translate(lower(btrim((nombre)::text)), 'áàäâãéèëêíìïîóòöôõúùüûñ'::text, 'aaaaaeeeeiiiiooooouuuun'::text)) WHERE (activo = true]
- mvp_productos_sigla_uniq (mvp_productos) [lower(btrim((sigla)::text))) WHERE ((activo = true) AND (sigla IS NOT NULL)]
- mvp_users_operador_cliente_unico (mvp_users) [cliente_id) WHERE (((rol)::text = 'operador'::text) AND (activo = true)]
- uq_cierre_resumen_cierre (mvp_cierre_resumen) [cierre_id]
- uq_cierres_periodo (mvp_cierres) [periodo_id]
- uq_mvp_comprobante_linea_orden (mvp_comprobante_linea) [comprobante_id, orden]
- uq_mvp_comprobante_serie (mvp_comprobante) [tipo_id, nro_int]
- uq_periodo_activo (mvp_periodo) [(true)) WHERE ((estado)::text <> 'CERRADO'::text]
- uq_periodo_codigo (mvp_periodo) [codigo]
- uq_unico_tesorero (mvp_users) [rol_tesorero) WHERE (rol_tesorero = true]
- uq_unico_tester (mvp_users) [es_tester) WHERE (es_tester = true]

## 5. ENUMS


## 6. Conteo de Registros

| Tabla | Registros |
|--------|-----------|
| mvp_comprobante_linea | 566 |
| mvp_ventas_detalle | 533 |
| mvp_egresos_auditoria | 339 |
| mvp_operacion_caja | 329 |
| mvp_comprobante | 264 |
| mvp_ventas | 231 |
| mvp_reglas_negocio | 59 |
| mvp_egresos | 46 |
| mvp_proveedores | 33 |
| mvp_ctacte | 31 |
| mvp_clientes | 22 |
| mvp_tipo_operaciones | 17 |
| mvp_productos | 16 |
| mvp_cierre_detalle | 15 |
| mvp_cierre_ctacte | 12 |
| mvp_rendiciones | 12 |
| mvp_cajas | 9 |
| mvp_comprobante_tipo | 6 |
| mvp_users | 6 |
| mvp_periodo | 4 |
| mvp_repartidores | 4 |
| mvp_socios | 4 |
| mvp_ventas_auditoria | 4 |
| mvp_cierre_resumen | 3 |
| mvp_cierres | 3 |
| mvp_ventas_bajas | 3 |
| mvp_config_interna | 1 |
| mvp_config_seguridad | 1 |
| mvp_system_status | 1 |
