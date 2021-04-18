def fatorial(n: int) -> int:
  if n == 0:
    return 1
  if n <= 2:
    return n
  
  indice = 1;
  numero = 1;
  
  while (indice <= n):
    numero = numero * indice
    indice += 1
  return numero


numero = input("")
numero = int(numero)

print(fatorial(numero))
