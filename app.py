from flask import Flask, render_template, request, jsonify
import pyodbc

app = Flask(__name__)

# String de conexão
server = 'DESKTOP-N24SLK8'
database = 'italiancars'
username = 'DESKTOP-N24SLK8'

conn_str = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};Trusted_Connection=yes'

conn = pyodbc.connect(conn_str)
cursor = conn.cursor()


@app.route('/api/carros', methods=['POST'])
def cadastrar_carro():
    data = request.json

    fabricante_id = data.get('fabricante')
    modelo = data.get('modelo')
    ano = data.get('ano')
    cor = data.get('cor')
    km = data.get('km')
    preco = data.get('preco')

    try:
        cursor.execute("INSERT INTO Carro (idFabricante, modelo, ano, cor, km, preco) VALUES (?, ?, ?, ?, ?, ?)",
                       (fabricante_id, modelo, ano, cor, km, preco))
        conn.commit()

        return jsonify({'message': 'Carro cadastrado!'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/cadastrar_carro')
def obter_lista_fabricante():

    cursor.execute("SELECT id, nomeFabricante FROM Fabricante")
    fabricantes = cursor.fetchall()

    return render_template('cadastrar_carro.html', fabricantes=fabricantes)


if __name__ == '__main__':
    app.run(debug=True)
