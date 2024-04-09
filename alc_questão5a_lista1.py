import math
theta1 = int(input('Ângulo_Theta1: '))
theta2 = int(input('Ângulo_Theta2: '))

def position(theta1, theta2):
    
    if not (0<=theta1<=360)or not (0<=theta2<=360):         # Verifica se os ângulos estão entre 0 e 360 graus.
     raise Exception("Os ângulos devem estar entre 0 e 360 graus")
    
    rad1 = math.radians(theta1)                             #Transforma para Radianos
    #rad2 = math.radians(theta2)                            #Transforma para Radianos

    Theta=theta1+theta2                                     #Cálculo de Theta
    rad = math.radians(Theta)                               #Transforma para Radianos
    
    # Cálculo do Seno
    seno1= math.sin(rad1)
    #seno2= math.sin(rad2)
    seno = math.sin(rad)

    # Cálculo do Cosseno
    cosseno1 = math.cos(rad1)
    #cosseno2 = math.cos(rad2)
    cosseno = math.cos(rad)

    L1 = 20
    L2 = 15

    #Calculo de X e Y
    x=L1*cosseno1+L2*cosseno
    y=L1*seno1+L2*seno
    #Arredondamento para 1 Casa Decimal
    x=round(x, 1)
    y=round(y, 1)

    return x,y

x,y=position(theta1,theta2)
print(f'O resultado de X é {x}')
print(f'O resultado de Y é {y}')


    
