#pergunta qual o nome do usuario
name = input("whats your name?")
#criando funcao que da oi 
def hello (name): 
#coloca maiusculo na str (com a funcao "capitalize so vai deixar maiusculo a primeira palavra") e remove espacos em branco AO LADO de string
    name = name.title().strip()
#dividir nome e sobrenome 
    nome, sobrenome = name.split(" ")
#essa funcao retorna o sobrenome 
    return sobrenome
#da oi para o usuario 
print(f"hello, {hello(name)}!" )


