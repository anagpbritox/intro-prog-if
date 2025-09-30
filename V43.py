# @cikey b8c2f0e997296c4047aa90efbb14a388
# @sid 20251174010038
# @aid V4.3


#begin_inputs

mes = int(input("Digite o numero do mes: "))

#end_inputs

lista = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']

saída = mes - 1

if 1 > mes or mes > 12:
    print('mes invalido')
else:
    print(lista[saída])