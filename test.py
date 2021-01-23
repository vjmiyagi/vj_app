from fastapi import FastAPI
import mysql.connector as mysql


db = mysql.connect(
    hostname="mysql.vjmiyagi.com",
    user="vjmiyagi",
    password="1386Waxedoff",
    database="vjm123"
)


print(db)

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello VJ"}
