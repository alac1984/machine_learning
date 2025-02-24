from datetime import datetime
from typing import Optional
from enum import Enum
from pydantic import BaseModel


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
    home_possession: float
    away_possession: float
    home_play_speed: float
    home_play_dribbling: float
    home_play_passing: float
    home_chance_passing: float
    home_chance_crossing: float
    home_chance_shooting: float
    home_defence_pressure: float
    home_defence_aggression: float
    away_play_speed: float
    away_play_dribbling: float
    away_play_passing: float
    away_chance_passing: float
    away_chance_crossing: float
    away_chance_shooting: float
    away_defence_pressure: float
    away_defence_aggression: float 
