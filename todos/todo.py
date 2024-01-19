from dataclasses import dataclass


@dataclass()
class Todo:
    id: int
    description: str
