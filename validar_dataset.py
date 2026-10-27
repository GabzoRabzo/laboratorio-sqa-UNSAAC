import pandas as pd

# Cargar dataset
csv_file = 'incidencias_software.csv'
df = pd.read_csv(csv_file)

print('=' * 60)
print('AUDITORÍA SQA: INGESTA Y VALIDACIÓN DE INCIDENCIAS')
print('=' * 60)
print(f'Total de incidencias cargadas: {len(df)}')
print('-' * 60)
print(df.to_string(index=False))
print('-' * 60)

# Resumen por Severidad
print('\n1. RESUMEN POR SEVERIDAD:')
sev_summary = df.groupby('severidad').agg(
    Cantidad=('id', 'count'),
    Horas_Deteccion=('tiempo_deteccion_hs', 'sum'),
    Horas_Reparacion=('tiempo_reparacion_hs', 'sum')
).reset_index()
print(sev_summary.to_string(index=False))

# Resumen por Categoría de Error
print('\n2. RESUMEN POR CATEGORÍA DE ERROR:')
cat_summary = df.groupby('categoria_error').agg(
    Cantidad=('id', 'count'),
    Horas_Deteccion=('tiempo_deteccion_hs', 'sum'),
    Horas_Reparacion=('tiempo_reparacion_hs', 'sum')
).sort_values(by='Cantidad', ascending=False).reset_index()
print(cat_summary.to_string(index=False))

print('\n3. MÉTRICAS GLOBALES SQA:')
tot_det = df['tiempo_deteccion_hs'].sum()
tot_rep = df['tiempo_reparacion_hs'].sum()
print(f'• Esfuerzo total de detección: {tot_det} horas')
print(f'• Esfuerzo total de reparación: {tot_rep} horas')
print(f'• Esfuerzo acumulado de calidad: {tot_det + tot_rep} horas')
print(f'• Promedio de detección por falla: {df["tiempo_deteccion_hs"].mean():.2f} horas')
print(f'• Promedio de reparación por falla: {df["tiempo_reparacion_hs"].mean():.2f} horas')
print('=' * 60)
