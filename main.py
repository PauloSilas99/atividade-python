# Defina três variáveis: nome, idade, e cidade.
# Atribua a elas valores apropriados.
# Crie uma função chamada informacoes_pessoais que imprima uma frase completa usando essas variáveis.

nome = "Paulo"
idade = 24
cidade = "São Luís"

def informacoes_pessoais():
    print('Olá,eu me chamo ',nome,'tenho',idade,'anos e sou de',cidade)

informacoes_pessoais()

# Defina uma variável global chamada contador com o valor 0.
# Crie uma função chamada incrementar_contador que incremente contador em 1 e imprima o valor atualizado.
# Crie uma variável local dentro da função incrementar_contador chamada mensagem e defina-a como uma string.

contador = 0

def incrementar_contador():
    global contador
    contador += 1
    print('Valor do contador:',contador)
    mensagem = "contador atualizado"
    print(mensagem)

incrementar_contador()
