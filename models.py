from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class FluxoCaixa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(100), nullable=False)
    tipo = db.Column(db.String(10), nullable=False)  # "entrada" ou "saida"
    valor = db.Column(db.Float, nullable=False)
    data = db.Column(db.DateTime, default=datetime.now)
