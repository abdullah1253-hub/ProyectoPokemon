import json
import random
from pathlib import Path


class PokemonRepository:
    def __init__(self):
        self.file_path = Path(__file__).resolve().parent.parent.parent / "data" / "pokemons-competitive.json"

    def get_all(self) -> dict:
        if not self.file_path.exists():
            return []
        else:
            with self.file_path.open('r', encoding= 'utf-8') as f:
                return json.load(f)





def load_pokemons():
    if not RUTA_DATOS.exists():
        return []
    with RUTA_DATOS.open('r', encoding='utf-8') as f:
        return json.load(f)

_pokemons_cache = load_pokemons()