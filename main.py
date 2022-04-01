from flask import Flask, render_template, request
import game_of_life

app = Flask(__name__)


@app.route('/', methods=['get', 'post'])
@app.route('/index.html', methods=['get', 'post'])
def index():
    server_message = ''
    dl = 20
    sh = 20
    if request.method == 'POST':
        if request.form.get('dl').isdigit() and request.form.get('sh').isdigit():
            dl = int(request.form.get('dl'))
            sh = int(request.form.get('sh'))
            server_message = f"Красаучык. Размеры поля изменены на: { dl }x{ sh }. Наслаждайся <3"
        elif dl == 20 and sh == 20:
            server_message = "С тандартные размеры поля 20х20, неплохой выбор. Да? Наслаждайся <3"
        else:
            server_message = "Пчел введи числа"


    game_of_life.GameOfLife(dl, sh)
    return render_template('index.html', server_message=server_message)


@app.route('/live')
@app.route('/live.html')
def live():
    game = game_of_life.GameOfLife()
    if game.life_counter > 0:
        game.form_new_generation()
    game.life_counter += 1

    return render_template('live.html', game=game)



if __name__ == '__main__':
    app.run(debug=True)
