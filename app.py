from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from flasgger import Swagger
from models import db, FluxoCaixa
from datetime import datetime
import os

app = Flask(__name__)
CORS(app)

# Configurações da aplicação
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SWAGGER'] = {
    'title': 'Fluxo de Caixa API',
    'uiversion': 3
}

# Inicialização das extensões
db.init_app(app)
Swagger(app)

@app.route('/fluxo_caixa', methods=['GET'])
def get_fluxo_caixa():
    """Lista todos os registros do fluxo de caixa
    ---
    responses:
      200:
        description: Lista de registros
    """
    fluxo = FluxoCaixa.query.all()
    return jsonify([{
        'id': f.id,
        'descricao': f.descricao,
        'tipo': f.tipo,
        'valor': f.valor,
        'data': f.data.strftime('%Y-%m-%d %H:%M:%S')
    } for f in fluxo])

@app.route('/fluxo_caixa', methods=['POST'])
def add_fluxo_caixa():
    """Adiciona um novo registro ao fluxo de caixa
    ---
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            descricao:
              type: string
            tipo:
              type: string
              enum: [entrada, saida]
            valor:
              type: number
          required:
            - descricao
            - tipo
            - valor
    responses:
      201:
        description: Registro criado com sucesso
      400:
        description: Dados inválidos
    """
    data = request.get_json()
    descricao = data.get('descricao')
    tipo = data.get('tipo')
    valor = data.get('valor')

    if not descricao or not tipo or not valor:
        return jsonify({'error': 'Dados inválidos'}), 400

    novo_fluxo = FluxoCaixa(descricao=descricao, tipo=tipo, valor=valor)
    db.session.add(novo_fluxo)
    db.session.commit()

    return jsonify({
        'message': 'Registro criado com sucesso',
        'id': novo_fluxo.id,
        'descricao': novo_fluxo.descricao,
        'tipo': novo_fluxo.tipo,
        'valor': novo_fluxo.valor,
        'data': novo_fluxo.data.strftime('%Y-%m-%d %H:%M:%S')
    }), 201

@app.route('/fluxo_caixa/<int:id>', methods=['DELETE'])
def delete_fluxo_caixa(id):
    """Remove um registro do fluxo de caixa
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID do registro a ser removido
    responses:
      200:
        description: Registro excluído com sucesso
      404:
        description: Registro não encontrado
    """
    fluxo = FluxoCaixa.query.get(id)
    if not fluxo:
        return jsonify({'error': 'Registro não encontrado'}), 404

    db.session.delete(fluxo)
    db.session.commit()
    return jsonify({'message': 'Registro excluído com sucesso'})

@app.route('/saldo', methods=['GET'])
def get_saldo():
    """Retorna o saldo atual (entradas - saídas)
    ---
    responses:
      200:
        description: Saldo atual
    """
    entradas = db.session.query(db.func.sum(FluxoCaixa.valor)).filter(FluxoCaixa.tipo == 'entrada').scalar() or 0
    saidas = db.session.query(db.func.sum(FluxoCaixa.valor)).filter(FluxoCaixa.tipo == 'saida').scalar() or 0
    saldo = entradas - saidas
    return jsonify({'saldo': saldo})

# Rota para servir o swagger.json
@app.route('/swagger.json')
def swagger_json_file():
    return send_from_directory(os.path.join(app.root_path, 'swagger'), 'swagger.json')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
