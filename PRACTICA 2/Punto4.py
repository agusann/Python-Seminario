email = str(input("Ingrese email= "))
validacion = True
if email.count("@") != 1:
    validacion = False

if email.find("@") == 0:
    validacion=False


for i in range(len(email)):
    if email[i] == "@":
        if email[i+1] != ".":
            validacion = False

if email.startswith("@") or email.startswith(".") or email.endswith("@") or email.endswith("."):
    validacion = False

tope= email.rfind(".")
dominio= email[tope + 1:]
if len(dominio) < 2:
    validacion = False
    
print(validacion)
