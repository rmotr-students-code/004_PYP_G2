"""
Requirements:
 * A database created with some data about authors inside.
"""
import sqlite3
from flask import Flask, g, render_template
from . import config

app = Flask(__name__)


def connect_db():
    return sqlite3.connect(config.DATABASE_NAME)


@app.before_request
def before_request():
    g.db = connect_db()


@app.route('/')
def hello_world():
    cursor = g.db.execute('SELECT id, name, country_id FROM author;')
    authors = [dict(id=row[0], name=row[1], country=row[2]) for row in cursor.fetchall()]
    user = None

    return render_template('authors_with_conditional.html',
        authors=authors, user=user)
