import sqlite3

# Conectar ao banco de dados (o arquivo será criado automaticamente se não existir)
conn = sqlite3.connect('db.sqlite3')  # O arquivo db.sqlite3 será criado na mesma pasta
cursor = conn.cursor()

# Criar a tabela 'fluxo_caixa'
cursor.execute('''
CREATE TABLE IF NOT EXISTS fluxo_caixa (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    descricao TEXT NOT NULL,
    tipo TEXT CHECK(tipo IN ('entrada', 'saida')) NOT NULL,
    valor REAL NOT NULL,
    data TEXT DEFAULT (CURRENT_TIMESTAMP)
);
''')

# Confirmar as mudanças e fechar a conexão
conn.commit()
conn.close()

print("Banco de dados 'db.sqlite3' e a tabela 'fluxo_caixa' foram criados com sucesso!")