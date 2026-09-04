from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')

def pagina_inicial():
     return ''''
     <h1>Vai corinthians!</h1><p>Meu primeiro servidor Flask está funcionando.</p>
      <a href="/sobre">Ver quem fez</a>
      <a href="/corinthians">VAi curintia</a>

     '''
     
@app.route('/sobre')

def sobre():
     return '''
     <h1 style='color:blue'> Meu nome é </h1>
     <p> Daniel <b> Martins</b>
     <!-- e eu colocaria algo de hmtl se eu soubesse -->
     <a href="/">Voltar ao início</a>
     
     '''

@app.route('/var')
def var():
     palavra = 'hiagão'
     return f'<h1>adicionando texto de var: {palavra}</h1>'
    

@app.route('/idade/<int:ano>')
def idade(ano):
     calculoidade = 2026 - ano
     return f'você tem {calculoidade} anos!'

@app.route('/salvar/<nome>/produto')
def salvar(nome):
     return f'Você salvou o produto [{nome}] com sucesso ! '

@app.route('/html')
def pagina_html():
     return render_template('index.html')

@app.route('/corinthians')
def pagina_corinthians():
     return render_template('corinthians.html')

@app.route('/calcular/<nome>/<int:ano>')
def calcular(nome, ano):
     ano_atual = datetime.now().year
     idade = ano_atual - ano

     if idade > 18:
          status = 'Maior de Idade'
     else:
          status = 'Menor de idade - ACESSO NEGADO! CATARRENTO'
     
     return render_template('variaveis.html', nome_usuario = nome, ano_atual = ano_atual, nascimento = ano, idade = idade, status = status) 

# -- ultima coisa do arquivo, NÃO MEXER 
if __name__ == '__main__':
     app.run( debug=True )