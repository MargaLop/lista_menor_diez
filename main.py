arr = [-22,2,9.002,8,53,0.66,777,'pera',43,2]

def no_errores(lista):

    if not(isinstance(lista, list)):
            return None
        
        
    else:
        
        def lista_de_cero_a_diez (lista):
            nueva_lista = []

            for numero in lista:
                if (isinstance(numero, int)) or (isinstance(numero, float)):
                    if numero <= 10:
                    
                        nueva_lista.append(numero)
            return nueva_lista

        return lista_de_cero_a_diez (lista)
 

print(no_errores(arr))




       