import CALCULO as cal

cal = cal.calculos()


class menu():
    option = ""
    while option != "6":
        option = input("Selecione la opcion que desea realizar:\n" +
                       "1 - Calculo de salario\n" +
                       "2 - Escribir un nombre\n" +
                       "3 - Elevacion de nuemro entero\n" +
                       "4 - Revision de numeros primos\n" +
                       "5 - Contar la letra 'a' en una cadena de texto\n" +
                       "6 - Salir\n")

        if (option == "1"):
            cal.calcSalary()

        elif (option == "2"):
            cal.printName()

        elif (option == "3"):
            cal.elevate()

        elif (option == "4"):
            cal.primeNumber()

        elif (option == "5"):
            cal.countStr()

        elif (option == "6"):
            pass

        else:
            print("Opcion no valida")