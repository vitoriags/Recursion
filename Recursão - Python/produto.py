def produto(m: int, n: int) -> int:
  # caso de parada
  if m == n:
    return m
  
  # recursividade
  return n * produto(m, n - 1)

numero1 = input("")
numero1 = int(numero1)

numero2 = input("")
numero2 = int(numero2)

print(produto(numero1, numero2))
