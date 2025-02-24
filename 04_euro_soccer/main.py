from settings import Settings
from database import extract_data, SQL
from models import Data, create_data_object


if __name__ == "__main__":
    # Extract data
    settings = Settings("development")
    db_data = extract_data(settings, SQL)

    # Check if data follows the constraints and create dict
    data_objs = []
    for d in db_data:
        data_obj = create_data_object(d)
        data_objs.append(data_obj)

    print(data_objs[0])
