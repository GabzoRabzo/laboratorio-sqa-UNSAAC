# Laboratorio SQA UNSAAC – Gestión de Incidencias de Software
**Repositorio Oficial:** `laboratorio-sqa-UNSAAC`  
**Asignatura:** Ingeniería de Software II – Semestre 2026-II  
**Docente:** Mg. Alex F. Huillca Huaman  
**Institución:** Universidad Nacional de San Antonio Abad del Cusco (UNSAAC)  
**Facultad:** Ingeniería Eléctrica, Electrónica, Informática y Mecánica (FIEIM)  
**Escuela:** Ingeniería Informática y de Sistemas (EPIIS)  

---

## 👥 Equipo de Trabajo (Grupo 03)
| N° | Apellidos y Nombres | Código | Rol SQA |
|:--:|:--------------------|:------:|:--------|
| 1 | Rodriguez Ccoyto, Jairo Jaser | 221451 | Moderador / Lead QA |
| 2 | Toledo Bernal, Max Erixon | 221452 | Desarrollador / Autor |
| 3 | Pumaccahua Huallpa, Patrick Michael | 220213 | Auditor / Tester |
| 4 | Torres Bautista, Ronil Nilo | 220964 | Registrador / SQA Metrics |

---

## 📌 Propósito del Repositorio
Repositorio estructurado para el **Aseguramiento Estadístico de la Calidad del Software (ACS)** en el marco de la **Guía Práctica 03: Aseguramiento de la Calidad de Software**.

El objetivo es gestionar, versionar y analizar el histórico de incidencias (errores y defectos) del sistema transaccional web **TechBank SAC**, aplicando técnicas estadísticas (Diagrama de Pareto), cálculo de métricas de confiabilidad/disponibilidad (MTBF, MTTF, MTTR) y el marco de mejora continua **Seis Sigma (DMAMC)**.

---

## 📊 Diccionario de Datos (`incidencias_software.csv`)

El archivo [`incidencias_software.csv`](./incidencias_software.csv) contiene el dataset base con las primeras 10 incidencias registradas en el entorno de pruebas de aceptación:

| Campo | Tipo | Descripción | Valores Posibles |
|:------|:----:|:------------|:-----------------|
| `id` | Entero | Identificador único secuencial de la incidencia | 1, 2, 3, ... |
| `categoria_error` | Texto (Código) | Taxonomía estándar del error según causa raíz | `EEI`, `MCC`, `ERD`, `VEP`, `EDL`, `ICI`, `PLT` |
| `severidad` | Texto | Grado de impacto técnico y operativo en el sistema | `Serio`, `Moderado`, `Menor` |
| `tiempo_deteccion_hs` | Numérico (h) | Horas de inspección/testing invertidas en hallar la falla | 1.0 a 20.0 hs |
| `tiempo_reparacion_hs` | Numérico (h) | Horas de ingeniería requeridas para subsanar el defecto | 1.0 a 10.0 hs |

---

## 🏷️ Taxonomía de Errores (Codificación Oficial SQA)
1. **EEI (Especificaciones Erróneas / Incompletas):** Requisitos ambiguos, contradictorios o no especificados por el stakeholder.
2. **MCC (Mala Comunicación con el Cliente):** Discrepancias entre lo solicitado por el usuario y lo interpretado por el analista.
3. **ERD (Error en Representación de Datos):** Problemas en el diseño de modelos relacionales, esquemas o tipos de datos.
4. **VEP (Violación de Estándares de Programación):** Incumplimiento de guías de estilo, convenciones de nombrado o directrices de arquitectura.
5. **EDL (Error de Diseño Lógico):** Fallas algorítmicas, flujos de control erróneos o condiciones límite no contempladas.
6. **ICI (Interfaz Inconsistente):** Problemas de usabilidad, desalineación visual o fallas de navegación en UI/UX.
7. **PLT (Error de Traducción de Lenguaje):** Errores en la sintaxis, tipado o transpilación del código fuente.

---

## 🚀 Instrucciones de Ejecución Rápida
Para cargar y verificar el dataset en Python con Pandas:
```bash
python validar_dataset.py
```
