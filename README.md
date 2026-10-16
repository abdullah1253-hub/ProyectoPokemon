# Proyecto Pokémon - Fase 2

Aplicación web desarrollada con Flask para gestionar un catálogo de Pokémon (Pokédex), filtrar por atributos y realizar enfrentamientos aleatorios en una arena de batalla.

## Estructura del Repositorio

```text
ProyectoPokemon/
├── app/
│   ├── main.py                   # Servidor Flask y lógica de rutas
│   ├── static/
│   │   └── style.css             # Hoja de estilos
│   └── templates/
│       ├── base.html             # Plantilla base (Jinja2)
│       ├── index.html            # Registro de entrenador
│       ├── listado.html          # Vista de catálogo
│       ├── detalle.html          # Ficha del Pokémon
│       └── battle.html           # Arena de combate
├── data/
│   └── pokemons-competitive.json # Base de datos local
├── requirements.txt
└── README.md
```

## Requisitos e Instalación

1. Crear y activar el entorno virtual:

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

2. Instalar dependencias:

```bash
pip install -r requirements.txt
```

3. Ejecutar la aplicación:

```bash
python app/main.py
```

La aplicación se desplegará en `http://localhost:8080/`.

## Funcionalidades

### 1. Registro de Entrenador (`/`)
* Formulario mediante `POST`.
* Se valida en el servidor que la cadena tenga entre 3 y 15 caracteres.
* Al no usar bases de datos ni sesiones en esta fase, el parámetro `trainer` se mantiene pasando la variable por la URL (`?trainer=Nombre`) entre todas las vistas.

### 2. Filtro de Pokémon (`/pokemons/`)
* Utiliza el método `GET`.
* Se usa `GET` en los filtros para que los parámetros de búsqueda queden guardados en la URL (`?name=pika&type=electric`), lo que permite recargar la página o compartir el enlace con los filtros aplicados.
* En `main.py` se leen los argumentos con `request.args` y se filtra la lista antes de enviarla al renderizado.

### 3. Elección de Inicial para Batalla (`/pokemons/`)
* Formulario independiente en la misma vista usando `POST`.
* Se valida que el Pokémon introducido exista en la lista cargada desde el JSON.
* Gestiona las validaciones y redirecciones correspondientes.

### 4. Ficha de Detalle (`/pokemons/<id>`)
* Busca el objeto por su ID dinámico.
* Calcula rangos en la plantilla Jinja2 para clasificar el peso e independizar las barras de estadísticas.

### 5. Arena de Batalla (`/battle/`)
* Selecciona un oponente aleatorio mediante `random.choice()`.
* Elige 4 movimientos al azar para el Pokémon seleccionado utilizando `random.sample()`.

---

**Autor:** Abdullah Riaz