def validar_numero(texto: str, base: str) -> tuple[bool, str]:
    """
    Valida que la entrada cumpla con las restricciones del proyecto:
    - No vacía, sin espacios ni signos[cite: 10]
    - Entero no negativo de hasta 128 dígitos[cite: 9]
    - Caracteres permitidos según la base seleccionada[cite: 10]
    """
    if not texto:
        return False, "Error: La entrada no puede estar vacía."[cite: 10]

    if " " in texto:
        return False, "Error: La entrada no debe contener espacios."[cite: 10]

    # Verificar presencia de signos o decimales
    if any(c in texto for c in ['+', '-', '.', ',']):
        return False, "Error: No se admiten signos (+/-) ni números fraccionarios."[cite: 10]

    # Límite máximo de 128 dígitos
    if len(texto) > 128:
        return False, "Error: La entrada no debe exceder los 128 dígitos."[cite: 9]

    # Caracteres válidos por base[cite: 10]
    digitos_validos = {
        '2': set("01"),
        '8': set("01234567"),
        '10': set("0123456789"),
        '16': set("0123456789ABCDEFabcdef")
    }

    if base not in digitos_validos:
        return False, f"Error: Base '{base}' desconocida."

    permitidos = digitos_validos[base]
    for caracter in texto:
        if caracter not in permitidos:
            return False, f"Error: El carácter '{caracter}' no es válido para la base {base}."[cite: 10]

    return True, ""