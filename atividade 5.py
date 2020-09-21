mulher=0
homem=0
idadeFeminina=0
idadeMasculina=0
for x in range(10):
    sexo=(input("Insira o seu sexo (f/m): "))
    if sexo=="m":
         mulher=mulher+1
         idadeFeminina=idadeFeminina+(int(input("Insira sua idade: ")))
    else:
        homem=homem+1
        idadeMasculina=idadeMasculina+(int(input("Insira sua idade: ")))



print("A media da idade dos homens é",idadeMasculina/homem)
print("A media da idade das mulheres é",idadeFeminina/mulher)
print("A Idade média do grupo",(idadeFeminina+idadeMasculina)/(homem+mulher))



