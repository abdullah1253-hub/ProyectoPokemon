# Proyecto Pokémon - Fase 4

Aplicación web desarrollada con Flask estructurada en una arquitectura por capas modular, utilizando Blueprints, formularios Flask-WTF y gestión de sesiones segura.

## Estructura del Repositorio

```text
ProyectoPokemon/
├── app/
│   ├── __init__.py
│   ├── services/
│   │   └── pokemon_service.py
│   ├── forms/
│   │   └── trainer_form.py
│   ├── utils/
│   │   └── decorators.py
│   ├── routes/
│   │   ├── auth_routes.py
│   │   └── pokemon_routes.py
│   ├── static/
│   │   └── style.css
│   └── templates/
│       ├── base.html
│       ├── index.html
│       ├── listado.html
│       ├── detalle.html
│       └── battle.html
├── data/
│   └── pokemons-competitive.json
├── requirements.txt
├── run.py
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
   python run.py
   ```

La aplicación se desplegará en `http://localhost:8080/`.

## Arquitectura y Funcionalidades

### 1. Arquitectura por Capas y Blueprints

El código se ha desacoplado de un único fichero y se ha organizado en capas funcionales dentro del paquete `app`:

- **Capa de Servicio (`services/`)**: centraliza la lectura del fichero JSON, el filtrado de Pokémon y la lógica aleatoria de oponentes mediante funciones puras.
- **Blueprints (`routes/`)**:
  - `auth_bp` (`auth_routes.py`): gestiona el acceso inicial, la validación y el cierre de sesión (`/logout`).
  - `pokemon_bp` (`pokemon_routes.py`): controla el catálogo, los filtros de búsqueda, las fichas de detalle y la arena de combate.

### 2. Registro y Autenticación con Flask-WTF (`/`)

- Utiliza una clase `TrainerForm` basada en `Flask-WTF` para gestionar el formulario de entrada.
- Incorpora protección contra ataques CSRF mediante `hidden_tag()` y validación automática de longitud (entre 3 y 15 caracteres) en el servidor.
- **Control de sesión**: si un usuario ya tiene una sesión activa (`session['trainer']`), visitar la raíz (`/`) redirige automáticamente al catálogo sin volver a mostrar el formulario.

### 3. Filtro de Pokémon (`/pokemons/`)

- Emplea el método `GET` para conservar los parámetros de búsqueda (`?name=pika&type=electric`) en la URL, facilitando la recarga y el uso compartido de enlaces.
- La lógica de filtrado se procesa de forma limpia desde la capa de servicio.

### 4. Elección de Inicial para Batalla (`/pokemons/`)

- Formulario independiente mediante `POST` que valida la existencia del Pokémon introducido antes de redirigir a la arena.

### 5. Ficha de Detalle (`/pokemons/<id>`)

- Busca dinámicamente el Pokémon por su identificador y calcula rangos de peso y estadísticas directamente en las plantillas Jinja2.

### 6. Arena de Batalla (`/battle/`)

- Selecciona un oponente aleatorio (`random.choice()`) y 4 movimientos (`random.sample()`).
- **Persistencia**: almacena los datos en `session['rival_pokemon']` y `session['user_moves']`, evitando cambios indeseados al refrescar la página (F5) y asegurando que solo se reinicien al seleccionar un nuevo Pokémon inicial.

---

**Autor:** Abdullah Riaz