import Functions

continuar = "s"
print("Calculadora")

while continuar == "s":
    try:
        num1 = float(input("Digite um Número: "))
        op = input("Digite qual operação vai ser realizada: ")
        num2 = float(input("Digite o Segundo Número: "))
        if op == "+":
            Functions.Soma(num1,num2)
        elif op == "-":
            Functions.Subtracao(num1,num2)
        elif op == "/":
            Functions.Divisao(num1, num2)
        elif op == "*":
            Functions.Multiplicacao(num1,num2)
        else:
            print("Digite um operador logico valido (+ , - , / , *)")
        continuar = input("Deseja fazer outra operação? (s/n) : ")
    except ValueError:
        print("Digite um Valor Valido!")
    
    

