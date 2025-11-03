print("Introduce el precio del artículo")
precio = float(input())
print("Introduce el precio de venta real del artículo")
precioDescuento = float(input())
descuento = ((precio-precioDescuento)/precio)*100
print("Se ha realizado un descuento del ",descuento,"%")
