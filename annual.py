import numpy as np
import matplotlib.pyplot as plt

months = np.array(["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Nomviembre", "Diciembre"])
product_a = np.array([150, 200,250,300,220,210,180,190,230,240,280,300])
product_b = np.array([180, 210,230,250,270,260,240,250,270,290,310,330])
product_c = np.array([200, 220,240,260,280,300,320,340,360,380,400,420])

# Calcula el total de ventas por producto y por mes
total_sales_a = np.sum(product_a)
print("Total de ventas del producto A:", total_sales_a)

total_sales_b = np.sum(product_b)
print("Total de ventas del producto B:", total_sales_b)

total_sales_c = np.sum(product_c)
print("Total de ventas del producto C:", total_sales_c)

# Calcula el total de ventas por mes
total_sales_month = product_a + product_b + product_c
print("Total de ventas por mes:", total_sales_month)

# Calcula el promedio de ventas por mes
average_sales_month = np.mean(total_sales_month)
print("Promedio de ventas por mes:", average_sales_month)

# Encuentra el mes con las ventas más altas y más bajas
max_sales_month = np.max(total_sales_month)
print("Mes con las ventas más altas:", months[np.argmax(total_sales_month)], "con un total de:", max_sales_month, "USD")

min_sales_month = np.min(total_sales_month)
print("Mes con las ventas más bajas:", months[np.argmin(total_sales_month)], "con un total de:", min_sales_month, "USD")

# Calcula el producto más vendido en total
total_sales_products = np.array([total_sales_a, total_sales_b, total_sales_c])
best_selling_product = np.argmax(total_sales_products) + 1
if best_selling_product == 1:
    print("El producto más vendido anualmente es el producto A")
elif best_selling_product == 2:
    print("El producto más vendido anualmente es el producto B")
else:
    print("El producto más vendido anualmente es el producto C")

# Crea un gráfico de barras para visualizar las ventas mensuales por producto
plt.figure(figsize=(10, 6))
plt.bar(months, product_a, label='Producto A')
plt.title('Ventas mensual del producto A')
plt.xlabel('Meses')
plt.ylabel('Ventas (USD)')
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(10, 6))
plt.bar(months, product_b, label='Producto B')
plt.title('Ventas mensuales del producto B')
plt.xlabel('Meses')
plt.ylabel('Ventas (USD)')
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(10, 6))
plt.bar(months, product_c, label='Producto C')
plt.title('Ventas mensuales del producto C')
plt.xlabel('Meses')
plt.ylabel('Ventas (USD)')
plt.xticks(rotation=45)
plt.show()

# Crea un gráfico de líneas para visualizar las ventas mensuales totales
plt.figure(figsize=(10, 6))
plt.plot(months, total_sales_month, marker='o', linestyle='-', color='b')
plt.title('Ventas mensuales totales de los tres productos')
plt.xlabel('Meses')
plt.ylabel('Ventas (USD)')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Crea un gráfico de pastel para visualizar las ventas totales por producto
labels = ['Producto A', 'Producto B', 'Producto C']
sizes = [total_sales_a, total_sales_b, total_sales_c]
plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=['#ff9999', '#66b3ff', '#99ff99'])
plt.axis('equal')
plt.title('Distribución de ventas anuales por producto')
plt.show()

# Crea un gráfico de líneas múltiples para visualizar la relación entre las ventas de los productos A, B y C mes a mes durante un año
plt.figure(figsize=(10, 6))
plt.plot(months, product_a, marker='o', linestyle='-', color='r', label='Producto A')
plt.plot(months, product_b, marker='s', linestyle='--', color='g', label='Producto B')
plt.plot(months, product_c, marker='^', linestyle='-.', color='b', label='Producto C')
plt.title('Relación entre las ventas de los tres productos a lo largo del año')
plt.xlabel('Meses')
plt.ylabel('Ventas (USD)')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()