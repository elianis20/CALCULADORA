#TITULO DE LA CALCULADORA "GOE CALC"

# INTERFAZ DE USUARIO
print("Bienvenido a GeoCalc: ")

#SELECION DE LA FIGURA 
def mostrar_menu():
                print("Selecciona la figura que deseas calcular: (2d o 3d) ")
                print(f"1. circulo:")
                print(f"2. rectangulo:")
                print(f"3. pentagono:")
                print(f"4. trapecio:")
                print(f"5. esfera:")
                print(f"6. cilindro:")
                print(f"7. cono:")
                print(f"8. cubo:")
                print(f"9. triangulorectangulo:")
                print("M. Mostrar menu de nuevo")
                print("S. Salir")

    # FUNCIONES ´PARA CALCULAR EL AREA Y EL VOLUMEN DE LAS FIGURAS 
mostrar_menu()
while True:
    opcion = input("ELIGE UNA OPCION: ").lower().strip()
    if opcion == "1":
        radio = float(input("Ingrese el radio del circulo: "))
        area_circulo =  3.1416 * radio ** 2
        print(f"El area del circulo es: {area_circulo:.2f}")
    elif opcion == "2":
        base = float(input("Ingrese la base del rectangulo: "))
        altura = float(input("Ingrese la altura del rectangulo: "))
        area_rectangulo = 2 * (base + altura)
        print(f"El area del rectangulo es: {area_rectangulo:.2f}")
    elif opcion == "3":
        lado = float(input("Ingrese el lado del pentagono: "))
        apotema = float(input("Ingrese la apotema del pentagono: "))
        area_pentagono = (5 * lado * apotema) / 2
        print(f"El area del pentagono es: {area_pentagono:.2f}")
    elif opcion == "4":
        base_mayor = float(input("Ingrese la base mayor del trapecio: "))
        base_menor = float(input("Ingrese la base menor del trapecio: "))
        altura_trapecio = float(input("Ingrese la altura del trapecio: "))
        lado1 = float(input("Igresa el lado izquierdo del trapecio: "))
        lado2 = float(input("Igresa el lado derecho del trapecio: "))
        area_trapecio = ((base_mayor + base_menor) / 2) * altura_trapecio
        print(f"El area del trapecio es: {area_trapecio:.2f}")
    elif opcion == "5":
        radio_esfera = float(input("Ingrese el radio de la esfera: "))
        volumen_esfera = (4/3) * 3.1416 * radio_esfera ** 3
        print(f"El volumen de la esfera es: {volumen_esfera:.2f}")
    elif opcion == "6":
        radio_cilindro = float(input("Ingrese el radio del cilindro: "))
        altura_cilindro = float(input("Ingrese la altura del cilindro: "))
        volumen_cilindro = 3.1416 * radio_cilindro ** 2 * altura_cilindro
        print(f"El volumen del cilindro es: {volumen_cilindro:.2f}")
    elif opcion == "7":
        radio_cono = float(input("Ingrese el radio del cono: "))
        altura_cono = float(input("Ingrese la altura del cono: "))
        volumen_cono = (1/3) * 3.1416 * radio_cono ** 2 * altura_cono
        print(f"El volumen del cono es: {volumen_cono:.2f}")
    elif opcion == "8":
        lado_cubo = float(input("Ingrese el lado del cubo: "))
        volumen_cubo = lado_cubo ** 3 
        print(f"El volumen del cubo es: {volumen_cubo:.2f}")
    elif opcion == "9":
        base_triangulo = float(input("Ingrese la base del triangulo rectangulo: "))
        altura_triangulo = float(input("Ingrese la altura del triangulo rectangulo: "))
        area_triangulo = (base_triangulo * altura_triangulo) / 2
        print(f"El area del triangulo rectangulo es: {area_triangulo:.2f}")
    elif opcion == "m":
        mostrar_menu()
    elif opcion == "s":
        print("Gracias por usar GeoCalc. ¡Hasta luego!")
    