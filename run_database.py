from db_connection import connect
from pathlib import Path

cur = connect.cursor()
filePath = Path("database.sql")

try:
    with open(filePath,"r") as fileReader:
        cur.execute(fileReader.read())
        connect.commit()
        print("SuccessFully!")
except Exception as e:
    print(f"Error: {e}")
    connect.rollback()      

connect.close()
cur.close()