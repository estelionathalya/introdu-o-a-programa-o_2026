mensagem = input("mensagem: ")
tamanho = len(mensagem)
if tamanho < 3 or tamanho > 140:
    print("mensagem bloqueada por violar as diretrizes de spam!")
else:
     print("mensagem enviada com sucesso!")
