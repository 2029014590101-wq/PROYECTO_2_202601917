# Diccionarios auxiliares para conversión de dígitos hexadecimales
VALORES_HEX = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
    '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
    'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15
}

SIMBOLOS_HEX = {
    0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
    5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
    10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'
}

NOMBRES_BASES = {
    '2': 'Binario',
    '8': 'Octal',
    '10': 'Decimal',
    '16': 'Hexadecimal'
}

def a_decimal(texto: str, base_origen: int) -> tuple[int, list[str]]:
    """
    Convierte un número desde cualquier base a decimal utilizando el
    algoritmo de notación posicional sin usar int(texto, base)[cite: 6, 11].
    """
    pasos = []
    acumulado = 0
    
    if base_origen == 10:
        for char in texto:
            acumulado = acumulado * 10 + VALORES_HEX[char]
        return acumulado, pasos

    pasos.append(f"ETAPA: {NOMBRES_BASES[str(base_origen)].upper()} A DECIMAL")
    
    # Notación posicional de derecha a izquierda
    for idx, char in enumerate(reversed(texto)):
        val_digito = VALORES_HEX[char]
        aporte = val_digito * (base_origen ** idx)
        acumulado += aporte
        
        if base_origen == 16 and val_digito >= 10:
            pasos.append(f"{char.upper()} (valor {val_digito}) x {base_origen}^{idx} = {aporte}")
        else:
            pasos.append(f"{char.upper()} x {base_origen}^{idx} = {aporte}")
            
    pasos.append(f"Suma de los aportes: {acumulado}")
    return acumulado, pasos

def desde_decimal(valor_decimal: int, base_destino: int) -> tuple[str, list[str]]:
    """
    Convierte un entero decimal a cualquier base utilizando el
    algoritmo de divisiones sucesivas sin usar bin(), oct() o hex()[cite: 6, 11].
    """
    pasos = []
    if base_destino == 10:
        return str(valor_decimal), pasos

    pasos.append(f"ETAPA: DECIMAL A {NOMBRES_BASES[str(base_destino)].upper()}")
    
    if valor_decimal == 0:
        pasos.append(f"0 / {base_destino}: cociente = 0, residuo = 0, dígito = 0")
        pasos.append("Resultado final: 0")
        return "0", pasos

    residuos = []
    actual = valor_decimal
    
    while actual > 0:
        cociente = actual // base_destino
        residuo = actual % base_destino
        digito = SIMBOLOS_HEX[residuo]
        residuos.append(digito)
        pasos.append(f"{actual} / {base_destino}: cociente = {cociente}, residuo = {residuo}, dígito = {digito}")
        actual = cociente

    residuos.reverse()
    resultado = "".join(residuos)
    pasos.append(f"Leer los residuos del último al primero: {resultado}")
    return resultado, pasos

def convertir_numero(texto: str, base_origen: str, base_destino: str) -> tuple[str, list[str]]:
    """
    Realiza la conversión utilizando decimal como base intermedia cuando corresponda[cite: 6, 12].
    """
    origen = int(base_origen)
    destino = int(base_destino)
    pasos_totales = []

    val_decimal, pasos_dec = a_decimal(texto, origen)
    pasos_totales.extend(pasos_dec)

    resultado_final, pasos_dest = desde_decimal(val_decimal, destino)
    pasos_totales.extend(pasos_dest)

    return resultado_final, pasos_totales