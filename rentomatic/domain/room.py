import uuid
import dataclasses

@dataclasses.dataclass
class Room:
    code: uuid.UUID
    size: int
    price: int
    longitude: float
    latitude: float

    @classmethod
    def from_dict(self, dictionary):
        return self(**dictionary)

    def to_dict(self):
        return dataclasses.asdict(self)