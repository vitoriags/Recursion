int produto(int numero1, int numero2){
  // ponto de parada
  if (numero1 == numero2)
    return numero1;
  // recursividade
  return numero2 * produto(numero1, numero2 - 1);
}