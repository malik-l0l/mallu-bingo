
from flask import Flask, render_template, redirect, url_for, request, session
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from bingo import *  
import os

# Ensure the /tmp/flask_instance directory exists
os.makedirs('/tmp/flask_instance', exist_ok=True)

app = Flask(__name__, instance_path='/tmp/flask_instance')
app.config["SECRET_KEY"] = "iamchatgpthahaha"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/flask_instance/db.sqlite3"
app.config["SESSION_TYPE"] = 'sqlalchemy'


db = SQLAlchemy(app)
app.config["SESSION_SQLALCHEMY"] = db

# Initialize the session extension
Session(app)

# Initialize game state
def init_game():
    return {
        'computer_b': create_board(),
        'player_b': create_board(),
        'computer_n': None,
        'player_n': None,
        'player_numbers': [],  # track player numbers
        'available_numbers': set(range(1, 26)),  # track computer numbers
        'count_p': 0,
        'count_c': 0,
        'winner': None,
        'show_computer': None
    }

@app.route("/", methods=["GET", "POST"])
def first():
    if 'game_state' not in session:
        session['game_state'] = init_game()

    return render_template("home.html")

@app.route("/play", methods=["POST", "GET"])
def play():
    game_state = session.get('game_state', init_game())

    if request.method == "POST":
        game_state["show_computer"] = True if request.form.get("computer-play") == "on" else None
        session['game_state'] = game_state

    if game_state["winner"] is not None:
        return redirect(url_for('won'))

    return render_template(
        "play.html",
        player_b=game_state['player_b'],
        computer_b=game_state['computer_b'] if game_state["show_computer"] else None,
        count_c=game_state["count_c"],
        count_p=game_state["count_p"],
        player_n=game_state["player_n"],
        computer_n=game_state["computer_n"]
    )

@app.route("/mark/<int:player_n>")
def mark(player_n):
    game_state = session.get('game_state', init_game())

    if game_state["winner"] is not None:
        return redirect(url_for('won'))

    if player_n not in game_state['player_numbers']:
        find_key_mark(game_state['player_b'], game_state['computer_b'], player_n)
        game_state["player_n"] = player_n
        game_state['player_numbers'].append(player_n)

        game_state["count_p"] = check_bingo(game_state['player_b'])
        game_state["count_c"] = check_bingo(game_state['computer_b'])

        if game_state["count_p"] >= 5:
            game_state["winner"] = 1
            session['game_state'] = game_state
            return redirect(url_for("won"))

        if game_state["count_c"] >= 5:
            game_state["winner"] = 0
            session['game_state'] = game_state
            return redirect(url_for("won"))

        computer_n = ask_computer(game_state['computer_b'])
        game_state['available_numbers'].remove(computer_n)
        game_state["computer_n"] = computer_n

        find_key_mark(game_state['computer_b'], game_state['player_b'], computer_n)

        game_state["count_c"] = check_bingo(game_state['computer_b'])
        game_state["count_p"] = check_bingo(game_state['player_b'])

        if game_state["count_c"] >= 5:
            game_state["winner"] = 0
            session['game_state'] = game_state
            return redirect(url_for("won"))

        if game_state["count_p"] >= 5:
            game_state["winner"] = 1
            session['game_state'] = game_state
            return redirect(url_for("won"))

        session['game_state'] = game_state
        return redirect(url_for('play'))
    else:
        return redirect(url_for('play'))

@app.route("/won", methods=["POST", "GET"])
def won():
    game_state = session.get('game_state', init_game())

    if game_state["winner"] == 1:
        winner = "Player"
    elif game_state["winner"] == 0:
        winner = "Computer"
    else:
        return redirect(url_for('play'))

    return render_template(
        "won.html",
        candidate=winner,
        player_b=game_state['player_b'],
        computer_b=game_state['computer_b'],
        count_c=game_state["count_c"],
        count_p=game_state["count_p"],
    )

@app.route("/play-again", methods=["GET", "POST"])
def play_again():
    if request.method == "POST":
        game_state = init_game()
        game_state["show_computer"] = True if request.form.get("computer-play") == "on" else None
        session['game_state'] = game_state

    return redirect(url_for('play'))

@app.after_request
def add_header(response):
    response.cache_control.no_store = True
    response.cache_control.no_cache = True
    response.cache_control.must_revalidate = True
    response.cache_control.max_age = 0
    return response

