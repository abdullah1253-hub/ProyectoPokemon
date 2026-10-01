from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    proyecto = "Batallas Pokemon"
    nombre = "Abdullah Riaz"
    año = 2026

    return render_template(
        'index.html',
        proyecto=proyecto,
        nombre=nombre,
        año=año
    )


if __name__ == '__main__':
    app.run('0.0.0.0', 8080)