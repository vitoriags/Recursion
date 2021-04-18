int potencia(int base, int expoente){
  // ponto de parada
  if (expoente == 1)
    return base;
  if (expoente == 0)
    return 1;
  // recursividade
  return base * potencia(base, expoente - 1);
}