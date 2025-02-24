from datetime import datetime
from typing import Optional
from enum import Enum
from pydantic import BaseModel
from xml import (
    determine_winner,
    get_shoton,
    get_shotoff,
    get_foulcommit,
    get_ycard,
    get_rcard,
    get_cross,
    get_corner,
    get_possession
)

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
    home_winner: bool
    away_winner: bool
    draw: bool


def create_data_object(d: dict) -> Data:
    return Data(
        match_id=d["match_id"],
        date=d["date"],
        home_name=d["home_name"],
        away_name=d["away_name"],
        home_goal=d["home_goal"],
        away_goal=d["away_goal"],
        home_shoton=get_shoton(d["shoton"]),
        away_shoton=get_shoton(d["shoton"]),
        home_shotoff=get_shotoff(d["shotoff"]),
        away_shotoff=get_shotoff(d["shotoff"]),
        home_foulcommit=get_foulcommit(d["foulcommit"]),
        away_foulcommit=get_foulcommit(d["foulcommit"]),
        home_ycard=get_ycard(d["card"]),
        away_ycard=get_ycard(d["card"]),
        home_rcard=get_rcard(d["card"]),
        away_rcard=get_rcard(d["card"]),
        home_cross=get_cross(d["cross"]),
        away_cross=get_cross(d["cross"]),
        home_corner=get_corner(d["corner"]),
        away_corner=get_corner(d["corner"]),
        home_possession=get_possession(d["possession"]),
        away_possession=get_possession(d["possession"]),
        home_play_speed=d["home_play_speed"],
        home_play_dribbling=d["home_play_dribbling"],
        home_play_passing=d["home_play_passing"],
        home_chance_passing=d["home_chance_passing"],
        home_chance_crossing=d["home_chance_crossing"],
        home_chance_shooting=d["home_chance_shooting"],
        home_defence_pressure=d["home_defence_pressure"],
        home_defence_aggression=d["home_defence_agression"],
        away_play_speed=d["away_play_speed"],
        away_play_dribbling=d["away_play_dribbling"],
        away_play_passing=d["away_play_passing"],
        away_chance_passing=d["away_chance_passing"],
        away_chance_crossing=d["away_chance_crossing"],
        away_chance_shooting=d["away_chance_shooting"],
        away_defence_pressure=d["away_defence_pressure"],
        away_defence_aggression=d["away_defence_aggression"],
        home_winner=True if d["home_goal"] > d["away_goal"] else False,
        away_winner=True if d["away_goal"] > d["home_goal"] else False,
        draw=True if d["away_goal"] == d["home_goal"] else False,
    )
