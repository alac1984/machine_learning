import sqlite3
from sqlite3.dbapi2 import Connection
from typing import Optional

from dotenv import load_dotenv

from settings import Settings

SQL = """
    select
        m.match_api_id as match_id,
        m.season,
        m.date,
        m.home_team_api_id as home_id,
        ht.team_long_name as home_name,
        m.away_team_api_id as away_id,
        at.team_long_name as away_name,
        m.home_team_goal as home_goal,
        m.away_team_goal as away_goal,
        m.goal,
        m.shoton,
        m.shotoff,
        m.foulcommit,
        m.card,
        m.cross,
        m.corner,
        m.possession,
        htc.play_speed as home_play_speed,
        htc.play_dribbling as home_play_dribbling,
        htc.play_passing as home_play_passing,
        htc.chance_creation_passing as home_chance_passing,
        htc.chance_creation_crossing as home_chance_crossing,
        htc.chance_creation_shooting as home_chance_shooting,
        htc.defence_pressure as home_defence_pressure,
        htc.defence_aggression as home_defence_aggression,
        atc.play_speed as away_play_speed,
        atc.play_dribbling as away_play_dribbling,
        atc.play_passing as away_play_passing,
        atc.chance_creation_passing as away_chance_passing,
        atc.chance_creation_crossing as away_chance_crossing,
        atc.chance_creation_shooting as away_chance_shooting,
        atc.defence_pressure as away_defence_pressure,
        atc.defence_aggression as away_defence_aggression
    from match m
    inner join team ht on ht.team_api_id = m.home_team_api_id
    inner join team at on at.team_api_id = m.away_team_api_id
    inner join team_attributes_condensed htc on htc.team_api_id = m.home_team_api_id
    inner join team_attributes_condensed atc on atc.team_api_id = m.home_team_api_id
    where
        m.goal is not null and
        m.shoton is not null and
        m.shotoff is not null and
        m.foulcommit is not null and
        m.card is not null and
        m.cross is not null and
        m.corner is not null and
        m.possession is not null
    ;
"""

class SQLiteDB:

    def __init__(self, db_path):
            self.db_path = db_path

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_path)
        self.conn.row_factory = sqlite3.Row
        return self.conn

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            self.conn.rollback()
        else:
            self.conn.commit()
        self.conn.close()


def extract_data(settings: Settings, sql: str, **kwargs):
    with SQLiteDB("04_euro_soccer/" + settings.DB) as conn2:
        cur = conn2.cursor()

        conn = kwargs.get("conn")
        if conn:
            cur = kwargs["conn"].cursor()

        data = cur.execute(sql)
        return data.fetchall()


