import sqlite3
from sqlite3 import Error
from secure_data import DB_PATH


def create_db(db_file):
    db = None
    try:
        db = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return db


def create_table(db):
    c = db.cursor()
    sql = """ CREATE TABLE IF NOT EXISTS images (
                id integer PRIMARY KEY,
                img_id text NOT NULL,
                owner text NOT NULL,
                server text NOT NULL,
            ); """
    c.execute(sql)


def insert(db, img_id: str, owner: str, server: str):

    sql = f'''INSERT INTO images(img_id,owner,server)
              VALUES({img_id}, {owner}, {server}) '''
    c = db.cursor()
    c.execute(sql)
    db.commit()

    return c.lastrowid


images_db = create_db(DB_PATH)
create_table(images_db)

