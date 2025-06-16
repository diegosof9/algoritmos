def ordenamiento_insercion(lista_numeros):

    for j in range(1, len(lista_numeros)):

        # print(lista_numeros[j])
        clave = lista_numeros[j]
        i = j - 1
        # print(i)

        while i >= 0 and lista_numeros[i] > clave:

            lista_numeros[i + 1] = lista_numeros[i]
            i = i - 1

        lista_numeros[i + 1] = clave

    return lista_numeros


lista_numeros = [200, 1, 1001, 34, 5, 1, 4]

print(ordenamiento_insercion(lista_numeros))