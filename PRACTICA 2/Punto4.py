email = str(input("Ingrese email= "))
validacion = True
#Contiene exactamente un @
if email.count("@") != 1:
    validacion = False
#tiene al menos un carácter antes del @.
if email.find("@") == 0:
    validacion=False


#Tiene al menos un punto (.) después del @.
for i in range(len(email)):
    if email[i] == "@":
        if email[i+1] != ".":
            validacion = False

#no empieza ni termina con @ ni con ..
if email.startswith("@") or email.startswith(".") or email.endswith("@") or email.endswith("."):
    validacion = False

#La parte después del último punto tiene al menos 2 caracteres (el dominio).
tope= email.rfind(".")
dominio= email[tope + 1:]
if len(dominio) < 2:
    validacion = False
    
print(validacion)
