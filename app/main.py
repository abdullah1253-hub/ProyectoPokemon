import json
import random
from pathlib import Path
from flask import Flask, render_template, request, redirect, url_for, session
from flask_session import Session

app = Flask(__name__)

app.config["SESSION_TYPE"] = "filesystem"
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_FILE_DIR"] = "./.flask_session"
app.secret_key = "clave_super_secreta"

Session(app)


RUTA_DATOS = Path(__file__).resolve().parent.parent / "data" / "pokemons-competitive.json"

with RUTA_DATOS.open('r', encoding='utf-8') as f:
    pokemons_data = json.load(f)


## Index page home
@app.route('/', methods=['GET', 'POST'])
def index():
    proyecto = "Batallas Pokemon"
    nombre = "Abdullah"
    año = 2026
    error = None

    if request.method == 'POST':
        trainer = request.form.get('trainer', '').strip()

        if len(trainer) < 3 or len(trainer) > 15:
            error = "Trainer's name should be between 3 and 15 characters."
        else:
            session['trainer'] = trainer
            print("SESSION:", dict(session))
            return redirect(url_for('listado'))
        
    return render_template(
        'index.html',
        proyecto=proyecto,
        nombre=nombre,
        año=año
        error = error
    )

## List of pokemon
@app.route('/pokemons/', methods=['GET', 'POST'])
def listado():
    trainer = session.get('trainer')
    
    if not trainer:
        return redirect(url_for('index'))

    starter_error = None

    if request.method == 'POST':
        starter_name = request.form.get('starter_name', '').strip().lower()
        
        if not starter_name:
            starter_error = "Por favor, escribe el nombre de un Pokémon."
        else:
            starter_found = False
            for p in pokemons_data:
                if p['name'].lower() == starter_name:
                    starter_found = True
                    break
            
            if starter_found:
                session['starter_name'] = starter_name
                session.pop('rival_pokemon', None)
                session.pop('user_moves', None)
                return redirect(url_for('battle'))
            else:
                starter_error = "Este Pokémon no existe. Revisa el nombre."

    search_name = request.args.get('name', '').strip().lower()
    search_type = request.args.get('type', '').strip().lower()

    filtered_pokemons = []
    for p in pokemons_data:
        match_name = search_name in p['name'].lower()
        
        match_type = True
        if search_type:
            match_type = False
            for t in p.get('types', []):
                if search_type in t.lower():
                    match_type = True
                    break
        
        if match_name and match_type:
            filtered_pokemons.append(p)

    all_types = []
    for p in pokemons_data:
        for t in p.get('types', []):
            if t not in all_types:
                all_types.append(t)
    all_types.sort()

    return render_template(
        'listado.html',
        pokemons=filtered_pokemons,
        all_types=all_types,
        proyecto="Batallas Pokemon",
        trainer=trainer,
        starter_error=starter_error
    )

## Pokemon detail page
@app.route('/pokemons/<int:id>/')
def detalle(id):
    
    trainer = session.get('trainer')
    if not trainer:
        return redirect(url_for('index'))

    pokemon_encontrado = None
    for p in pokemons_data:
        if p.get('id') == id:
            pokemon_encontrado = p
            break
            
    if not pokemon_encontrado:
        return "Pokemon not found", 404
   
    return render_template('detalle.html', pokemon=pokemon_encontrado, proyecto="ProyectoPokemon", trainer=trainer)

## Battle page
@app.route('/battle')
def battle():
    trainer = session.get('trainer')
    starter_name = session.get('starter_name')

    if not trainer or not starter_name:
        return redirect(url_for('index'))

    user_pokemon = None
    for p in pokemons_data:
        if p['name'].lower() == starter_name.lower():
            user_pokemon = p
            break

    if not user_pokemon:
        return redirect(url_for('listado'))

    if 'rival_pokemon' in session and 'user_moves' in session:
        rival_pokemon = session['rival_pokemon']
        selected_moves = session['user_moves']
    else:
        rival_options = []
        for p in pokemons_data:
            if p['name'].lower() != starter_name.lower():
                rival_options.append(p)

        if rival_options:
            rival_pokemon = random.choice(rival_options)
        else:
            rival_pokemon = user_pokemon

        user_moves = user_pokemon.get('moves', [])
        if len(user_moves) >= 4:
            selected_moves = random.sample(user_moves, 4)
        else:
            selected_moves = user_moves
            
        session['rival_pokemon'] = rival_pokemon
        session['user_moves'] = selected_moves

    return render_template(
        'battle.html',
        trainer=trainer,
        user_pokemon=user_pokemon,
        rival_pokemon=rival_pokemon,
        user_moves=selected_moves,
        proyecto="Batallas Pokemon"
    )

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=8080)