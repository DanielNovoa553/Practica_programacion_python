from funciones import conversor

menu = """
 💰 Bienvenidos al conversor de monedas 💰
    
    1 - Pesos Colombainos
    2 - Pesos Argentinos
    3 - Pesos Mexicanos
    
  Elige una opcion : """

opcion = int(input(menu))

if opcion == 1:
    conversor("colombianos", 3875)

elif opcion == 2:
    conversor("argentinos", 65)

elif opcion == 3:
    conversor("mexicanos", 20)

else:
    print("Ingresa una opcion correcta por favor")
