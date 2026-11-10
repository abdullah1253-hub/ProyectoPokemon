import json
import random
from pathlib import Path

RUTA_DATOS = Path(__file__).resolve().parent.parent.parent / "data" / "pokemons-competitive.json"

def load_pokemons():
    if not RUTA_DATOS.exists():
        return []
    with RUTA_DATOS.open('r', encoding='utf-8') as f:
        return json.load(f)

_pokemons_cache = load_pokemons()

def get_all_pokemons():
    return _pokemons_cache

def get_pokemon_by_id(pokemon_id: int):
    for p in _pokemons_cache:
        if p.get('id') == pokemon_id:
            return p
    return None

def get_pokemon_by_name(name: str):
    if not name:
        return None
    search_term = name.strip().lower()
    for p in _pokemons_cache:
        if p.get('name', '').lower() == search_term:
            return p
    return None

def filter_pokemons(name: str = "", type_: str = ""):
    search_name = name.strip().lower()
    search_type = type_.strip().lower()
    filtered = []
    
    for p in _pokemons_cache:
        match_name = search_name in p.get('name', '').lower()
        match_type = True
        
        if search_type:
            types = [t.lower() for t in p.get('types', [])]
            match_type = any(search_type in t for t in types)
            
        if match_name and match_type:
            filtered.append(p)
            
    return filtered

def get_all_types():
    types_set = set()
    for p in _pokemons_cache:
        for t in p.get('types', []):
            types_set.add(t)
    return sorted(list(types_set))

def get_random_rival(starter_name: str):
    rival_options = [p for p in _pokemons_cache if p.get('name', '').lower() != starter_name.strip().lower()]
    if rival_options:
        return random.choice(rival_options)
    return get_pokemon_by_name(starter_name)