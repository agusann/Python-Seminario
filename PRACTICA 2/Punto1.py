text = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way
to do it.
Although that way may not be obvious at first unless you're
Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good
idea.
Namespaces are one honking great idea -- let's do more of
those!"""

lineas = text.split("\n")
print(lineas)
cantidad_lineas = len(lineas)
print("La cantidad total de lineas es ", cantidad_lineas)
cantidad_de_palabras=0
for linea in lineas:
    cantidad_de_palabras += len(linea.split())
print ("La cantidad de palabras es ", cantidad_de_palabras)
prom= cantidad_de_palabras/cantidad_lineas
print("El promedio de palabras por linea es ", prom)
mayor_prom = ""
for linea in lineas:
    if (len(linea.split()) > prom):
        mayor_prom += linea

print ("ACA VAN TODAS LAS LINEAS QUE SUPERAN EL PROMEDIO DE PALABRAS")
print (mayor_prom)

#Nose que hice mal, pero no me dio como en la practica