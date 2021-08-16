import math



op1 = input("Digite um valor: ")
op1 = float(op1)
print("OP1 é", op1)

operador = input("Digite o operador: ")
print("Operador é", operador)

if operador != "square root":
    
    op3 = input("Digite outro valor: ")
    op3 = float(op3)
    print("OP3 é", op3)

if operador == "-":
    print("O resultado será: ", op1 - op3)

elif operador == "+":
    print("O resultado vai ser: ", op1 + op3)

elif operador == "x":
    print("O resultado vai ser: ", op1 * op3)

elif operador == "/":
    print("O resultado vai ser: ", op1 / op3)

elif operador == "**":
    print("O resultado vai ser: ", op1 ** op3)

elif operador == "square root":
    print("O resultado vai ser: ", math.sqrt(op1))
