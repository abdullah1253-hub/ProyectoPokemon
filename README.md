# Proyecto Pokémon - Fase 3

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
* El nombre del entrenador se almacena en session['trainer'], eliminando la necesidad de pasar parámetros por la URL y protegiendo el acceso a las páginas posteriores.

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
* Selecciona un oponente aleatorio (random.choice()) y 4 movimientos (random.sample()), guardando ambos en session['rival_pokemon'] y session['user_moves'] para garantizar la persistencia de la batalla tras recargar la página.

### Fase 6 Mantenimiento del estado con sesiones

En esta fase dejé de pasar las variables de un lado a otro por la URL y pasé a usar `Flask-Session` para que la aplicación sea más robusta. Estos son los datos concretos que guardo en la sesión y el porqué:

* **`trainer`**: Sirve para saber quién está conectado. Si alguien intenta saltarse el inicio y entrar directamente a la arena de batalla escribiendo la ruta a mano, al no tener la sesión validada el servidor lo bloquea y lo manda fuera.
* **`starter_name`**: Al elegir a mi Pokémon, lo guardo aquí para que la URL de la batalla quede totalmente limpia. Así evito que los usuarios puedan hacer trampas modificando el nombre desde la barra de direcciones.
* **`rival_pokemon` y `user_moves`**: Esto es clave para la persistencia del combate. Los guardo en la sesión nada más generarse para que queden fijados. Si no lo hiciera, cada vez que el usuario pulsara F5 por error le cambiaría el oponente y los ataques. Estos datos solo se resetean (usando `session.pop()`) si el usuario vuelve al listado y decide pelear con un Pokémon distinto.

---

**Autor:** Abdullah Riaz