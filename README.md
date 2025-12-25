# 💰 Rastreador de Gastos Personales (CLI)

¡Bienvenido a mi gestor de finanzas personales! Esta es una aplicación de consola construida con **Python** que permite registrar, visualizar y filtrar gastos diarios de manera eficiente.

El proyecto utiliza persistencia de datos mediante archivos **CSV**, lo que significa que tus gastos se guardan automáticamente y no se pierden al cerrar el programa.

## 🚀 Características Principales

* **📝 Registro de Gastos:** Guarda concepto, monto y fecha.
* **💾 Persistencia de Datos:** Uso de la librería `csv` y `os` para gestionar una base de datos local en `mis_gastos.csv`.
* **🔍 Filtros Avanzados:**
    * Por **Monto Mínimo** (ej: ver gastos mayores a $50).
    * Por **Nombre de Producto** (ej: buscar todos los gastos de "Pizza").
    * Por **Fecha Específica** (ej: ver qué gastaste el 25/12/2023).
* **🛡️ Validaciones:** El sistema es robusto ante errores de usuario (evita cierres inesperados si ingresas texto en lugar de números).
* **✨ Formato Limpio:** Uso de tablas formateadas en la terminal para una lectura fácil.

## 🛠️ Tecnologías Utilizadas

* **Lenguaje:** Python 3
* **Librerías Nativas:**
    * `csv` (Manejo de archivos de texto estructurados)
    * `os` (Verificación de existencia de archivos en el sistema)
* **Control de Versiones:** Git & GitHub

## 💻 ¿Cómo ejecutar este proyecto?

Si quieres probar este código en tu computadora, sigue estos pasos:

1.  **Asegúrate de tener Python instalado.**
2.  **Clona este repositorio:**
    ```bash
    git clone [https://github.com/rod670/rastreador-gastos-python.git](https://github.com/rod670/rastreador-gastos-python.git)
    ```
3.  **Entra a la carpeta del proyecto:**
    ```bash
    cd rastreador-gastos-python
    ```
4.  **Ejecuta el script:**
    ```bash
    python gastos.py
    ```

## 📸 Vistazo al Proyecto

El menú principal te permite navegar fácilmente:

```text
=== REGISTRO DE GASTOS PERSONALES ===
1. Agregar gasto
2. Ver gastos y Filtros
3. Salir
```
Rodrigo Gómez De La Torre - Estudiante de ingeniería de software