def converte_valor(valor):
    # Garante que o valor seja float
    numero = float(valor)
    # Formata com separador de milhar e vírgula decimal
    return f"{numero:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")