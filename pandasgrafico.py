import pandas as pd

import matplotlib.pyplot as plt

arquivocsv = input("digite o nome do arquivo csv a ser lido, ele deve estar na mesma pasta do projeto")

separador = input("digite o separador utilizado neste arquivo, por exemplo , ou ;")

#lendo o arquivo csv que está disponivel neste endereço e separado por ponto e virgula, e com o codigo abaixo..armazenando em df_etanol

dataframeCriado = pd.read_csv(arquivocsv, sep=separador)   


colunax = input("Digite o nome da coluna que ficará no eixo x, digite igualzinho ao que está no arquivo.csv")

colunay = input("Digite o nome da coluna que ficará no eixo y, digite igualzinho ao que está no arquivo.csv")


#trocando as , por . na coluna do eixo y, caso existam
dataframeCriado[colunay] = dataframeCriado[colunay].str.replace(',','.')   

#convertendo a coluna y para float
dataframeCriado[colunay] = dataframeCriado[colunay].astype(float)

x = dataframeCriado[colunax]
y = dataframeCriado[colunay]

cor = (input("Digite a cor que voce quer que fique a barra: r(vermelho), g(verde), b(azul), y(amarelo)"))

barra = (input("Se voce quiser barras horizontais digite h, se quiser barra verticais digite v"))

if barra == 'h':
    barraescolhida = 'barh'
else:
    barraescolhida = 'bar'

titulo = input("Digite um titulo para o grafico")

textox = input("digite o texto que deve aparecer no eixo x")

textoy = input("digite o texto que deve aparecer no eyxo y ")

if(barra == 'h'):
    plt.barh(x, y, color={cor})
    plt.title(titulo)
    plt.xlabel(textox)
    plt.ylabel(textoy)

    plt.show()
else:
    plt.bar(x, y, color={cor})
    plt.title(titulo)
    plt.xlabel(textox)
    plt.ylabel(textoy)

    plt.show() 





