from config import db
from sqlalchemy import text

from entities.citation import Article

def get_refrences():
    """ result = db.session.execute(text("SELECT id, content, done FROM todos"))
    todos = result.fetchall()
    return [Todo(todo[0], todo[1], todo[2]) for todo in todos]  """
    return None # I left the boilerplate commented for copy pasting but return a list of Refrence objects

def create_refrence(content):
    """ sql = text("INSERT INTO todos (content) VALUES (:content)")
    db.session.execute(sql, { "content": content })
    db.session.commit() """
    # I left the boilerplate commented for copy pasting but create refrence inside the database from content 
    # (containing data from the html form)
    