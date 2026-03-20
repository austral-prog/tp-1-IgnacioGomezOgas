def price():
    """
    Ejercicio 8 - Cálculo de Precio Final

    Dado un precio base, calcular e imprimir:
    1. El monto del impuesto (21%)
    2. El subtotal (precio base + impuesto)
    3. El monto de la propina (10% del subtotal)
    4. El precio final (subtotal + propina)
    """
    precio_base = 100

    monto_iva=precio_base*0.21
    print(monto_iva)
    subtotal=monto_iva+precio_base
    print(subtotal)
    monto_propina=.1*subtotal
    print(monto_propina)
    precio_final=subtotal+monto_propina
    print(precio_final)
price()