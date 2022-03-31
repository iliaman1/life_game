from flask import Flask, render_template
import game_of_life

app = Flask(__name__)


@app.route('/')
@app.route('/index.html')
def index():
    game_of_life.GameOfLife(25, 25)
    return render_template('index.html')


@app.route('/live')
@app.route('/live.html')
def live():
    game = game_of_life.GameOfLife()
    game.form_new_generation()
    game.life_counter += 1

    return render_template('live.html', game=game)



if __name__ == '__main__':
    app.run(debug=True)
