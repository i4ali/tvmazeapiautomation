import sqlite3
import pytest

DATABASE = "./test_db"

@pytest.fixture
def clean_numbers_table():
    db = sqlite3.connect(DATABASE)
    with db:
        try:
            db.execute("DELETE FROM numbers_table")
        except:
            print("unable to delete records from number_table")