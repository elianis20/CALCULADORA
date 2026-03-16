#=======================================================================
# CALCULADORA GEOMETRICA - GOE CALC
#=======================================================================

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

print("Bienvenido a GOE CALC")
mostrar_menu()

while True:
    opcion = input("\nElige una opcion: ").lower().strip()

    #------ CIRCULO ------
    if opcion == "1":
        print("\n--- CIRCULO ---")
        try:
            radio = float(input("Ingresa el radio: "))  # ✅ bien
            area = 3.1416 * radio ** 2
            perimetro = 2 * 3.1416 * radio
            print(".................")
            print("RESULTADOS:")
            print(f"  Area:      {area:.2f}")
            print(f"  Perimetro: {perimetro:.2f}")
            print(".................")
        except ValueError:
            print("inserte un dato válido")

    #------ RECTANGULO ------
    elif opcion == "2":
        print("\n--- RECTANGULO ---")
        try:
            base = float(input("Ingresa la base: "))        # ✅ faltaba input()
            altura = float(input("Ingresa la altura: "))    # ✅ faltaba input()
            area = base * altura
            perimetro = 2 * (base + altura)
            print(".................")
            print("RESULTADOS:")
            print(f"  Area:      {area:.2f}")
            print(f"  Perimetro: {perimetro:.2f}")
            print(".................")
        except ValueError:
            print("inserte un dato válido")

    #------ PENTAGONO ------
    elif opcion == "3":
        print("\n--- PENTAGONO ---")
        try:
            lado = float(input("Ingresa el lado: "))        # ✅ faltaba input()
            apotema = float(input("Ingresa la apotema: "))  # ✅ faltaba input()
            perimetro = 5 * lado
            area = (perimetro * apotema) / 2
            print(".................")
            print("RESULTADOS:")
            print(f"  Area:      {area:.2f}")
            print(f"  Perimetro: {perimetro:.2f}")
            print(".................")
        except ValueError:
            print("inserte un dato válido")

    #------ TRAPECIO ------
    elif opcion == "4":
        print("\n--- TRAPECIO ---")
        try:
            base_mayor = float(input("Ingresa la base mayor: "))  # ✅ faltaba input()
            base_menor = float(input("Ingresa la base menor: "))  # ✅ faltaba input()
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
        except ValueError:
            print("inserte un dato válido")

    #------ ESFERA ------
    elif opcion == "5":
        print("\n--- ESFERA ---")
        try:
            radio = float(input("Ingresa el radio: "))  # ✅ faltaba input()
            area = 4 * 3.1416 * radio ** 2
            volumen = (4/3) * 3.1416 * radio ** 3
            print(".................")
            print("RESULTADOS:")
            print(f"  Area sup.: {area:.2f}")
            print(f"  Volumen:   {volumen:.2f}")
            print(".................")
        except ValueError:
            print("inserte un dato válido")

    #------ CILINDRO ------
    elif opcion == "6":
        print("\n--- CILINDRO ---")
        try:
            radio = float(input("Ingresa el radio: "))    # ✅ faltaba input()
            altura = float(input("Ingresa la altura: "))  # ✅ faltaba input()
            area = 2 * 3.1416 * radio ** 2 + 2 * 3.1416 * radio * altura
            volumen = 3.1416 * radio ** 2 * altura
            print(".................")
            print("RESULTADOS:")
            print(f"  Area sup.: {area:.2f}")
            print(f"  Volumen:   {volumen:.2f}")
            print(".................")
        except ValueError:
            print("inserte un dato válido")

    #------ CONO ------
    elif opcion == "7":
        print("\n--- CONO ---")
        try:
            radio = float(input("Ingresa el radio: "))    # ✅ faltaba input()
            altura = float(input("Ingresa la altura: "))  # ✅ faltaba input()
            generatriz = (radio ** 2 + altura ** 2) ** 0.5
            area = 3.1416 * radio ** 2 + 3.1416 * radio * generatriz
            volumen = (1/3) * 3.1416 * radio ** 2 * altura
            print(".................")
            print("RESULTADOS:")
            print(f"  Generatriz:{generatriz:.2f}")
            print(f"  Area sup.: {area:.2f}")
            print(f"  Volumen:   {volumen:.2f}")
            print(".................")
        except ValueError:
            print("inserte un dato válido")

    #------ CUBO ------
    elif opcion == "8":
        print("\n--- CUBO ---")
        try:
            lado = float(input("Ingresa el lado: "))  # ✅ faltaba input()
            area = 6 * lado ** 2
            volumen = lado ** 3
            print(".................")
            print("RESULTADOS:")
            print(f"  Area sup.: {area:.2f}")
            print(f"  Volumen:   {volumen:.2f}")
            print(".................")
        except ValueError:
            print("inserte un dato válido")

    #------ TRIANGULO RECTANGULO ------
    elif opcion == "9":
        print("\n--- TRIANGULO RECTANGULO ---")
        try:
            cateto1 = float(input("Ingresa el cateto adyacente: "))       # ✅ faltaba input()
            cateto2 = float(input("Ingresa el cateto opuesto: "))         # ✅ faltaba input()
            angulo1 = float(input("Ingresa el angulo 1 (sin el 90): "))   # ✅ faltaba input()
            angulo2 = float(input("Ingresa el angulo 2 (sin el 90): "))   # ✅ faltaba input()
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
        except ValueError:
            print("inserte un dato válido")

    elif opcion == "m":
        mostrar_menu()

    elif opcion == "s":
        print("\nGracias por usar GOE CALC")
        print("Hasta luego!")
        break

    else:
        print("Opcion no valida, intenta de nuevo")