if __name__ == "__main__":
    app.run()


#4
"""
from flask import Flask, render_template, redirect, url_for, request, session
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from bingo import *   

app = Flask(__name__)
app.config["SECRET_KEY"] = "iamchatgpt"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
app.config["SESSION_TYPE"] = 'sqlalchemy'
db = SQLAlchemy(app)
app.config["SESSION_SQLALCHEMY"] = db

# Initialize the session extension
Session(app)

# Initialize game state
def init_game():
    return {
        'computer_b': create_board(),
        'player_b': create_board(),
        'computer_n': None,
        'player_n': None,
        'player_numbers': [],  # track player numbers
        'available_numbers': set(range(1, 26)),  # track computer numbers
        'count_p': 0,
        'count_c': 0,
        'winner': None,
        'show_computer': None
    }

@app.route("/", methods=["GET", "POST"])
def first():
    if 'game_state' not in session:
        session['game_state'] = init_game()

    return render_template("home.html")


@app.route("/play", methods=["POST", "GET"])
def play():
    game_state = session.get('game_state', init_game())

    if request.method == "POST":
        game_state["show_computer"] = True if request.form.get("computer-play") == "on" else None
        session['game_state'] = game_state

    if game_state["winner"] is not None:
        return redirect(url_for('won'))

    return render_template(
        "play.html",
        player_b=game_state['player_b'],
        computer_b=game_state['computer_b'] if game_state["show_computer"] else None,
        count_c=game_state["count_c"],
        count_p=game_state["count_p"],
        player_n=game_state["player_n"],
        computer_n=game_state["computer_n"]
    )


@app.route("/mark/<int:player_n>")
def mark(player_n):
    game_state = session.get('game_state', init_game())

    if game_state["winner"] is not None:
        return redirect(url_for('won'))

    if player_n not in game_state['player_numbers']:
        find_key_mark(game_state['player_b'], game_state['computer_b'], player_n)
        game_state["player_n"] = player_n
        game_state['player_numbers'].append(player_n)

        game_state["count_p"] = check_bingo(game_state['player_b'])
        game_state["count_c"] = check_bingo(game_state['computer_b'])

        if game_state["count_p"] >= 5:
            game_state["winner"] = 1
            session['game_state'] = game_state
            return redirect(url_for("won"))

        if game_state["count_c"] >= 5:
            game_state["winner"] = 0
            session['game_state'] = game_state
            return redirect(url_for("won"))

        computer_n = ask_computer(game_state['computer_b'])
        game_state['available_numbers'].remove(computer_n)
        game_state["computer_n"] = computer_n

        find_key_mark(game_state['computer_b'], game_state['player_b'], computer_n)

        game_state["count_c"] = check_bingo(game_state['computer_b'])
        game_state["count_p"] = check_bingo(game_state['player_b'])

        if game_state["count_c"] >= 5:
            game_state["winner"] = 0
            session['game_state'] = game_state
            return redirect(url_for("won"))

        if game_state["count_p"] >= 5:
            game_state["winner"] = 1
            session['game_state'] = game_state
            return redirect(url_for("won"))

        session['game_state'] = game_state
        return redirect(url_for('play'))
    else:
        return redirect(url_for('play'))


@app.route("/won", methods=["POST", "GET"])
def won():
    game_state = session.get('game_state', init_game())

    if game_state["winner"] == 1:
        winner = "Player"
    elif game_state["winner"] == 0:
        winner = "Computer"
    else:
        return redirect(url_for('play'))

    return render_template(
        "won.html",
        candidate=winner,
        player_b=game_state['player_b'],
        computer_b=game_state['computer_b'],
        count_c=game_state["count_c"],
        count_p=game_state["count_p"],
    )


@app.route("/play-again", methods=["GET", "POST"])
def play_again():
    if request.method == "POST":
        game_state = init_game()
        game_state["show_computer"] = True if request.form.get("computer-play") == "on" else None
        session['game_state'] = game_state

    return redirect(url_for('play'))


@app.after_request
def add_header(response):
    response.cache_control.no_store = True
    response.cache_control.no_cache = True
    response.cache_control.must_revalidate = True
    response.cache_control.max_age = 0
    return response

if __name__ == "__main__":
    app.run()
"""


