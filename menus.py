from validaciones import validar_numero
from conversiones import convertir_numero, NOMBRES_BASES
from historial import HistorialManager
from practica import ModoPractica

MAPA_BASES = {
    '1': '2',
    '2': '8',
    '3': '10',
    '4': '16'
}

def seleccionar_base(titulo: str) -> str | None:
    """Muestra el menú de selección de base de origen/destino y retorna la base o None si decide volver[cite: 6]."""
    while True:
        print("\n" + "=" * 40)
        print(titulo)
        print("=" * 40)
        print("1. Binario")
        print("2. Octal")
        print("3. Decimal")
        print("4. Hexadecimal")
        print("0. Volver al menú principal")
        
        opcion = input("Seleccione una opción: ").strip()
        if opcion == '0':
            return None
        elif opcion in MAPA_BASES:
            return MAPA_BASES[opcion]
        else:
            print("\nError: Opción inválida. Seleccione un número de la lista.")

def flujo_conversion(historial_mgr: HistorialManager):
    """Maneja la selección de bases, la validación de la entrada, la conversión y el historial[cite: 6, 7]."""
    base_origen = seleccionar_base("SELECCIONE LA BASE DE ORIGEN")
    if not base_origen:
        return

    base_destino = seleccionar_base("SELECCIONE LA BASE DE DESTINO")
    if not base_destino:
        return

    # No se permite la misma base como origen y destino[cite: 6]
    if base_origen == base_destino:
        print("\nError: La base de origen y la base de destino no pueden ser iguales.")
        input("Presione Enter para continuar...")
        return

    nombre_origen = NOMBRES_BASES[base_origen]
    nombre_destino = NOMBRES_BASES[base_destino]

    print("\n" + "=" * 40)
    print(f"CONVERSIÓN: {nombre_origen.upper()} A {nombre_destino.upper()}")
    print("=" * 40)
    print("Ingrese un entero no negativo de hasta 128 dígitos.")
    print("Escriba 'volver' para regresar al menú principal.")

    while True:
        entrada = input("Número a convertir: ").strip()
        if entrada.lower() == 'volver':
            return

        es_valido, msj_error = validar_numero(entrada, base_origen)
        if not es_valido:
            print(msj_error)
            continue

        # Realizar conversión y generar procedimiento paso a paso[cite: 6]
        resultado, pasos = convertir_numero(entrada, base_origen, base_destino)

        print("\n" + "=" * 40)
        print("RESULTADO")
        print("=" * 40)
        print(f"Número ingresado: {entrada}")
        print(f"Base de origen: {nombre_origen}")
        print(f"Base de destino: {nombre_destino}")
        print(f"Resultado: {resultado}")
        print("\nPROCEDIMIENTO PASO A PASO")
        print("-" * 40)
        for paso in pasos:
            print(paso)
        
        # Registrar conversión en el historial[cite: 7]
        historial_mgr.agregar_registro(entrada, base_origen, base_destino, resultado)
        print("\nConversión agregada al historial.")
        input("Presione Enter para continuar...")
        break

def flujo_historial(historial_mgr: HistorialManager):
    """Maneja la visualización y operaciones sobre el historial[cite: 8]."""
    while True:
        tiene_registros = historial_mgr.mostrar_historial()
        if not tiene_registros:
            input("Presione Enter para continuar...")
            break

        print("\n1. Eliminar un registro")
        print("2. Vaciar historial")
        print("3. Volver al menú principal")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == '1':
            idx_str = input("Ingrese el número de registro a eliminar: ").strip()
            if idx_str.isdigit():
                historial_mgr.eliminar_registro(int(idx_str))
            else:
                print("\nError: Debe ingresar un número entero válido.")
            input("Presione Enter para continuar...")
        elif opcion == '2':
            historial_mgr.vaciar_historial()
            input("Presione Enter para continuar...")
            break
        elif opcion == '3':
            break
        else:
            print("\nError: Opción inválida.")

def flujo_practica(practica_mgr: ModoPractica):
    """Maneja la interfaz del modo de práctica[cite: 8, 9]."""
    while True:
        print("\n" + "=" * 40)
        print("MODO DE PRÁCTICA")
        print("=" * 40)
        practica_mgr.mostrar_resumen()
        print("\n1. Resolver un nuevo ejercicio")
        print("2. Reiniciar puntuación")
        print("3. Volver al menú principal")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == '1':
            practica_mgr.generar_ejercicio()
            input("Presione Enter para continuar...")
        elif opcion == '2':
            practica_mgr.reiniciar_puntuacion()
            input("Presione Enter para continuar...")
        elif opcion == '3':
            break
        else:
            print("\nError: Opción inválida.")