def calcular_media(numero1, numero2):
    return (numero1 + numero2) / 2


if __name__ == "__main__":
    try:
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        media = calcular_media(n1, n2)
        print(f"A média aritmética é: {media}")
    except ValueError:
        print("Por favor, digite apenas números válidos.")
