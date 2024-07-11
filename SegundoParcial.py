#Segundo Parcial - PY-Market
#Crear un programa en Python que gestione una lista de productos la tienda PY-Market. El programa debe permitir:

#$Cargar los datos desde el archivo productos.csv

import csv

def leerArchivo(archivo):
    try:
        with open(archivo, 'r') as csvfile:
            reader = csv.reader(csvfile)
            for fila in reader:
                print(fila)
    except FileNotFoundError:
        print(f"Error: El archivo '{archivo}' no existe.")
    except csv.Error as e:
        print(f"Error al leer el archivo: {e}")
print("----------------------------------------------------------------------------------------------------------------------------------------")
leerArchivo('C:/Users/LEGION/Downloads/productos.csv')

#Calcular el precio promedio de los productos.

import csv

def calcularPromedio(archivo):
    try:
        with open(archivo, 'r') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            sumaPrecio = 0
            cantidadFilas = 0
            for row in reader:
                try:
                    precio = float(row[1])
                    sumaPrecio += precio
                    cantidadFilas += 1
                except ValueError:  
                    print(f"Error al leer el precio en la fila {cantidadFilas + 1}: {row[1]}")
                    continue

            if cantidadFilas == 0:
                raise Exception("El archivo CSV no contiene datos") 

            promedioPrecio = sumaPrecio / cantidadFilas
            return promedioPrecio

    except FileNotFoundError: 
        print(f"Error. El archivo '{archivo}' no se encontro.")
        return None

archivo = 'C:/Users/LEGION/Downloads/productos.csv'
promedio = calcularPromedio(archivo)
print("----------------------------------------------------------------------------------------------------------------------------------------")
print(f"El promedio del precio es de {promedio:.6f} pesos.")
print("----------------------------------------------------------------------------------------------------------------------------------------")

##Manejar excepciones al leer archivos.
#Utilizar funciones lambda para aplicar descuentos.

import csv

def calcularDescuento(archivo):
    try:
        with open(archivo, 'r') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            precio_con_descuento = lambda precio, descuento: precio - (precio * descuento / 100)

            for fila in reader:
                nombre_producto, precio, porcentaje_descuento = fila
                precio = float(precio)
                porcentaje_descuento = float(porcentaje_descuento)

                precioFinal = precio_con_descuento(precio, porcentaje_descuento)

                print(f"El producto {nombre_producto} tiene un precio de {precio:.2f} pesos y tiene un descuento del %{porcentaje_descuento:.2f}, por lo tanto su precio final es de {precioFinal:.2f} pesos.")
                print("----------------------------------------------------------------------------------------------------------------------------------------")
    except FileNotFoundError:
        print("Error: El archivo no existe.")
    except csv.Error as e:
        print(f"Error leyendo el archivo CSV: {e}")
    except ValueError as e:
        print(f"Error de valor: {e}")

calcularDescuento('C:/Users/LEGION/Downloads/productos.csv')

#Instrucciones:

#Implementa funciones para cargar los productos desde el archivo productos.csv.
#Implementa una función para calcular el precio promedio de los productos.
#Maneja excepciones al leer el archivo.
#Utiliza una función lambda para aplicar un descuento a los precios de los productos.