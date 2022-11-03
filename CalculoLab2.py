import math


class calculos():
    def __init__(self):
        self.TraH = None
        self.PagoH = None
        self.Usu = None
        self.Num = None
        self.str = None

#Calculo del salario 
 
    def calcSalary(self):
        self.TraH = int(
            input("Ingrese horas trabajadas:\n"))
        self.PagoH = int(
            input("Ingrese el dinero por horas\n"))
        calc = self.PagoH * self.TraH
        print(f"Horas trabajadas: {self.TraH}.\n" +
              f"Pago por hora: {self.PagoH}.\n" +
              f"El monto total de su paga es de: {calc}")

#Lectura del nombre

    def printName(self):
        self.usu = input("Por favor escriba su nombre:\n")

        print(f"Bienvenido a la UIA {self.usu.lower()}\n" +
              f"Bienvenido a la UIA {self.usu.upper()}")

#Estrutura de elevacion de numeros

    def elevate(self):
        self.Num = int(input('Escriba el numero entero\n'))

        if (self.Num >= 1 and self.Num <= 10):
            print(f"Elevar a 2: {math.pow(self.Num, 2)}")
        elif (self.Num >= 11 and self.Num <= 20):
            print(f"Elevar a 4: {math.pow(self.Num, 4)}")
        elif (self.Num >= 21 and self.Num <= 30):
            print(f"Elevar a 6: {math.pow(self.Num, 6)}")
        elif (self.Num >= 31 and self.Num <= 40):
            print(f"Elevar a 8: {math.pow(self.Num, 8)}")
        elif (self.Num >= 41 and self.Num <= 50):
            print(f"Elevar a 10: {math.pow(self.Num, 10)}")
        else:
            print(f"Numero no valido: {0}")

#Descifrado de numeros primos 

    def primeNumber(self):
        self.Num = int(
            input("Inserte el numero para identificar si es un numero primo o no\n"))

        def isPrime(num):
            for i in range(2, num):
                if (num % i == 0):
                    return False
            return True

        if (isPrime(self.Num)):
            print(f"{self.Num} es un numero primo.")

        else:
            print(f"{self.Num} no es un numero primo.")

    def countStr(self):
        self.str = input("Escribe el texto que desee\n")
        print(
            f"El texto  '{self.str.lower()}' tiene {self.str.count('a')} 'a' ")