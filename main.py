while True:
  print ("digite o valor de M")
  m = int(input())
  print ("digite o valor de N")
  n = int(input())
  if m >= n:
      print("Valor de M chegou ao valor de N")
  else:
      cont = m
      while m < n:
        m += 1
        cont += m
        if m >= n:
          break
      print ("O resultado é", cont)