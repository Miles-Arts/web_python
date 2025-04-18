# 🌐 Web con Python, Flask, Jinja y Bootstrap 🤖

Este proyecto es una aplicación web creada utilizando **Python** y el microframework **Flask**. Además, se utiliza **HTML** con **Jinja2** para las plantillas dinámicas y **Bootstrap** para el diseño responsivo y estilizado de las páginas web.

## 🚀 Características
- **Flask**: Framework ligero y fácil de usar para el desarrollo web.
- **Jinja2**: Motor de plantillas para generar contenido dinámico en las páginas HTML.
- **Bootstrap**: Framework CSS para un diseño moderno y responsivo.
- **Rutas**: Implementación de rutas para diferentes páginas como la principal, lenguajes y contacto.

## 📂 Estructura del Proyecto
```
WEB-PYTHON/
├── index.py          # Archivo principal de la aplicación Flask
├── templates/        # Carpeta que contiene las plantillas HTML
│   ├── base.html     # Plantilla base con estructura común
│   ├── index.html    # Página principal
│   ├── contacto.html # Página de contacto
│   ├── lenguajes.html # Página de lenguajes
```

## 🛠️ Requisitos
- Python 3.7 o superior
- Flask (instalable con `pip install flask`)
- Bootstrap (integrado a través de CDN en las plantillas HTML)

## ▶️ Cómo ejecutar la aplicación
1. Clona este repositorio o descarga los archivos.
2. Navega al directorio del proyecto:
   ```bash
   cd WEB-PYTHON
   ```
3. Crea y activa un entorno virtual (opcional pero recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```
4. Instala Flask:
   ```bash
   pip install flask
   ```
5. Ejecuta la aplicación:
   ```bash
   python index.py
   ```
6. Abre tu navegador y ve a `http://127.0.0.1:5017`.

## 📄 Licencia
Este proyecto está bajo la licencia MIT.

---
¡Disfruta creando aplicaciones web con Python, Flask, Jinja y Bootstrap! 🎉
