from dataclasses import dataclass, field


@dataclass
class Pokemon:
    id: int
    name: str
    types: list[str]
    stats: list[dict]
    moves: list[dict]
    sprites: dict = field(default_factory=dict)
    height: int = 0
    weight: int = 0
    max_hp: int | None = None

    def __post_init__(self):
        if self.max_hp is None:
            base_hp = self.get_stat("hp")
            self.max_hp = base_hp * 3 if base_hp > 0 else 100

    def get_stat(self, stat_name: str) -> int:
        for stat in self.stats:
            if stat.get("name") == stat_name:
                return stat.get("value", 0)
        return 0

    def get_move(self, move_name: str) -> dict | None:
        if not move_name:
            return None
        target = move_name.strip().lower()
        for move in self.moves:
            if move.get("name", "").lower() == target:
                return move
        return None

    @classmethod
    def from_dict(cls, data: dict) -> "Pokemon":
        return cls(
            id=data["id"],
            name=data["name"],
            types=data.get("types", []),
            stats=data.get("stats", []),
            moves=data.get("moves", []),
            sprites=data.get("sprites", {}),
            height=data.get("height", 0),
            weight=data.get("weight", 0),
            max_hp=data.get("max_hp"),
        )

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "types": self.types,
            "stats": self.stats,
            "moves": self.moves,
            "sprites": self.sprites,
            "max_hp": self.max_hp,
        }