from flask import *
from googletrans import Translator
import googletrans


app = Flask(__name__, template_folder="template")


@app.route('/')
def index():
    translator = Translator()  # Définit les langues source et cible
    text = "Bonjour, comment ça va ?"  # Texte à traduire
    translation = translator.translate(text, dest='en')  # Traduit le texte
    print(translation.text)  # Affiche la traduction
    lang = googletrans.LANGUAGES.values()
    print(lang)
    return render_template('index.html', data=lang)

if __name__ == "__main__":
    app.run(debug=True)