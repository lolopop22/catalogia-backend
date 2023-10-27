import dataclasses


@dataclasses.dataclass
class Film:
    poster: str
    title: str
    runtime: int
    directors: list
    producers: list
    cast: list
    synopsis: str

    @classmethod
    def from_dict(cls, f):
        return cls(**f)
    
    def to_dict(self):
        return dataclasses.asdict(self)

