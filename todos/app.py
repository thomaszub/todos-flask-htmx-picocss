import os
import sqlite3
from contextlib import closing

from flask import Flask, g, render_template, send_from_directory

from todos.todo import Todo

DATABASE = "todos.db"

app = Flask(__name__)


def init_db():
    with closing(sqlite3.connect(DATABASE)) as conn:
        with closing(conn.cursor()) as cur:
            cur.execute(
                "CREATE TABLE IF NOT EXISTS todos (id INTEGER PRIMARY KEY AUTOINCREMENT, description TEXT);"
            )


def get_connection():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


@app.teardown_appcontext
def close_db(_):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()


@app.get("/favicon.ico")
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, "static/images"),
        "favicon.ico",
        mimetype="image/vnd.microsoft.icon",
    )


@app.get("/")
def index():
    todos = []
    with closing(get_connection()) as conn:
        with closing(conn.cursor()) as cur:
            res = cur.execute("SELECT id, description FROM todos")
            todos = [Todo(row[0], row[1]) for row in res.fetchall()]
    return render_template("index.html", todos=todos)


def start(debug=False):
    app.run(debug=debug)


if __name__ == "__main__":
    init_db()
    start(debug=True)
