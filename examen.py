
def menu():
    print("""***CAJERO AUTOMATICO***
1. consultar saldo
2. depositar dinero
3. retirar dinero
4. Salir
----------
Opcion (1-4)?""")

def leer_opcion():
    op = input()
    while not op.isdigit() or int(op) < 1 or int(op) > 4:
        print("Error. Opcion no valida. Digite un numero del 1 al 4")
        input("Presione cualquier tecla para continuar...")
        print("\n")
        menu()
        op = input()
    return int(op)


def consultar_saldo (saldonuevo): 
    print("\n*** 1. CONSULTAR SALDO ***")
    print(f"Su saldo actual es: {saldonuevo}")



def depositar_dinero(saldonuevo):
    print("\n*** 2. DEPOSITAR DINERO ***")
    saldo = float(input("Ingrese el monto a depositar: "))
    if saldo < 0:
        print("Error. El monto no puede ser negativo")
        return saldonuevo
    else:
        saldonuevo = saldonuevo + saldo
        print(f"Usted ha depositado {saldo} ")
        return saldonuevo

def retirar_dinero(saldonuevo):
    print("\n*** 3. RETIRAR ***")
    retirar = float(input("Ingrese el monto a retirar: "))
    if retirar < 0:
        print("Error. El monto no puede ser negativo")
        return saldo
    elif retirar > saldo:
        print("Error. Saldo insuficiente")
        return saldo
    else:
        saldo -= retirar
        print(f"Usted ha retirado: {retirar}")
        return saldo

def main():
    opcion = 0
    saldonuevo = 0
    while opcion != 4:
        menu()
        opcion = leer_opcion()

        if opcion == 1:
            consultar_saldo(saldonuevo)
        elif opcion == 2:
            depositar_dinero(saldonuevo)
        elif opcion == 3:
            retirar_dinero(saldonuevo)
        else:
            print("\nGracias por utilizar Nequi")

main()