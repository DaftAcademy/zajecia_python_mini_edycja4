import sqlite3
from flask import Flask, g

DATABASE = 'first_db'

app = Flask(__name__)


#CREATE TABLE `simple_users` (
#	`username`	TEXT
#);

# zgapione z http://flask.pocoo.org/docs/0.12/patterns/sqlite3/
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = sqlite3.connect(DATABASE)
        g._database = db
    return db


# zgapione z http://flask.pocoo.org/docs/0.12/patterns/sqlite3/
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
       
        
#@app.route('/<new_user>')
#def insert_new_user(new_user):
#    db = get_db()
#    c = db.cursor()
#    c.execute("INSERT INTO users VALUES ('{}', 3)".format(new_user))
#    db.commit()
#    return 'inserted {}'.format(new_user)

    
@app.route('/<new_user>')
def insert_new_user(new_user):
    
    db = get_db()
    c = db.cursor()
    query = "INSERT INTO simple_users VALUES ('{}');".format(new_user)
    print('query = {}'.format(query))
    print('better_query = {}'.format(query))
    # execute jest "lepszy" - wykonuje tylko jeden 'SQL statement'
    # executescript użyty w celu zademonstrowania SQLinjection
    c.executescript(query)
    db.commit()
    return 'inserted {}'.format(new_user)
   
   
@app.route('/<new_user>')
def better_insert_new_user(new_user):
    # no SQLinjection
    db = get_db()
    c = db.cursor()
    better_query = "INSERT INTO simple_users VALUES (?);"
    c.execute(better_query, (new_user, ))
    db.commit()
    return 'inserted {}'.format(new_user)
    

if __name__ == "__main__":
    app.run()