#3
"""
from flask import Flask, render_template, redirect, url_for, request
from bingo import *

app = Flask(__name__)

# Initialize game state
def init_game():
    return {
        'computer_b': create_board(),
        'player_b': create_board(),

        'computer_n': None,
        'player_n': None,

        'player_numbers': [], #track player numbers
        'available_numbers': set(range(1, 26)),  # track computer numbers
        
        'count_p':0,
        'count_c':0,

        'winner':None,

        'show_computer':None
    }

game_state = init_game()

@app.route("/", methods=["GET","POST"])
def first():

    return render_template(
        "home.html",
    )



@app.route("/play", methods=["POST", "GET"])
def play():

    if request.method == "POST":
        game_state["show_computer"] = True if request.form.get("computer-play") == "on" else None

    if game_state["winner"] is not None:
        return redirect(url_for('won'))
    return render_template(
        "play.html",
        player_b=game_state['player_b'],
        computer_b=game_state['computer_b'] if game_state["show_computer"] else None,
        count_c=game_state["count_c"],
        count_p=game_state["count_p"],
        player_n=game_state["player_n"],
        computer_n=game_state["computer_n"]
    )


    
@app.route("/mark/<int:player_n>")
def mark(player_n):
    if game_state["winner"] is not None:
        return redirect(url_for('won'))

    if player_n not in game_state['player_numbers']:
        find_key_mark(game_state['player_b'], game_state['computer_b'], player_n)

        game_state["player_n"] = player_n
        game_state['player_numbers'].append(player_n)
        
        game_state["count_p"] = check_bingo(game_state['player_b'])
        game_state["count_c"] = check_bingo(game_state['computer_b'])

        if game_state["count_p"] >= 5:
            game_state["winner"] = 1
            return redirect(url_for("won"))

        if game_state["count_c"] >= 5:
            game_state["winner"] = 0
            return redirect(url_for("won"))

        computer_n = ask_computer(game_state['computer_b'])
        game_state['available_numbers'].remove(computer_n)
        game_state["computer_n"] = computer_n

        find_key_mark(game_state['computer_b'], game_state['player_b'], computer_n)

        game_state["count_c"] = check_bingo(game_state['computer_b'])
        game_state["count_p"] = check_bingo(game_state['player_b'])

        if game_state["count_c"] >= 5:
            game_state["winner"] = 0
            return redirect(url_for("won"))

        if game_state["count_p"] >= 5:
            game_state["winner"] = 1
            return redirect(url_for("won"))

        # Redirect to the home page after processing
        return redirect(url_for('play'))
    else:
        # Handle case where player number is already marked
        return redirect(url_for('play'))


@app.route("/won", methods=["POST", "GET"])
def won():
    if game_state["winner"] == 1:
        winner = "Player"
    elif game_state["winner"] == 0:
        winner = "Computer"
    else:
        return redirect(url_for('play'))

    return render_template(
        "won.html",
        candidate=winner,
        player_b=game_state['player_b'],
        computer_b=game_state['computer_b'],
        count_c=game_state["count_c"],
        count_p=game_state["count_p"],
    )


@app.route("/play-again", methods=["GET","POST"])
def play_again():
    # reset the game state and go to index.html
    global game_state
    game_state = init_game()

    if request.method == "POST":
        game_state["show_computer"] = True if request.form.get("computer-play") == "on" else None

    return redirect(url_for('play'))

@app.after_request
def add_header(response):
    response.cache_control.no_store = True
    response.cache_control.no_cache = True
    response.cache_control.must_revalidate = True
    response.cache_control.max_age = 0
    return response

if __name__ == "__main__":
    app.run()

"""

