def potencia(base: int, expoente: int) -> int:
  # ponto de parada
  if expoente == 0:
    return 1;
  if expoente == 1:
    return base;

  # recursividade
  return base * potencia(base, expoente - 1)


base = input("")
base = int(base)
expoente = input("")
expoente = int(expoente)

print(potencia(base, expoente))