def aoquadrado(numero: int, n: int) -> int:
  # ponto de parada
  if (n * n > numero):
    return n - 1
  
  # recursividade
  return aoquadrado(numero, n + 1)


numero = input("")
numero = int(numero)
print(aoquadrado(numero, 1))