#1
"""
1

from flask import Flask, render_template,redirect,request
from bingo import *


app = Flask(__name__)

global computer_b
global player_b

global player_numbers 

player_numbers = []




computer_b = create_board()
player_b = create_board()

SHOW_COMPUTER : bool = True


@app.route("/",methods=["POST","GET"])
def home():
    return render_template("index.html",
                            player_b = player_b,
                            computer_b=computer_b if SHOW_COMPUTER else None,
                            count_c=None,
                            count_p=None,
                            player_n=None,
                            computer_n=None
                            
                            )


@app.route("/mark/<int:player_n>")
def mark(player_n):

    if player_n not in player_numbers:

        find_key_mark(player_b,computer_b,player_n)
        player_numbers.append(player_n)
        print(player_numbers)
            
        count_p = check_bingo(player_b)
        count_c = check_bingo(computer_b)

        if count_p >= 5:
            return "<h2> PLAYER WON </h2>"

        if count_c >= 5:
            return "<h2> COMPUTER WON </h2>"

        computer_n = ask_computer(computer_b)
        available.remove(computer_n)

        find_key_mark(computer_b, player_b, computer_n)

        count_c = check_bingo(computer_b)
        count_p = check_bingo(player_b)

        if count_c >= 5:
            return "<h2> COMPUTER WON </h2>"

        if count_p >= 5:
            return "<h2> PLAYER WON </h2>"

        return render_template("index.html",
        player_b = player_b,
        computer_b=computer_b if SHOW_COMPUTER else None,
        count_p=count_p,
        count_c=count_c,
        player_n=player_n,
        computer_n=computer_n 
        )
    else: 
        #computer mark the number when reload happpens problem solve
        return render_template("index.html",
        player_b = player_b,
        computer_b=computer_b if SHOW_COMPUTER else None,
        count_p=None,
        count_c=None,
        player_n=None,
        computer_n=None 
        )
if __name__ == "__main__":
    app.run(debug=True)

"""

#2
"""


from flask import Flask, render_template, redirect, url_for, request
from bingo import *

app = Flask(__name__)

# Initialize game state
SHOW_COMPUTER = True

def init_game():
    return {
        'computer_b': create_board(),
        'player_b': create_board(),

        'computer_n': None,
        'player_n': None,

        'player_numbers': [], #track player numbers
        'available_numbers': set(range(1, 26)),  # track computer numbers
        
        'count_p':0,
        'count_c':0,

        'winner':None

    }

game_state = init_game()

@app.route("/", methods=["GET"])
def first():
    return render_template(
        "home.html",
    )

@app.route("/play-again", methods=["GET"])
def play_again():
    # reset the game state and goto index.html
    pass


@app.route("/play", methods=["POST", "GET"])
def home():
    return render_template(
        "index.html",
        player_b=game_state['player_b'],
        computer_b=game_state['computer_b'] if SHOW_COMPUTER else None,
        count_c=game_state["count_c"],
        count_p=game_state["count_p"],
        player_n=game_state["player_n"],
        computer_n=game_state["computer_n"]
    )


@app.route("/won", methods=["POST", "GET"])
def won():
    if game_state["winner"]==1:
        winner = "Player"
    if game_state["winner"]==0:
        winner = "Computer"

    return render_template(
        "won.html",
        candidate=winner
    )
    

@app.route("/mark/<int:player_n>")
def mark(player_n):
    
    if player_n not in game_state['player_numbers']:

        find_key_mark(game_state['player_b'], game_state['computer_b'], player_n)

        game_state["player_n"] = player_n

        game_state['player_numbers'].append(player_n)
        
        game_state["count_p"] = check_bingo(game_state['player_b'])
        game_state["count_c"] = check_bingo(game_state['computer_b'])

        if game_state["count_p"] >= 5:
            # return render_template("won.html",candidate="Player")
            game_state["winner"] = 1
            return redirect(url_for("won"))

        if game_state["count_c"] >= 5:
            # return render_template("won.html",candidate="Computer")
            game_state["winner"] = 0
            return redirect(url_for("won"))


        computer_n = ask_computer(game_state['computer_b'])
        game_state['available_numbers'].remove(computer_n)
        game_state["computer_n"] = computer_n

        find_key_mark(game_state['computer_b'], game_state['player_b'], computer_n)

        game_state["count_c"] = check_bingo(game_state['computer_b'])
        game_state["count_p"] = check_bingo(game_state['player_b'])


        if game_state["count_c"] >= 5:
            # return render_template("won.html",candidate="Computer")
            game_state["winner"] = 0
            return redirect(url_for("won"))

        if game_state["count_p"] >= 5:
            # return render_template("won.html",candidate="Player")
            game_state["winner"] = 1
            return redirect(url_for("won"))


        # Redirect to the home page after processing
        return redirect(url_for('home'))
    else:
        # Handle case where player number is already marked
        return redirect(url_for('home'))

@app.after_request
def add_header(response):
    response.cache_control.no_store = True
    return response

if __name__ == "__main__":
    app.run(debug=True)

"""