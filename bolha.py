lista=[7,3,4,1,8,5]

def bubble_sort(lista):
    n=len(lista)
    for j in range (n-1):
        for i in range (n-1):
          if lista[i] > lista [i+1]:
         #troca acontece 
            lista[i], lista [i+1]=lista [i+1], lista [i]
    return lista
    

#Este código agora esta completo
Mostrar_Lista=bubble_sort(lista)
print(Mostrar_Lista)
