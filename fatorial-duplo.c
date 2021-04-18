int fatorialduplo(int numero){
  // ponto de parada
  if (numero == 0)
    return 1;
  if (numero <= 2)
    return numero;
  // recursividade
  return numero * fatorialduplo(numero - 2);
}