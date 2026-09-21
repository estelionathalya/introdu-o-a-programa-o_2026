idade = int(input("idade: "))
carteira = input("carteira de estudante (s/n): ")
if idade >= 60:
    print("gratuidade concedida por lei!")
elif idade < 18 or carteira == "s":
    print("meia entrada autorizada!")
else: 
    print("passagem inteira!")