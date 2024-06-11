texto = input("Informe a letra")
VOGAIS = ("AEIOU")

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")

print("\n")