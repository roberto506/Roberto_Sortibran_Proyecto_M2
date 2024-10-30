print("=====================")
print("Generador de contraseñas")
print("=====================")
#Crear un programa que genera una contraseña de 8 caracteres con 3 palabras que asigne el usuario
#se declaran tres variables
palabra1 = input ("Introduce la primer palabra: " )
palabra2 = input ("Introduce la segunda palabra: ") 
palabra3 = input ("Introduce la tercer palabra: ")
 
#se utiliza la sentencia condicional  "if" y "len"
#el signo " + " realiza una concadenacion
if len(palabra1) < 2 :
    palabra1 =  "x"  +  palabra1
if len(palabra2) < 2 :
    palabra2 =  "x"  +  palabra2
if len(palabra3) < 2 :
    palabra3 =  "x"  +  palabra3
 
#Se genera la contraseña / se declara la variable contraseña y se realiza concadenacion
contraseña = palabra1[0] +  palabra2[0] + palabra3[0] + palabra1[1] +palabra2[1] +palabra3[1]
print("La contraseña es: " , contraseña ) 
#Se solicita ingrese la contraseña al usuario 
#Se utiliza la sentencia  condicional multiple que son "if"  ,"elif" y "else"
contraseña_usuario = input("Introduce la contraseña:  ")

if len(contraseña_usuario ) < len(contraseña) :
        print("Faltan" , len(contraseña ) - len(contraseña_usuario ) , "caracteres ")
elif len(contraseña_usuario) > len(contraseña) :
            print("Sobran" , len(contraseña_usuario ) -  len(contraseña ) , "caracteres " )
elif contraseña_usuario == contraseña:
             print("contraseña correcta")
               
else:
            print("contraseña incorrecta")
        
        
            
              
        
 
 
    
   
