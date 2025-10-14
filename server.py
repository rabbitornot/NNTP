from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    nom = request.form.get('nom')
    if nom:
        return f"<h2>Bonjour, {nom} !</h2><a href='/'>Retour</a>"
    else:
        return "<h2>Veuillez entrer un nom.</h2><a href='/'>Retour</a>"

if __name__ == '__main__':
    app.run(debug=True)