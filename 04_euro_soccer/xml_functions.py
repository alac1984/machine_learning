from bs4 import BeautifulSoup as Soup


def get_shots(team_id: int, xml_str: str) -> int:
    soup = Soup(xml_str, 'lxml')
    values = soup.find_all('value')
    shots = 0
    for value in values:
        if int(value.team.text) == team_id:  # type: ignore
            shots += 1

    return shots


def get_foulcommit():
    ...

def get_ycard():
    ...

def get_rcard():
    ...

def get_cross():
    ...

def get_corner():
    ...

def get_possession():
    ...
