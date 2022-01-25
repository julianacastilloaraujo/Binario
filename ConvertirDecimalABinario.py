def ConvertirDecimalABinario():

   print('Hola este es un programa desarrollado en python')
   CD = int(input('Dame el número decimal que deseas convertir a binario'))
   B = ' '
   while (CD > 0) : 
   Operacion = str (CD % 2)
   B = Operacion + B
   CD = CD //2
   print(str(B))

   if __name__ == "__main__":
   
   ConvertirDecimalABinario
   
