
from random import randint

numero = randint(1, 100)
intentos = 0
print('Debe adivinar un número al azar del 1 al 100, tiene 8 intentos para lograrlo. \nSi falla el juego elegirá otro número al azar')

while intentos <= 8:
    intentos += 1
    adivina = int(input('Ingrese un número del 1 al 100: '))
    if intentos == 8:
        intentos = 0
        numero = randint(1, 100)
        print('Haz alcanzado el máximo de intentos, se volverá a elegir un número al azar que debes adivinar')
        continue
    if adivina == numero:
        print(f'ES CORRECTO, adivinaste el número {numero} y te tomó: {intentos} intentos')
        break
    elif adivina < 1 or adivina > 100:
        print('Incorrecto! debes elegir un número entre la franja del 1 al 100')
    elif adivina > numero:
        print('Incorrecto! el número elegido es mayor al número que debes adivinar')
    elif adivina < numero:
        print('Incorrecto! el número elegido es menor al número que debes adivinar')