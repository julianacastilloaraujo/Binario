#Ejercicio en practica de clase tomado de parzibyte.me
def numero_decimal(decimal):
   if decimal <=0:
      return "0"
   bin = ""
   while decimal > 0:
      restante = int(decimal %2)
      decimal = int(decimal /2)
      bin = str(restante) + bin
   return bin
decimal = int(input("Dame un numero: "))
bin = numero_decimal(decimal)
print(f"El numero {decimal} es {bin} en binario")
