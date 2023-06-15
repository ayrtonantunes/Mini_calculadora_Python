print("Bem-vindo(a) a sua calculadora pessoal!")

opcao = int(input("Escolha uma das opções abaixo pelo seu número:\n1-Soma\n2-Subtração\n3-Multiplicação\n4-Divisão\nInsira o número: "))


def calculadora():
    if opcao == 1:
        print("Você escolheu 'Soma'")
        num1 = float(input("Insira o primeiro número: "))
        num2 = float(input("Insira o segundo número: "))
        soma = num1 + num2
        print(f"O resultado é igual a: {soma}")
    elif opcao == 2:
        print("Você escolheu 'Subtração'")
        num1 = float(input("Insira o primeiro número: "))
        num2 = float(input("Insira o segundo número: "))      
        sub = num1 - num2
        if num1 < num2:
            sub = num2 - num1
            print(f"O resultado é igual a: {sub}")
    elif opcao == 3:
        print("Você escolheu 'Multiplicação'")
        num1 = float(input("Insira o primeiro número: "))
        num2 = float(input("Insira o segundo número: "))      
        mult = num1 * num2
        print(f"O resultado é igual a: {mult}")
    elif opcao == 4:
        print("Você escolheu 'Divisão'")
        num1 = float(input("Insira o primeiro número: "))
        num2 = float(input("Insira o segundo número: "))
        div = num1 / num2
        if num1 < num2:
            div = num2 / num1
            print(f"O resultado é igual a: {div}")

calculadora()
