#Jorge_Hinostrosa_Paula
#paulajhinostrosa@ciencias.unam.mx

def InterseccionConjuntos(lista1):
  S = lista1[1]
  for i in range(len(lista1)-1):
    S = S & lista1[i+1]
  return S

def RelacionConjuntos(A,B):
  if A == B:
    return "Los conjuntos A y B son iguales."
  elif A >= B:
    return "El conjunto A contiene al conjunto B propiamente." 
  elif A <= B:
    return "El conjunto B contiene al conjunto A propiamente."
  elif len(A & B) == 0:
    return "Los conjuntos A y B son disjuntos."
  else: 
    return "Ni la intersección ni la diferencia simétrica de A y B son vacías."

def PosiblesCadenas(lista3):
  n = len(lista3)
  lista = []
  for i in range(n):
    for j in range(n):
      if i != j:
        lista.append(lista3[i] + lista3[j])
  cadenasposibles = set(lista)
  print(cadenasposibles)
  return(len(cadenasposibles))

s1={1,3,4,5,6}
s2={1,3,4,5,6}
s3={1,2,3,4,5,6}
s4={1,3,4,5,6,7,8}
s5={1,3,4,7,9}
s6={1,3,4,10}
s7={10}
l1=[s1,s2,s3,s4,s5,s6]
print(InterseccionConjuntos(l1))
print(PosiblesCadenas(["ab","b","ba","aa"]))
print(RelacionConjuntos(s1,s2))
print(RelacionConjuntos(s3,s1))
print(RelacionConjuntos(s1,s3))
print(RelacionConjuntos(s1,s7))
print(RelacionConjuntos(s1,s5))
