from flask import *
from googletrans import Translator
import googletrans


app = Flask(__name__, template_folder="template")
translator = Translator()  # Définit les langues source et cible


@app.route('/', methods=['GET', 'POST'])
def index():
    lang = list(googletrans.LANGUAGES.values())
    if request.method == 'POST':
        input_data = request.form.get('input')
        src_input_lang = request.form.get('src_input_lang')
        src_output_lang = request.form.get('src_output_lang')

        traduction = ""
        if src_input_lang != None and src_output_lang != None and input_data != None:
            translation = translator.translate(input_data, src=src_input_lang, dest=src_output_lang)  # Traduit le texte
            traduction = translation.text
        return render_template('index.html', data=lang, traduction=traduction)

    else :
        return render_template('index.html', data=lang)


    # print(src_output_lang)
    # print(input_data)
    # print(str(src_input_lang))

        
        
        # if src_input_lang != None and src_output_lang != None and input_data != None: 
        #     translation = translator.translate(input_data, src=src_input_lang, dest=src_output_lang)  # Traduit le texte
        #     print(translation.text)  # Affiche la traduction

        #     return render_template('index.html',  traduction=translation.text)

        # return render_template('index.html', data=lang)

if __name__ == "__main__":
    app.run(debug=True)