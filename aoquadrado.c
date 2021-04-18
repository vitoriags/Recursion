int aoquadrado(int numero, int n){
  // ponto de parada
  if (n * n > numero)
    return n - 1;
  // recursividade
  return aoquadrado(numero, n + 1);
}