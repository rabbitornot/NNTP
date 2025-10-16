from flask import Flask, render_template, request, redirect, url_for
from backend.server import call_model, generate_plan
import json
from threading import Thread
import time

app = Flask(__name__)


results = {}

def format_json(output_ia):
    data = json.loads(output_ia)
    output_formated = ""
    chapters = data['chapters']
    
    for i, chapter in enumerate(chapters, start=1):
        output_formated += f"<h3>Chapitre {i} : {chapter['title']}</h3>"
        output_formated += f"<p><strong>Introduction :</strong> {chapter['introduction']}</p>"
        output_formated += f"<p><strong>Contenu :</strong> {chapter['content']}</p><hr>"
    
    return output_formated

def async_generate_plan(topic):
  
    results[topic] = generate_plan(topic)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    nom = request.form.get('nom')
    if nom:
       
        thread = Thread(target=async_generate_plan, args=(nom,))
        thread.start()
        
        return redirect(url_for('result', key=nom))
    return redirect(url_for('home'))

@app.route('/result/<key>')
def result(key):
    if key in results:

        formatted_output = format_json(results[key])
        return f"""
            <h2>Voici votre cours généré :</h2>
            {formatted_output}
            <br><a href='/'>Retour</a>
        """
    else:

        return f"""
            <h2>Le cours est toujours en cours de génération, merci de patienter...</h2>
            <p>La page se rafraîchira automatiquement.</p>
            <script>
                setTimeout(function() {{
                    window.location.reload();
                }}, 5000);
            </script>
            <a href='/'>Retour</a>
        """

if __name__ == '__main__':
    app.run(debug=True)
