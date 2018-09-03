from app import app
from db import db


@app.before_first_request # execute the following function before the first request
def create_tables():
    db.create_all()

db.init_app(app)
app.run()
