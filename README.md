# pilar-case-backend

## Instalar dependências
- pip install -r requirements.txt

## Rodar aplicação localmente
- python main.py

## Acessar endpoints localmente
### URL BASE: 
- http://localhost:5005
### Conta vogais em palavras: 
- http://localhost:5005/vowel_count
### Ordena palavras em um array: 
- http://localhost:5005/sort

## Rodar testes
- pytest

## Acessar aplicação deployada no HEROKU:
### URL BASE: 
- https://pilar-case-backend.herokuapp.com/
### Conta vogais em palavras: 
- https://pilar-case-backend.herokuapp.com/vowel_count
### Ordena palavras em um array: 
- https://pilar-case-backend.herokuapp.com/sort
# Descrição do Teste
Usando Python, escreva o código de uma API com as seguintes rotas:

[POST] /vowel_count -- conta vogais em palavras

Requisição: {"words": ["batman", "robin", "coringa"]}

Resposta: {"batman": 2, "robin": 2, "coringa": 3}

[POST] /sort -- ordena palavras em um array, aceitando ordenação reversa

Requisição: {"words": ["batman", "robin", "coringa"], "order": "asc"}

Resposta: ["batman", "coringa", "robin"]

Requisição: {"words": ["batman", "robin", "coringa"], "order": "desc"}

Resposta: ["robin", "coringa", "batman"]

Caso as requisições estejam fora dos padrões especificados acima, retorne o código HTTP apropriado (ex: método não é POST, rota inexistente, content type não é application/json) 

Construa um pipeline no GitHub Actions ou GitLab que rode 3 etapas: lint, testes e deploy utilizando uma ferramenta como Python Anywhere, Heroku, AWS ou outra de sua preferência.