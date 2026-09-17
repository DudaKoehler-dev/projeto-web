from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

print(__name__)

@app.route('/')
def inicio():
    return '<h1> Oiiiiiii </h1>'

@app.route('/sobre')
def sobre():
    return '''

<h1 style='color:red'>Meu nome é: </h1>
<p>João Paulo <b>Magagnato</b>
<!-- Tudo que eu pensar em html pode vir aqui -->

'''


@app.route('/tudo')
def tudo():
    return '''


<h1 style='color:blue'> Curso de GTI </h1>

'''

@app.route('/var')
def variavel():
    palavra = 'Sabugo'
    return f'<h1>Adicionando texto de var: {palavra}'

@app.route('/idade/<int:ano>')
def idade(ano):
    calculoIdade = 2026 - ano
    return f'Você tem {calculoIdade} anos!'

@app.route('/salvar/<nome>/produtos')
def salvar(nome):
    return f'Você salvou o produto [ {nome} ] com sucesso'


@app.route('/rotanova')
def rotanova():
    return '<h1>Essa é uma rota nova criada hoje!</h1>'

@app.route('/html')
def pagina_html():
    return render_template('index.html')

@app.route('/calcular/<nome>/<int:ano>')
def calcular(nome, ano):
    ano_atual = datetime.now().year
    idade = ano_atual - ano

    if idade > 18:
        status = 'Maior de Idade - ACESSO LIBERADO'
    else:
        status = 'Menor de Idade - ACESSO NEGADO'

    return render_template('variaveis.html', nome_usuario = nome,
                            ano_atual = ano_atual, nascimento = ano,
                            idade = idade, status = status)
                            
@app.route('/dicio')
def dicionario():
    dados = {
        'chave' : 'valor',
        'curso' : 'GTI',
        'local' : 'Fatec Jahu',
        'semestre' : '4°',
    }
    return render_template('dicio.html', **dados)


@app.route('/condicao/<int:numero>')
def condicao(numero):
    return render_template('condicao.html', numero = numero)

@app.route('/perfil/<nome>')
def perfil(nome):
    # Simulando um banco de dados com um dicionário de usuários
    # Na Aula 05 isso virá do MySQL de verdade
    usuarios = {
        'admin': {
            'nome': 'Administrador',
            'email': 'admin@fatec.br',
            'nivel': 'administrador',
            'ativo': True,
            'posts': 47
        },
        'joao': {
            'nome': 'João Silva',
            'email': 'joao@email.com',
            'nivel': 'usuario',
            'ativo': True,
            'posts': 12
        },
        'maria': {
            'nome': 'Maria Souza',
            'email': 'maria@email.com',
            'nivel': 'moderador',
            'ativo': False,
            'posts': 31
        }
    }

    # Busca o usuário pelo nome na URL — .get() retorna None se não existir
    usuario = usuarios.get(nome)

    # Passa o usuário (ou None) para o template
    return render_template('perfil.html', usuario=usuario, nome_buscado=nome)

# --- ULTIMA COISA DO ARQUIVO ---
if __name__ == '__main__':
    app.run(debug=True)