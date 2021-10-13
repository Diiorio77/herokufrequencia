from flask import Flask, request, jsonify
from sklearn.ensemble import GradientBoostingRegressor
import pickle


boost =  pickle.load(open("modelo.sav", "rb"))

colunas = ["maximo", "minimo", "frequencia", "aumento_frequencia"]

app = Flask(__name__)

@app.route('/')
def funcao():
    return "Camus de Aquário"


@app.route('/previsao/', methods=['POST'])
def bpm():
    informacao = request.get_json()
    informacao_input = [informacao[col] for col in colunas]
    bpm_previsto = boost.predict([informacao_input])
    return jsonify(previsao=bpm_previsto[0].round(2))


if __name__ == '__main__':
    app.run(debug=True)


