# ✦ Sistema de Gestión de Solicitudes de Certificados

Un proyecto final desarrollado para el curso de **Fundamentos de Programación**. Consiste en una aplicación web dinámica construida en Python con Flask para gestionar y centralizar el registro en memoria de trámites de certificados académicos.

## Tecnologías Utilizadas

* **Lenguaje:** Python 3
* **Framework Web:** Flask
* **Motor de Plantillas:** Jinja2
* **Frontend:** HTML5 (formularios nativos)

## Estructura del Proyecto

```text
Fundamentals_of_Programming/
│
├── templates/
│   ├── formulario.html    # Vista principal: formulario de registro
│   └── reporte.html       # Vista de consulta: lista de solicitudes
├── LICENSE                # Licencia de código abierto (MIT)
├── main.py                # Servidor Flask, lógica de negocio y validaciones
├── README.md              # Documentación del proyecto :3
└── requirements.txt       # Dependencias del proyecto (Flask)
```

## Ejecución

```bash
# 1. Instalar dependencias
pip install -r requirements.txt

# 2. Iniciar el servidor
python main.py
```

✦ Finalmente, podrás abrirlo en el navegador: `http://localhost:5019`

✦ Para apagar el servidor: `Ctrl + C` en la terminal y así liberar la consola.
