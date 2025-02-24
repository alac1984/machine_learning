from database import SQLiteDB

import sqlite3
import pytest


@pytest.fixture(scope="function")
def testdb():
    with SQLiteDB(":memory:") as conn:
        cur = conn.cursor()
        cur.execute("""
            create table test(
                id int,
                name varchar(10)
            );
        """)

        cur.execute("""
            insert into test(id, name) values
            (1, "Andre"), (2, "Monalise");
        """)

        yield conn
