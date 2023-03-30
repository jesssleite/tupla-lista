# Lista []
# Tupla () <IMPORTANTE> são imutáveis!!!!!

t = (1, 2, 3)  # 0:1 1:2 2:3
t2 = ("A", "B", "C")  # 0:"A" 1:"B" 2:"C"
print(type(t))

l = [1, 2, 3]
print(type(l))

print("Imprimindo segundo elemento da tupla", t[1])
print("Imprimindo segundo elemento da lista", l[1], " da lista", l)

l[1] = 5

print("Imprimindo segundo elemento da lista", l[1], " da lista", l)

t = (1, 5, 3)

print("Imprimindo segundo elemento da tupla", t[1], "da tupla ", t)

# Desempacotamento de tuplas
# swap de variáveis
a = 2
b = 3

# a = 3 e b = 2
a, b = b, a

print("a:", a, "b:", b)

# Desempacotamento
x, z, y = t


print(f"X:{x}, Z:{z}, Y:{y}")

# Pegadinha do malandro para tupla!
# Para declarar uma tupla com um elemento tem que usar vígula!!!
no_tupla = ("a")
print("no_tupla:", type(no_tupla))

tupla = ("a",)
print("tupla:", type(tupla))

# Próxima aula: desempacotamento de tupla vida real

if __name__ == '__main__':
    jessica = ("Jéssica", 25, "Estudante", "jessica@gmail.com")
    print("Nome: {}, Idade: {}, Profissão: {}, E-mail: {}".format(*jessica)) # metodo antigo python
    # é usado  para explodir todos os dados da tupla

    name, age, occupation, email = jessica
    print(f"Nome: {name}, Idade: {age},"
          f" Profissão: {occupation}," # metodo usado para novo Python
          f" E-mail: {email}")

# slice (Vale para lista, tuplas e strings) [start:end:step]
# o start é inclusive (bolinha cheia)
# o end é não inclusivo (bolinha vazia)
# o step pode ser negativo
# l[start:end:step]

#Para fazer uma cópia é preciso usar slice [:] ou o metodo copy
#nomes3 = nomes[:] ou nomes3 = nomes.copy()