print("=== MATRIZ 5x5 ===")

matriz = [[0 for _ in range(5)] for _ in range(5)]

print("Ingrese los 25 números:")
for i in range(5):
    for j in range(5):
        matriz[i][j] = int(input(f"Posición [{i}][{j}]: "))

print("\nMatriz ingresada:")
for i in range(5):
    for j in range(5):
        print(matriz[i][j], end="\t")
    print()