int fatorial(int numero){
  // ponto de parada
  if(numero == 0)
    return 1;
  if(numero <= 2)
    return numero;
  // recursividade
  int n = 1;
  for(int i = 1; i <= numero; i++)
      n  = n * i;
  return n;
}