import random
from validaciones import validar_numero
from conversiones import convertir_numero

BASES = ['2', '8', '10', '16']
NOMBRES_BASES = {
    '2': 'Binario',
    '8': 'Octal',
    '10': 'Decimal',
    '16': 'Hexadecimal'
}

class ModoPractica:
    def __init__(self):
        self.aciertos = 0
        self.respondidos = 0

    def reiniciar_puntuacion(self):
        """Reinicia la cantidad de aciertos y ejercicios respondidos[cite: 9]."""
        self.aciertos = 0
        self.respondidos = 0
        print("\n¡Puntuación reiniciada exitosamente!")

    def mostrar_resumen(self):
        """Muestra aciertos, respondidos y el porcentaje exacto de aciertos[cite: 9]."""
        porcentaje = (self.aciertos / self.respondidos * 100) if self.respondidos > 0 else 0.0
        print(f"\nAciertos: {self.aciertos}")
        print(f"Ejercicios respondidos: {self.respondidos}")
        print(f"Porcentaje de aciertos: {porcentaje:.1f}%")

    def generar_ejercicio(self):
        """Genera un ejercicio aleatorio de conversión entre 0 y 255 y evalúa la respuesta[cite: 8, 9]."""
        val_dec = random.randint(0, 255)[cite: 8]
        
        # Seleccionar bases distintas para origen y destino[cite: 6]
        origen = random.choice(BASES)
        destino = random.choice([b for b in BASES if b != origen])

        # Calcular representación inicial y respuesta esperada
        val_origen, _ = convertir_numero(str(val_dec), '10', origen)
        val_esperado, _ = convertir_numero(str(val_dec), '10', destino)

        print("\n" + "=" * 40)
        print("EJERCICIO DE PRÁCTICA")
        print("=" * 40)
        print(f"Convierta {val_origen} de {NOMBRES_BASES[origen]} a {NOMBRES_BASES[destino]}.")
        print("Ingrese únicamente el número de la respuesta.")

        while True:
            respuesta = input("Su respuesta: ").strip()
            valida, msj_err = validar_numero(respuesta, destino)
            
            # Formato inválido no penaliza la puntuación[cite: 9]
            if not valida:
                print(msj_err)
                print("Intente nuevamente (esta entrada no afecta su puntuación).")
                continue

            # Comparación insensible a mayúsculas/minúsculas para hexadecimal
            if respuesta.upper() == val_esperado.upper():
                print("\n¡Respuesta correcta!")
                self.aciertos += 1
            else:
                print(f"\nRespuesta incorrecta. La respuesta esperada era: {val_esperado}")
            
            self.respondidos += 1
            self.mostrar_resumen()
            break