def calcular(a,b):
    while b:
        a, b = b , a % b
        return a
    breack

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

mcd =  calcular(num1, num2)

print(f"el mcd de {num1} y {num2} es: {mcd}")