# EXAMEN DE RECUPERACIÓN - UNIDAD 2

# IMPORTANTE:
# 1. La salida debe ser ÚNICAMENTE el resultado. No agregues texto extra.
# 2. No modifiques las condiciones del menú (if/elif).
# 3. Usa solo una función print() por ejercicio.

problema = int(input("Número del problema (1-10): "))

if problema == 1:
    # Problema 1: Área de un círculo con radio 15.
    # Fórmula: Area = 3.1416 * r^2
    r = 15
    # Tu código aquí
    area=3.1416*r^2
    print(area)

elif problema == 2:
    # Problema 2: Genera una clave de producto (concatenar) con código y lote.
    # Resultado esperado: "prod-88-loteb" (todo en minúsculas).
    codigo = 88
    lote = "LoteB"
    # Tu código aquí
    print(f'prod-{codigo}-{lote}')

elif problema == 3:
    # Problema 3: Verifica si el carácter '@' está en el correo dado.
    email = "usuario.upa.edu.mx"
    # Tu código aquí
    print('@' in email)

elif problema == 4:
    # Problema 4: Convierte todo el texto a MAYÚSCULAS.
    aviso = "el examen termina pronto"
    # Tu código aquí
    aviso.upper
    print(aviso)

elif problema == 5:
    # Problema 5: Convierte el string "150.50" a float y luego a entero.
    # Imprime ambos resultados en una sola línea.
    dato = "150.50"
    # Tu código aquí
    print(float(dato),int(float(dato)))

elif problema == 6:
    # Problema 6: Conversión de Temperatura (Celsius a Fahrenheit).
    # C=30. Fórmula: F = (C * 1.8) + 32
    celsius = 30
    # Tu código aquí
    F=(celsius*1.8)+32
    print(F)

elif problema == 7:
    # Problema 7: Extrae los primeros 5 caracteres de la cadena.
    frase = "Programación en Python"
    # Tu código aquí
    print(frase[:5])


elif problema == 8:
    # Problema 8: Calcula la Densidad de un objeto.
    # Masa: 500kg, Volumen: 2m^3. Fórmula: d = m / v
    m = 500

    # Tu código aquí
    v=2*m^3
    d=m/v


elif problema == 9:
    # Problema 9: Determina si un número es negativo.
    numero = -15
    # Tu código aquí
    if numero<0:
        print('numero')




elif problema == 10:
    # Problema 10: Calcula la Energía Potencial.
    # m=5kg, h=10m, g=9.81. Fórmula: Ep = m * g * h
    m = 5
    h = 10
    g = 9.81
    # Tu código aquí
    ep=m*g*h
    print(ep)
    

else:
    print("Ingresa un número entre 1 y 10.")