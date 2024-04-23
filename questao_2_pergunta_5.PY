def invert_string(s):
    inverted = ''
    for char in s:
        inverted = char + inverted
    return inverted

s = "Estagio"  # Substitua "Estagio" pela string que você deseja inverter
print("String invertida: ", invert_string(s))
