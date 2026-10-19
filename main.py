from menus import flujo_conversion, flujo_historial, flujo_practica
from historial import HistorialManager
from practica import ModoPractica

def main():
    """
    Punto de entrada principal de la aplicación[cite: 10, 11].
    Inicializa los gestores de historial y práctica, y despliega el menú principal[cite: 5].
    """
    historial_mgr = HistorialManager()
    practica_mgr = ModoPractica()

    while True:
        print("\n" + "=" * 40)
        print("CONVERSOR DE SISTEMAS NUMÉRICOS")
        print("=" * 40)
        print("1. Realizar una conversión")
        print("2. Consultar el historial")
        print("3. Iniciar el modo de práctica")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ").strip()

        if opcion == '1':
            flujo_conversion(historial_mgr)
        elif opcion == '2':
            flujo_historial(historial_mgr)
        elif opcion == '3':
            flujo_practica(practica_mgr)
        elif opcion == '4':
            print("\n¡Gracias por utilizar el Conversor de Sistemas Numéricos! Hasta luego.")
            break
        else:
            print("\nError: Opción inválida. Ingrese un número del 1 al 4.")

if __name__ == "__main__":
    main()