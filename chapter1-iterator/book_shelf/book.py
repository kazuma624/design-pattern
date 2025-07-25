from dataclasses import dataclass

@dataclass
class Book:
    name: str

    def get_name(self):
        return self.name
