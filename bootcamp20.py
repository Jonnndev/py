#Strings


curso = "Python"


#Letras maiusculas
print(curso.upper())

#Letras minusculas
print(curso.lower())

#Title
print(curso.title())



curso2 = "   Python  "

#Espaçamentos

print(curso2.strip()) #TIRA TODOS ESPAÇAMENTOS

print(curso2.lstrip()) #TIRA OS ESPAÇAMENTOS DA ESQUERDA (LEFT)

print(curso2.rstrip()) #TIRA OS ESPAÇAMENTOS DA DIREITA (RIGHT)

#Interpolacao strings
print(".".join(curso))
