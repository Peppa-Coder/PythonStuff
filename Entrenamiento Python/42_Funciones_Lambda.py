
# Funcion anonima que simplifica la sintaxis, donde el : es como el return de una funcion normal
area_triangulo = lambda base, altura:(base*altura)/2

print(area_triangulo(7,5))


# pow(base, exponente) 
# al_cubo = lambda numero:numero**3
al_cubo = lambda numero:pow(numero, 3)

print(al_cubo(5))\


destacar_valor = lambda comision:'~ ${}!'.format(comision)

comision = 15600

print(destacar_valor(comision))