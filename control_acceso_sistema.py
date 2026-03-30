# VERIFICAR ACCESO AL SISTEMA CON OPERADORES LÓGICOS

USUARIO = "JUANBAEZ"
CONTRASEÑA = "JUAN123"

print("-----------------------------------------")
print("        -APP DE CONTROL DE ACCESO-")
print("-----------------------------------------")

# PEDIMOS EL NOMBRE
nombre_input = input("POR FAVOR, INGRESE SU NOMBRE: ")
NOMBRE = nombre_input.upper()

print("-----------------------------------------")

# PEDIMOS LA EDAD
print("DEBES TENER 18 AÑOS O MÁS PARA ACCEDER")
edad_input = input("INGRESE SU EDAD: ")
EDAD = int(edad_input)

print("-----------------------------------------")

# PEDIMOS USUARIO Y CONTRASEÑA
usuario_input = input("NOMBRE DE USUARIO: ").upper()
contra_input = input("INGRESE SU CONTRASEÑA: ").upper()

print("-----------------------------------------")

# VERIFICACIÓN
if (usuario_input == USUARIO) and (contra_input == CONTRASEÑA) and (EDAD >= 18):
    
    print("ACCESO PERMITIDO, BIENVENIDO", NOMBRE)
    input("PRESIONE ENTER PARA CONTINUAR")

else:
    
    print("ACCESO DENEGADO")
    input("PRESIONE ENTER PARA SALIR")
    exit()

# MENÚ
print("-----------------------------------------")
print("¿QUÉ OPERACIÓN DESEAS REALIZAR?")
print("1. CALCULADORA")
print("2. OPERADORES LÓGICOS")

opcion = input("INGRESE EL NUMERO DE OPCION: ")

if opcion == "1":
    import CALCUD_2

elif opcion == "2":
    import OP_LOGICOS

else:
    print("OPCIÓN NO VÁLIDA")
    input("PRESIONE ENTER PARA SALIR")
    exit()
