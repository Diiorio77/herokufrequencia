from flask import Flask, request, jsonify
import pickle


boost =  pickle.load(open("modelo.sav", "rb"))

colunas = ["maximo", "minimo", "frequencia", "aumento_frequencia"]

app = Flask(__name__)

@app.route('/')
def funcao():
    return "API Para Retorno das previsões do modelo de regressão"


@app.route('/previsao/', methods=['POST'])
def bpm():
    informacao = request.get_json()
    informacao_input = [informacao[col] for col in colunas]
    bpm_previsto = boost.predict([informacao_input])
    return jsonify(previsao=bpm_previsto[0].round(2))



app.run(debug=True)


