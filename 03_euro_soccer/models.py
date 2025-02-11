from datetime import datetime
from enum import Enum
from pydantic import BaseModel


class Winner(Enum):
    HOME = 0
    AWAY = 1
    DRAW = 2


class Data(BaseModel):
    match_id: int
    date: datetime
    home_name: str
    away_name: str
    home_goal: int
    away_goal: int
    home_shoton: int
    away_shoton: int
    home_shotoff: int
    away_shotoff: int
    home_foulcommit: int
    away_foulcommit: int
    home_ycard: int
    away_ycard: int
    home_rcard: int
    away_rcard: int
    home_cross: int
    away_cross: int
    home_corner: int
    away_corner: int
    home_posession: float
    away_posession: float
    winner: Winner
