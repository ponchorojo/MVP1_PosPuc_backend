from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class FluxoCaixa(db.Model):
    __tablename__ = 'fluxo_caixa'
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(100), nullable=False)
    tipo = db.Column(db.String(10), nullable=False)  # 'entrada' ou 'saida'
    valor = db.Column(db.Float, nullable=False)
    data = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __repr__(self):
        return f'<FluxoCaixa {self.descricao}, {self.tipo}, {self.valor}>'
    