import json
from pathlib import Path
from flask import Flask, render_template

app = Flask(__name__)

RUTA_DATOS = Path(__file__).resolve().parent.parent / "data" / "pokemons-competitive.json"

with RUTA_DATOS.open('r', encoding='utf-8') as f:
    pokemons_data = json.load(f)

## Index page home
@app.route('/')
def index():
    proyecto = "Batallas Pokemon"
    nombre = "Abdullah"
    año = 2026
    
    return render_template(
        'index.html',
        proyecto=proyecto,
        nombre=nombre,
        año=año
    )
## List of pokemon
@app.route('/pokemons/')
def listado():
    return render_template('listado.html', pokemons=pokemons_data)



## Details of pokemon
@app.route('/pokemons/<int:id>/')
def detalle(id):
    pokemon_encontrado = None
    for p in pokemons_data:
        if p.get('id') == id:
            pokemon_encontrado = p
            break
            
    if not pokemon_encontrado:
        return "Pokémon no encontrado", 404

    weight = pokemon_encontrado.get('weight', 0)

    if weight < 500:
        categoria_peso = "Ligero"
    elif weight <= 1500:
        categoria_peso = "Normal"
    else:
        categoria_peso = "Pesado"

    return render_template('detalle.html', pokemon=pokemon_encontrado, categoria_peso=categoria_peso)

if __name__ == '__main__':
    app.run(debug=True, port=8080)