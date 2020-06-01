import sqlite3
import csv

fVentas = open('./sales.csv', 'r')
csvreader = csv.reader(fVentas, delimiter=',')
d = {}
i=1
for linea in csvreader:
	if i < len(linea):
		if linea[2] not in  d and linea[2] != 'tipo_producto':
			d[linea[2]] = {"precio_unitario":float(linea[9]), "coste_unitario":float(linea[10]),"id":i}
			i+=1
	


conn =sqlite3.connect('ventas.db')
print("Opened database successfully")
c = conn.cursor()
# Insert a row of data
for tipo_producto, precio_unitario in d.items():
	c.execute("INSERT INTO productos (id, tipo_producto, precio_unitario, costo_unitario) VALUES ('{}','{}', '{}','{}')".format( d[tipo_producto]["id"], tipo_producto, d[tipo_producto]["precio_unitario"], d[tipo_producto]["coste_unitario"]))
# Save (commit) the changes
conn.commit()
print("Records created successfully")
# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()





