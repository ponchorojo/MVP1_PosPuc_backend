# Fluxo de Caixa - Projeto MVP - Victor Magno Thuler Pereira

Este é um sistema simples de fluxo de caixa com **front-end em HTML/CSS/JS puro** e **back-end em Python (Flask)**. Ele permite registrar entradas e saídas financeiras, visualizar a lista de registros e calcular o saldo total, além de cancelar registros (DELETE).

---

## Estrutura do Projeto

```
MVP_Fluxo_de_caixa/
├── front_end/           # Interface web (HTML, JS e CSS)
│   ├── index.html
│   ├── script.js
│   └── style.css
│
└── back_end/            # API REST com Flask
    ├── app.py
    ├── models.py
    └── requirements.txt
```

---

## Como Rodar o Projeto:

### 1. Rodar o Back-End (Flask)

#### Passos:

```bash
cd back_end
python -m venv venv
# Ative o ambiente virtual:
# Windows:
venv\Scripts\activate

# Instale as dependências:
pip install -r requirements.txt

# Execute o servidor Flask:
python app.py
```
> Para acessar o Swagger: `http://localhost:5000/apidocs`
