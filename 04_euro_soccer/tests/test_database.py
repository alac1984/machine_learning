import pytest
from database import extract_data
from settings import Settings


def test_sqlitedb(testdb):
    cur = testdb.cursor()

    cur.execute("select * from test")
    rows = cur.fetchall()
    assert rows[0]["id"] == 1
    assert rows[0]["name"] == "Andre"
    assert rows[1]["id"] == 2
    assert rows[1]["name"] == "Monalise"


def test_extract_data(testdb):
    settings = Settings("test")
    cur = testdb.cursor()
    sql = "select * from test"
    data = extract_data(settings, sql, conn=testdb)

    assert data[0]["id"] == 1
    assert data[0]["name"] == "Andre"
    assert data[1]["id"] == 2
    assert data[1]["name"] == "Monalise"
