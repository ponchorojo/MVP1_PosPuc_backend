# 💸 Fluxo de Caixa - Projeto MVP

Este é um sistema simples de fluxo de caixa com **front-end em HTML/CSS/JS puro** e **back-end em Python (Flask)**. Ele permite registrar entradas e saídas financeiras, visualizar a lista de registros e calcular o saldo total, além de cancelar registros (DELETE).

---

## Estrutura do Projeto

```
fluxo_caixa_app/
├── front/           # Interface web (HTML, JS e CSS)
│   ├── index.html
│   ├── script.js
│   └── style.css
│
└── back/            # API REST com Flask
    ├── app.py
    ├── models.py
    └── requirements.txt
```

---

## Como Rodar o Projeto

### 1. Rodar o Back-End (Flask)

#### Passos:

```bash
cd back_end
python -m venv venv
# Ative o ambiente virtual:
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

# Instale as dependências:
pip install -r requirements.txt

# Execute o servidor Flask:
python app.py
```

> O servidor irá rodar em: `http://localhost:5000`


> Para acessar o Swagger: `http://localhost:5000/apidocs`
