def fatorial_duplo(numero: int) -> int:
  # ponto de parada
  if numero == 0:
    return 1
  if numero <= 2:
    return numero

  # recursividade
  return numero * fatorial_duplo(numero - 2)

numero = input('')
numero = int(numero)

print(fatorial_duplo(numero))
