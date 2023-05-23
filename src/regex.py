import re
texto = "Inicio de Clases 8 de mayo de 2023" # texto donde buscar
patron = "(\d)+(\D)+(\d)+" # expresión regular que busca uno o más dígitos
coincidencia = re.search(patron, texto) # buscar el patrón en el texto
if coincidencia: # si hay una coincidencia
    resultado = coincidencia.group() # extraer la subcadena que coincide
    print(resultado)
else: # si no hay una coincidencia
    print("No se encontró el patrón")