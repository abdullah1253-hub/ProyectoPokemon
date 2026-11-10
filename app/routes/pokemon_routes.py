import random
from flask import Blueprint, render_template, request, redirect, url_for, session
from app.services import pokemon_service

pokemon_bp = Blueprint('pokemon', __name__)

@pokemon_bp.route('/pokemons/', methods=['GET', 'POST'])
def listado():
    trainer = session.get('trainer')
    if not trainer:
        return redirect(url_for('auth.index'))
        
    starter_error = None

    if request.method == 'POST':
        starter_name = request.form.get('starter_name', '').strip().lower()
        found_pokemon = pokemon_service.get_pokemon_by_name(starter_name)
        
        if found_pokemon:
            session['starter_name'] = starter_name
            session.pop('rival_pokemon', None)
            session.pop('user_moves', None)
            return redirect(url_for('pokemon.battle'))
        else:
            starter_error = "Este Pokémon no existe. Revisa el nombre."

    search_name = request.args.get('name', '').strip().lower()
    search_type = request.args.get('type', '').strip().lower()

    filtered = pokemon_service.filter_pokemons(search_name, search_type)
    all_types = pokemon_service.get_all_types()

    return render_template(
        'listado.html',
        pokemons=filtered,
        all_types=all_types,
        proyecto="Batallas Pokemon",
        trainer=trainer,
        starter_error=starter_error
    )

@pokemon_bp.route('/pokemons/<int:id>/')
def detalle(id):
    trainer = session.get('trainer')
    if not trainer:
        return redirect(url_for('auth.index'))
        
    pokemon = pokemon_service.get_pokemon_by_id(id)
    if not pokemon:
        return "Pokemon not found", 404

    return render_template('detalle.html', pokemon=pokemon, proyecto="ProyectoPokemon", trainer=trainer)

@pokemon_bp.route('/battle')
def battle():
    trainer = session.get('trainer')
    if not trainer:
        return redirect(url_for('auth.index'))
        
    starter_name = session.get('starter_name')
    if not starter_name:
        return redirect(url_for('pokemon.listado'))

    user_pokemon = pokemon_service.get_pokemon_by_name(starter_name)
    if not user_pokemon:
        return redirect(url_for('pokemon.listado'))

    if 'rival_pokemon' in session and 'user_moves' in session:
        rival_pokemon = session['rival_pokemon']
        selected_moves = session['user_moves']
    else:
        rival_pokemon = pokemon_service.get_random_rival(starter_name)
        
        moves = user_pokemon.get('moves', [])
        selected_moves = random.sample(moves, 4) if len(moves) >= 4 else moves
            
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