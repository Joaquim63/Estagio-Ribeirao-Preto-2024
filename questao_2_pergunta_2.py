def fibonacci_sequence(n):
    sequence = [0, 1]
    while sequence[-1] < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

def is_in_sequence(n, sequence):
    return n in sequence

n = int(input("Digite um número: "))
sequence = fibonacci_sequence(n)

if is_in_sequence(n, sequence):
    print(f"O número {n} pertence à sequência de Fibonacci.")
else:
    print(f"O número {n} não pertence à sequência de Fibonacci.")
