numero=int(input("Insira um numero de 1 a 12: "))-1
meses=["janeiro","fevereiro","março","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro"]


for x in range(1,12):
    if x==numero:
        print("O mes é: ",meses[numero])
        
if x != numero :
    print("Valor  não corresponde a nenhum mês")