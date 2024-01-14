import numpy as np
import matplotlib.pyplot as plt
from scipy.special import mathieu_cem
from scipy.integrate import odeint
import matplotlib.pyplot as plt


#QUESTÃO 1


def eqpendulo(y, t, g, l):                                                               # Representação da equação diferencial em forma de função
    teta, omega = y
    dydt = [omega, -(g/l) * np.sin(teta)]
    return dydt

teta0 = np.pi/4                                                                          # Ângulo inicial
omega0 = 0.0                                                                             # Velocidade angular inicial
y0 = [teta0, omega0]                                                                     # Momento inicial

g = 9.8                                                                                  # Aceleração da gravidade
l = 1.0                                                                                  # Tamanho do pêndulo em metros

t = np.linspace(0, 10, 1000)


solucao = odeint(eqpendulo, y0, t, args=(g, l))                                          # Resolução da eq. diferencial utilizando odeint da biblioteca scipy

plt.plot(t, solucao[:, 0], label='Ângulo (rad)')                                         #|
plt.plot(t, solucao[:, 1], label='Velocidade Angular (rad/s)')                           #|
plt.xlabel('Tempo (s)')                                                                  #| Plot do gráfico
plt.legend()                                                                             #|
plt.show()                                                                               #|

for tempo, (teta, omega) in zip(t, solucao):
    print(f'Tempo: {tempo:.2f}, Angulo: {teta:.4f}, Velocidade Angular: {omega:.4f}')    # Print dos cálculos realizados para montar o gráfico


#QUESTÃO 2

x = np.linspace(0, 10 * np.pi, 1000)                                                    # Gera um array de 0 a 10pi com 1000 espaços entre eles. Representa o domínio

plot1 = mathieu_cem(3, 3, x*180)[0]                                                     #|
plot2 = mathieu_cem(4, 4, x*180)[0]                                                     #| Função do scipy que calcula(ou tenta) as funções de Mathieu com diferentes parâmetros. (Algumas combinações de parâmetros deram errado)
plot3 = mathieu_cem(5, 5, x*180)[0]                                                     #|

plt.plot(x,plot1)                                                                       #|
plt.plot(x,plot2)                                                                       #| Plot dos gráficos das funções de Mathieu
plt.plot(x,plot3)                                                                       #|
plt.show()