import matplotlib.pyplot as plt

x=[2023,2022,2021,2020]
y=[1302,1212,1100,1045]

plt.plot(x,y,"y")  #muda a cor do grafico
plt.grid()         #adiciona grades no fundo do grafico
plt.scatter()      #adc pontos nas cordenadas demarcadas
plt.xlabel("x")    #adc uma legenda para a coordenada x
plt.ylabel("y")    #adc uma legenda para a coordenada y
plt.show() #exibe o grafico