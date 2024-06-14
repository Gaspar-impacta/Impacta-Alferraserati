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


@app.route('/api/carros', methods=['GET'])
def listar_carros():
    try:
        ordenacao = request.args.get('ordenacao')

        ordenacao_map = {
            '1': 'F.nomeFabricante ASC',
            '2': 'F.nomeFabricante DESC',
            '3': 'C.ano ASC',
            '4': 'C.ano DESC',
            '5': 'C.km ASC',
            '6': 'C.km DESC',
            '7': 'C.preco ASC',
            '8': 'C.preco DESC',
        }
        consulta_sql = """
            SELECT C.id, F.nomeFabricante, C.modelo, C.ano, C.cor, C.km, C.preco 
            FROM Carro AS C 
            INNER JOIN Fabricante AS F ON C.idFabricante = F.id
        """

        if ordenacao and ordenacao in ordenacao_map:
            consulta_sql += f" ORDER BY {ordenacao_map[ordenacao]}"

        cursor.execute(consulta_sql)
        carros = cursor.fetchall()

        carros_list = []
        for carro in carros:
            carro_dict = {
                'id': carro[0],
                'nomeFabricante': carro[1],
                'modelo': carro[2],
                'ano': carro[3],
                'cor': carro[4],
                'km': carro[5],
                'preco': carro[6]
            }
            carros_list.append(carro_dict)

        return jsonify(carros_list)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
       

@app.route('/lista')
def lista_carros():
    try:
        cursor.execute("SELECT C.id, F.nomeFabricante, C.modelo, C.ano, C.cor, C.km, C.preco FROM Carro C INNER JOIN Fabricante F ON C.idFabricante = F.id")
        carros = cursor.fetchall()

        return render_template('lista.html', carros=carros)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/editar_carro', methods=['GET'])
def renderizar_pagina_edicao():
    return render_template('editar_carro.html')


@app.route('/api/carros/<int:id_carro>/editar', methods=['GET'])
def obter_dados_carro_para_edicao(id_carro):
    try:
        cursor.execute("""
            SELECT C.id, F.nomeFabricante, C.modelo, C.ano, C.cor, C.km, C.preco 
            FROM Carro C 
            INNER JOIN Fabricante F ON C.idFabricante = F.id
            WHERE C.id = ?
        """, (id_carro,))
        carro = cursor.fetchone()

        if carro:
            carro_dict = {
                'id': carro[0],
                'nomeFabricante': carro[1],
                'modelo': carro[2],
                'ano': carro[3],
                'cor': carro[4],
                'km': carro[5],
                'preco': carro[6]
            }
            return jsonify(carro_dict)
        else:
            return jsonify({'error': 'Carro não encontrado.'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/carros/<int:id_carro>', methods=['PUT'])
def atualizar_carro(id_carro):
    data = request.json 

    km = data.get('km')
    preco = data.get('preco')

    try:
        cursor.execute("""
            UPDATE Carro 
            SET km = ?, preco = ?
            WHERE id = ?
        """, (km, preco, id_carro))
        conn.commit()

        return jsonify({'message': 'Carro atualizado com sucesso!'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/carros/<int:idCarro>', methods=['DELETE'])
def deletar_carro(idCarro):
    try:
        cursor.execute("DELETE FROM Carro WHERE id = ?", (idCarro,))
        conn.commit()

        return jsonify({'message': 'Carro deletado com sucesso!'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
