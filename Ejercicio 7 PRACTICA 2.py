cadena = input('Ingrese un string ')

cadenaInvertida = cadena[::-1] #invertimos la cadena

if (cadena == cadenaInvertida):
    print('la palabra ingresada es palindrome')
else:
    print('La palabra ingrtesada no es palindrome')        