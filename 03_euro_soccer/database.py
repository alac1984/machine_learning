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
        at.team_long_name as home_name,
        m.home_team_goal as home_goal,
        m.away_team_goal as away_goal,
        m.goal,
        m.shoton,
        m.shotoff,
        m.foulcommit,
        m.card,
        m.cross,
        m.corner,
        m.possession
    from match m
    inner join team ht on ht.team_api_id = m.home_team_api_id
    inner join team at on at.team_api_id = m.away_team_api_id
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
        return self.conn

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            self.conn.rollback()
        else:
            self.conn.commit()
        self.conn.close()


def extract_data(settings: Settings, sql: str, conn: Optional[Connection]):
    with SQLiteDB(settings.DB) as conn2:
        cur = conn2.cursor()

        if conn:
            cur = conn.cursor()

        data = cur.execute(sql)
        return data.fetchall()


