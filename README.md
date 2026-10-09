# ProyectoPokemon

Proyecto desarrollado en Python para crear una aplicación web de batallas de Pokémon utilizando Flask.

## Requisitos

* Python
* Flask

## Instalación

Crear un entorno virtual:

```bash
py -m venv venv
```

Instalar las dependencias:

```bash
pip install -r requirements.txt
```

## Ejecución

Para ejecutar la aplicación:

```bash
python main.py
```

La aplicación estará disponible en:

http://localhost:8080/

## Autor

Abdullah Riaz























##  Estructura del Proyecto

```text
ProyectoPokemon/
├── app/
│   ├── main.py              # Servidor Flask, lógica de rutas y carga JSON
│   ├── static/
│   │   └── style.css        # Hoja de estilos global unificada
│   └── templates/
│       ├── base.html        # Plantilla maestra (Jinja2)
│       ├── index.html       # Vista de bienvenida
│       ├── listado.html     # Vista de catálogo (Grid 4x4)
│       └── detalle.html     # Vista individual con estadísticas
├── data/
│   └── pokemons-competitive.json # Base de datos del proyecto
└── README.md                # Documentación del proyecto