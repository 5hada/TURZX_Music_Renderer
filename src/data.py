from dataclasses import dataclass
from enum import Enum


class Player(Enum):
    AppleMusic = 0
    Chrome = 1
    Youtube = 2
    ITunes = 3
    Spotify = 4


@dataclass
class PointRect:
    p1: tuple[int, int]
    p2: tuple[int, int]

    @property
    def left(self):
        return self.p1[0]

    @property
    def right(self):
        return self.p2[0]

    @property
    def top(self):
        return self.p1[1]

    @property
    def bottom(self):
        return self.p2[1]

    @property
    def rect(self):
        return Rect(self.left, self.top, self.right-self.left, self.bottom-self.top)

@dataclass
class Rect:
    x: int
    y: int
    w: int
    h: int

    @property
    def left(self):
        return self.x

    @property
    def right(self):
        return self.x + self.w

    @property
    def top(self):
        return self.y

    @property
    def bottom(self):
        return self.y + self.h

    def __ge__(self, other) -> bool:
        return self.left <= other.left and self.top <= other.top and self.right >= other.right and self.bottom >= other.bottom


@dataclass
class Layout:
    thumb: Rect
    title: Rect
    detail: Rect
    progress: Rect
    timestamp: Rect
    totaTime: Rect
    background: list[Rect]


@dataclass
class PlayData:
    player: Player
    name: str
    artist: str
    duration: str
