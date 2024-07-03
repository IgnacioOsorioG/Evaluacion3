import json
def registrar():
    puntFornite=0
    puntValorant=0
    puntfifa=0
    idjugador=input("Ingrese su id de jugador o nickname: ")
    nombre=input("ingrese su nombre: ")
    apellido=input("ingrese su apellido: ")
    print("Escriba el juego en que compite(Valorant, Fornite o Fifa)")
    flag=True  
    while flag:
        juego=input(">")
        if juego.upper()=="VALORANT" or juego.upper()=="FORNITE" or juego.upper()=="FIFA":
            if juego.upper()=="VALORANT":
                while True:
                    try:
                        puntValorant=int(input("ingrese su puntaje: "))
                        sino=input("Desea agregar otro juego (s/n): ")
                        if sino.upper()=="N":
                            flag=False
                        break
                    except:
                        print("El puntaje deben ser numeros")
            elif juego.upper()=="FORNITE":
                while True:
                    try:
                        puntFornite=int(input("ingrese su puntaje: "))
                        sino=input("Desea agregar otro juego (s/n): ")
                        if sino.upper()=="N":
                            flag=False
                        break
                    except:
                        print("El puntaje deben ser numeros")
            elif juego.upper()=="FIFA":
                while True:
                    try:
                        puntfifa=int(input("ingrese su puntaje: "))
                        sino=input("Desea agregar otro juego (s/n): ")
                        if sino.upper()=="N":
                            flag=False
                        break
                    except:
                        print("El puntaje deben ser numeros")
        else:
                print("juego no encontrado")
    while True:
        print("¿Qué tipo de jugador eres? (Principiante-Avanzado-Experto)")
        tipojugador=input(">")
        if tipojugador.upper()=="PRINCIPIANTE" or tipojugador.upper()=="AVANZADO" or tipojugador.upper()=="EXPERTO":
            break
        else:
            print("Opcion no valida")
    jugador={
        "id_jugador":idjugador,
        "Nombre_jugador":nombre+" "+apellido,
        "VALORANT":puntValorant,
        "FORNITE":puntFornite,
        "FIFA":puntfifa,
        "Tipo":tipojugador
    }
    print(jugador)
    return jugador
        
def listar():
    jugadores={}
    try:
        with open("jugadores.json","r") as file:
            jugadores=json.load(file)
        for fila in jugadores:
            if fila!="Tipo":
                print(fila,end=" ")
            else:
                print(fila)
        for fila in jugadores:
            if fila!="Tipo":
                print(jugadores[fila],end=" ")
            else:
                print(jugadores[fila])
    except:
        print("No hay jugadores registrados")


def menu():
    opc=0
    while opc!=4:
        print("**********Menú**********")
        print("1.-Registrar puntaje torneo")
        print("2.-Listar todos los puntajes")
        print("3.-Imprimir por tipo")
        print("4.-Salir del programa")
        while True:
            try:
                opc=int(input(">"))
                if opc<1 or opc>4:
                    print("Opcion no encontrada")
                else:
                    break
            except:
                print("opcion no valida")
        if opc==1:
            jugador=registrar()
            with open("jugadores.json","w") as file: #no logro que se cree un diccionario nuevo, en vez de eso se reemplaza
                json.dump(jugador,file)
        elif opc==2:
            listar()
        elif opc==3: #no recuendo como usar txt
            print("¿Qué tipo quieres buscar?(Principiante-Anavanzado-Experto)")
            tipo=input(">")
            if tipo.upper()=="PRINCIPIANTE" or tipo.upper()=="AVANZADO" or tipo.upper()=="EXPERTO":
                with open("jugadores.json","r") as archivo:
                    jugadores=json.load(archivo)
                if tipo.upper()=="PRINCIPIANTE":
                    with open("principiantes.txt","w") as file:
                        ""
                elif tipo.upper()=="AVANZADO":
                    with open("avanzados","w") as file:
                        ""
                elif tipo.upper()=="EXPERTO":
                    with open("expertos.txt","w") as file:
                        ""
            
        else:
            print("Saliendo del programa")
menu()