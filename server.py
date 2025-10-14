from flask import Flask, render_template, request
from backend.server import call_model, generate_plan



app = Flask(__name__)





@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    nom = request.form.get('nom')
    if nom:
        
        return f"<h2>{"Welcome ! Here is your fully generate by IA Course !", {generate_plan(nom)}} !</h2><a href='/'>Retour</a>"
        


if __name__ == '__main__':
    app.run(debug=True)