NOMBRES_BASES = {
    '2': 'Binario',
    '8': 'Octal',
    '10': 'Decimal',
    '16': 'Hexadecimal'
}

class HistorialManager:
    def __init__(self):
        self.registros = []

    def agregar_registro(self, entrada: str, origen: str, destino: str, resultado: str):
        """Agrega una conversión válida realizada desde el menú al historial[cite: 7]."""
        self.registros.append({
            'entrada': entrada,
            'origen': NOMBRES_BASES.get(origen, origen),
            'destino': NOMBRES_BASES.get(destino, destino),
            'resultado': resultado
        })

    def mostrar_historial(self) -> bool:
        """
        Muestra en consola los registros numerados[cite: 8].
        Retorna True si hay registros, u informa y retorna False si está vacío[cite: 8].
        """
        if not self.registros:
            print("\nEl historial está vacío.")
            return False

        print("\n" + "=" * 40)
        print("HISTORIAL DE CONVERSIONES")
        print("=" * 40)
        for idx, reg in enumerate(self.registros, start=1):
            print(f"Registro {idx}")
            print(f"  Entrada: {reg['entrada']}")
            print(f"  Origen: {reg['origen']}")
            print(f"  Destino: {reg['destino']}")
            print(f"  Resultado: {reg['resultado']}")
            print("-" * 20)
        print(f"Total de registros: {len(self.registros)}")
        return True

    def eliminar_registro(self, indice: int) -> bool:
        """Elimina un registro seleccionado por su número tras validar el índice[cite: 8]."""
        if 1 <= indice <= len(self.registros):
            self.registros.pop(indice - 1)
            print(f"\n¡Registro {indice} eliminado exitosamente!")
            return True
        else:
            print("\nError: Número de registro inválido.")
            return False

    def vaciar_historial(self):
        """Vacía completamente la lista del historial[cite: 8]."""
        self.registros.clear()
        print("\n¡Historial vaciado correctamente!")