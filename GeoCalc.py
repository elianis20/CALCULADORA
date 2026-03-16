#====================================
# CALCULADORA GEOMETRICA - GOE CALC
#====================================

#esta funcion muestra el menu principal
def mostrar_menu():
    print("\n====================================")
    print("     CALCULADORA GEOMETRICA")
    print("          GOE CALC")
    print("====================================")
    print("  -- FIGURAS 2D --")
    print("  1. Circulo")
    print("  2. Rectangulo")
    print("  3. Pentagono")
    print("  4. Trapecio")
    print("  -- FIGURAS 3D --")
    print("  5. Esfera")
    print("  6. Cilindro")
    print("  7. Cono")
    print("  8. Cubo")
    print("  -- ESPECIAL --")
    print("  9. Triangulo Rectangulo")
    print("====================================")
    print("  M. Mostrar menu de nuevo")
    print("  S. Salir")
    print("====================================")

#mensaje de bienvenida
print("Bienvenido a GOE CALC")

#mostramos el menu al iniciar
mostrar_menu()

#bucle principal, se repite hasta que el usuario salga
while True:
    opcion = input("\nElige una opcion: ").lower().strip()

    #------ CIRCULO ------
    #formula area: PI * radio al cuadrado
    #formula perimetro: 2 * PI * radio
    if opcion == "1":
        print("\n--- CIRCULO ---")
        radio = float(input("Ingresa el radio: "))
        area = 3.1416 * radio ** 2
        perimetro = 2 * 3.1416 * radio
        print(".................")
        print("RESULTADOS:")
        print(f"  Area:      {area:.2f}")
        print(f"  Perimetro: {perimetro:.2f}")
        print(".................")

    #------ RECTANGULO ------
    #formula area: base por altura
    #formula perimetro: 2 por (base + altura)
    elif opcion == "2":
        print("\n--- RECTANGULO ---")
        base = float(input("Ingresa la base: "))
        altura = float(input("Ingresa la altura: "))
        area = base * altura
        perimetro = 2 * (base + altura)
        print(".................")
        print("RESULTADOS:")
        print(f"  Area:      {area:.2f}")
        print(f"  Perimetro: {perimetro:.2f}")
        print(".................")

    #------ PENTAGONO ------
    #formula perimetro: 5 * lado
    #formula area: (perimetro * apotema) / 2
    elif opcion == "3":
        print("\n--- PENTAGONO ---")
        lado = float(input("Ingresa el lado: "))
        apotema = float(input("Ingresa la apotema: "))
        perimetro = 5 * lado
        area = (perimetro * apotema) / 2
        print(".................")
        print("RESULTADOS:")
        print(f"  Area:      {area:.2f}")
        print(f"  Perimetro: {perimetro:.2f}")
        print(".................")

    #------ TRAPECIO ------
    #formula area: ((base mayor + base menor) / 2) * altura
    #formula perimetro: suma de los 4 lados
    elif opcion == "4":
        print("\n--- TRAPECIO ---")
        base_mayor = float(input("Ingresa la base mayor: "))
        base_menor = float(input("Ingresa la base menor: "))
        altura = float(input("Ingresa la altura: "))
        lado1 = float(input("Ingresa el lado izquierdo: "))
        lado2 = float(input("Ingresa el lado derecho: "))
        area = ((base_mayor + base_menor) / 2) * altura
        perimetro = base_mayor + base_menor + lado1 + lado2
        print(".................")
        print("RESULTADOS:")
        print(f"  Area:      {area:.2f}")
        print(f"  Perimetro: {perimetro:.2f}")
        print(".................")

    #------ ESFERA ------
    #formula area superficial: 4 * PI * radio al cuadrado
    #formula volumen: (4/3) * PI * radio al cubo
    elif opcion == "5":
        print("\n--- ESFERA ---")
        radio = float(input("Ingresa el radio: "))
        area = 4 * 3.1416 * radio ** 2
        volumen = (4/3) * 3.1416 * radio ** 3
        print(".................")
        print("RESULTADOS:")
        print(f"  Area sup.: {area:.2f}")
        print(f"  Volumen:   {volumen:.2f}")
        print(".................")

    #------ CILINDRO ------
    #formula area: 2 tapas + cuerpo lateral
    #formula volumen: PI * radio al cuadrado * altura
    elif opcion == "6":
        print("\n--- CILINDRO ---")
        radio = float(input("Ingresa el radio: "))
        altura = float(input("Ingresa la altura: "))
        area = 2 * 3.1416 * radio ** 2 + 2 * 3.1416 * radio * altura
        volumen = 3.1416 * radio ** 2 * altura
        print(".................")
        print("RESULTADOS:")
        print(f"  Area sup.: {area:.2f}")
        print(f"  Volumen:   {volumen:.2f}")
        print(".................")

    #------ CONO ------
    #primero calculamos la generatriz con pitagoras
    #formula area: PI*radio cuadrado + PI*radio*generatriz
    #formula volumen: (1/3) * PI * radio cuadrado * altura
    elif opcion == "7":
        print("\n--- CONO ---")
        radio = float(input("Ingresa el radio: "))
        altura = float(input("Ingresa la altura: "))
        generatriz = (radio ** 2 + altura ** 2) ** 0.5
        area = 3.1416 * radio ** 2 + 3.1416 * radio * generatriz
        volumen = (1/3) * 3.1416 * radio ** 2 * altura
        print(".................")
        print("RESULTADOS:")
        print(f"  Generatriz:{generatriz:.2f}")
        print(f"  Area sup.: {area:.2f}")
        print(f"  Volumen:   {volumen:.2f}")
        print(".................")

    #------ CUBO ------
    #formula area: 6 caras iguales = 6 * lado al cuadrado
    #formula volumen: lado al cubo
    elif opcion == "8":
        print("\n--- CUBO ---")
        lado = float(input("Ingresa el lado: "))
        area = 6 * lado ** 2
        volumen = lado ** 3
        print(".................")
        print("RESULTADOS:")
        print(f"  Area sup.: {area:.2f}")
        print(f"  Volumen:   {volumen:.2f}")
        print(".................")

    #------ TRIANGULO RECTANGULO ------
    #primero calculamos la hipotenusa con pitagoras
    #formula area: (cateto1 * cateto2) / 2
    #formula perimetro: cateto1 + cateto2 + hipotenusa
    #los 3 angulos siempre deben sumar 180
    elif opcion == "9":
        print("\n--- TRIANGULO RECTANGULO ---")
        cateto1 = float(input("Ingresa el cateto adyacente: "))
        cateto2 = float(input("Ingresa el cateto opuesto: "))
        angulo1 = float(input("Ingresa el angulo 1 (sin contar el 90): "))
        angulo2 = float(input("Ingresa el angulo 2 (sin contar el 90): "))
        #verificamos que los angulos sumen 180
        if angulo1 + angulo2 + 90 != 180:
            print("  ERROR: los angulos no suman 180")
        else:
            hipotenusa = (cateto1 ** 2 + cateto2 ** 2) ** 0.5
            area = (cateto1 * cateto2) / 2
            perimetro = cateto1 + cateto2 + hipotenusa
            print(".................")
            print("RESULTADOS:")
            print(f"  Hipotenusa:{hipotenusa:.2f}")
            print(f"  Area:      {area:.2f}")
            print(f"  Perimetro: {perimetro:.2f}")
            print(f"  Angulos: 90 + {angulo1} + {angulo2} = 180")
            print(".................")

    #si el usuario escribe m se muestra el menu de nuevo
    elif opcion == "m":
        mostrar_menu()

    #si el usuario escribe s sale del programa
    elif opcion == "s":
        print("\nGracias por usar GOE CALC")
        print("Hasta luego!")
        break

    #si escribe algo que no existe
    else:
        print("Opcion no valida, intenta de nuevo") 