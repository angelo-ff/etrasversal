import msvcrt
import os
import numpy
from colorama import Fore, Style
"""
Platinum, $120.000. (Asientos del 1 al 20).
 Gold, $80.000. (Asientos del 21 al 50).
 Silver, $50.000. (Asientos del 51 al 100.).
"""
escenario = numpy.empty([10,10], object)
platinun = 120000
gold = 80000
silver = 50000
ganancias = 0




def limpiar_pantalla():
    print(f"{Fore.BLACK}{Style.BRIGHT}<<PRESIONE UNA TECLA PARA CONTINUAR>>{Style.RESET_ALL}{Fore.RESET}")
    msvcrt.getch()
    os.system('cls')

def printa(texto):
    print(f"{Fore.YELLOW}{Style.DIM}{texto}{Style.RESET_ALL}{Fore.RESET}")

def titulo(texto):
    print(f"{Fore.CYAN}\t**********************{Fore.RESET}")
    print(f"{Fore.MAGENTA}{Style.BRIGHT}{texto}{Style.RESET_ALL}{Fore.RESET}")
    print(f"{Fore.CYAN}\t**********************{Fore.RESET}")

def printv(texto):
    print(f"{Fore.GREEN}{Style.DIM}{texto}{Style.RESET_ALL}{Fore.RESET}")

def printr(texto):
    print(f"{Fore.RED}{Style.DIM}{texto}{Style.RESET_ALL}{Fore.RESET}")

def verescenario():
    print("(                ESCENARIO            )")
    print("⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛")
    print(" A   B   C   D   E   F   G   H   I   J")
    for x in range(10):
        for y in range(10):
            if escenario[x,y] == None:
                print(f"{y+1}🟩", end=" ")
            else:
                print(" 🟥", end=" ")
                
        print(f"{10 - x}")

rutguardados = []

letras = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"] 
filas = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

cantpla = 0
cantgold = 0
cantsil = 0 

def comprarentrada (colum, fila, rut, cantidad):
    totalpagar = 0
    global cantpla 
    global cantgold 
    global cantsil 
    global ganancias
    if verescenario != None:
        if fila >=1 and fila <= 10:
            if rut >= 11111111 and rut <= 99999999:
                if cantidad >= 1 and cantidad<= 3:  
                    if cantidad == 1:     
                        if colum in letras:
                            columnas = letras.index(colum)
                            asiento = filas.index(fila)
                            if asiento == 10 or 9:
                                print(f"El valor de la entrada es {platinun}")
                                totalpagar = platinun

                                pago = int(input("ingrese monto"))

                                if pago == totalpagar:
                                    cantpla += 1
                                    ganancias = totalpagar
                                else:
                                    printr("Dinero insuficiente")
                            elif asiento == 8 or 7 or 6:
                                print(f"El valor del asiento es {gold}")
                                totalpagar = gold
                                pago = int(input("Ingrese monto"))
                                if pago >= totalpagar:
                                    cantgold += 1
                                    ganancias = gold
                                    for x in range(asiento):
                                        if escenario[asiento,columnas] == None:
                                            escenario[asiento,columnas] = rut
                                            printa("Asiento comprado")
                                            break   
                            elif asiento >=1 and asiento<= 5:
                                print(f"El valor del asiento es {silver}")
                                totalpagar = silver
                                pago = int(input("Ingrese monto :  "))
                                if pago >= totalpagar:
                                    cantsil += 1
                                    ganancias += silver
                                    for x in range(asiento):
                                        if escenario[asiento,columnas] == None:
                                            escenario[asiento,columnas] = rut
                                            printa("Asiento comprado")
                                            break   
                        else:
                            printr("Columna invalida")            
                    elif cantidad == 2:
                        pass        
                else:
                    printr("la cantidad a comprar no puede ser mayor a 3")
            else:
                printr("Rut no valido")
        else:
            printr("Fila no valida")
    else:
        printr("Ya no hay asientos disponibles")

totalcant = (cantpla + cantgold + cantsil)
def ganancias ():
    print(f"""
     TIPO DE ENTRADA | CANTIDAD | TOTAL|
    -Platinun ${platinun}     {cantpla}        
    -Gold     ${gold}      {cantgold}  
    -Silver   ${silver}      {cantsil}
    -Total                {totalcant}          {ganancias}  

    
    
    """)