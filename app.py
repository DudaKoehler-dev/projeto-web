from flask import Flask

app = Flask(__name__)

@app.route('/')
def pagina_inicial():

     return '<h1>Meu primeiro servidor Flask está funcionando e a duda não toma banho.</h1>'

@app.route('/nome')
def nome():

     return '<p>O daniel toma bastante</p>'


if __name__ == '__main__':
    app.run(debug=True)
