import os
from dataclasses import dataclass

from flask import Flask, render_template, send_from_directory


@dataclass()
class Todo:
    id: int
    description: str


todos = [Todo(1, "Bread"), Todo(2, "Milk")]

app = Flask(__name__)


@app.route("/favicon.ico")
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, "static/images"),
        "favicon.ico",
        mimetype="image/vnd.microsoft.icon",
    )


@app.get("/")
def index():
    return render_template("index.html", todos=todos)


def start(debug=False):
    app.run(debug=debug)


if __name__ == "__main__":
    start(debug=True)
