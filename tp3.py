#Ejercicio 1— “Caja del Kiosco”

nombre = ""

while not nombre.strip().isalpha():
   nombre = input("Por favor, ingrese su nombre de cliente: ")
   if not nombre.strip().isalpha():
      print("El nombre no puede estar vacio ni numeros, ¡intente de nuevo!")

nombre_correcto = nombre.strip().capitalize()

cantidad = 0

while True:
   numero = input("Ingrese la cantidad de productos a comprar: ")
   if numero.isdigit():
      cantidad = int(numero)
      if cantidad > 0:
         break
      else: 
         print("El numero a ingresar debe ser mayor a 0. Por favor, ¡intente de nuevo!")
   else: 
      print("Por favor, ingrese un numero entero.")

total_sin_descuento = 0
total_con_descuento = 0

for i in range(1, cantidad + 1):
   precio = ""
   while not precio.isdigit():
      precio = input(f"Producto {i} - Precio: ")
      if not precio.isdigit():
         print("Por favor, ingrese un precio valido.")

   precio_valido = int(precio)
   total_sin_descuento += precio_valido

   descuento = ""
   while descuento not in ["s", "n"]:
      descuento = input(f"Producto {i} - ¿Tiene desceunto? (S/N): ").strip().lower()
      if descuento not in ["s", "n"]:
        print("Por favor, responda con 'S' para Si o 'N' para No.")

   if descuento == "s":
      precio_total = precio_valido*0.90
   else:
      precio_total = precio_valido

   total_con_descuento += precio_total

ahorro = total_sin_descuento - total_con_descuento
promedio = total_con_descuento / cantidad

print("\n" + "=" * 30)
print(f"Cliente: {nombre_correcto.strip()}")
print(f"Cantidad de productos: {cantidad}")
print("-" * 30)
print(f"Total sin descuento: ${total_sin_descuento}")
print(f"Total con descuento: ${total_con_descuento:.2f}")
print(f"Ahorro: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")
print("=" * 30)


#Ejercicio 2 — “Acceso al Campus y Menú Seguro”

usuario_correcto = "alumno"
clave_correcta = "python123"

intentos = 0
intentos_max = 3
acceso = False

while intentos < intentos_max:
   print(f"Intento {intentos + 1} / 3")
   usuario = input("Usuario: ")
   clave = input("Clave: ")

   if usuario == usuario_correcto and clave == clave_correcta:
      print("Acceso concedido.")
      acceso = True
      break
   else: 
      print("Error: Credenciales no validas.")
      intentos += 1
    
if not acceso:
   print("Cuenta bloqueada.")
else:
   while True:
      print("\n1) Estado  2) Cambiar clave  3) Mensaje  4) Salir")
      opcion = input("Opcion: ")

      if not opcion.isdigit():
         print("Error: Ingrese un numero valido.")
         continue
      
      opcion = int(opcion)

      if opcion < 1 or opcion > 4 :
         print("Error: Opcion fuera de rango.")
         continue
      
      if opcion == 1:
         print("Estado: Inscripto.")

      elif opcion == 2:
         nueva_clave = input("Ingrese su nueva clave: ")
        
         if len (nueva_clave) < 6 :
            print("Error: Minimo 6 caracteres.")
            continue
         
         confirmar = input("Confirme la nueva clave: ")

         if nueva_clave == confirmar:
            clave_correcta == nueva_clave
            print("Clave cambiada correctamente.")
         else:
            print("Error: Las claves no coinciden.")

      elif opcion == 3:
         print("¡No te rindas, vas a lograrlo!")
      elif opcion == 4:
         print("Saliendo...")
         break
         
#Ejercicio 3 (Alta) — “Agenda de Turnos con Nombres (sin listas)”

nombre = input("Operador: ")

while not nombre.isalpha():
   print("Error.")
   nombre = input("Operador: ")

lunes_t1 = ""
lunes_t2= ""
lunes_t3 = ""
lunes_t4 = ""

martes_t1 = ""
martes_t2 = ""
martes_t3 = ""

while True: 
   print("\n 1 Reservar turno.")
   print("\n 2 Cancelar turno.")
   print("\n 3 Ver agenda del dia.")
   print("\n 4 Resumen general.")
   print("\n 5 Cerrar sistema.")

   opcion = input("Opcion: ")


   if not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 5:
      print("Opcion invalida, intente de nuevo.")
      continue

   elif opcion == "5":
      break

   elif opcion == "1":
      dia = input("1=Lunes  2=Martes ")
      
      if dia != "1" and dia != "2":
         print("Dia invalido:")
         continue

      nombre_paciente = input("Paciente: ")
      while not nombre_paciente.isalpha():
         nombre_paciente = input("Paciente: ")

      nombre_paciente = nombre_paciente.capitalize()
      
      if dia == "1":
         if nombre_paciente == lunes_t1 or nombre_paciente == lunes_t2 or nombre_paciente == lunes_t3 or nombre_paciente == lunes_t4:
            print("Repetido.")

         if lunes_t1 == "":
            lunes_t1 = nombre_paciente
         elif lunes_t2 == "":
            lunes_t2 = nombre_paciente
         elif lunes_t3 == "": 
            lunes_t3 = nombre_paciente
         elif lunes_t4 == "":
            lunes_t4 = nombre_paciente
         else:
            print("No hay turnos disponibles.")

      else:
         if nombre_paciente == martes_t1 or nombre_paciente == martes_t2 or nombre_paciente == martes_t3:
            print("Repetido.")
         elif martes_t1 == "":
            martes_t1 = nombre_paciente
         elif martes_t2 == "":
            martes_t2 = nombre_paciente
         elif martes_t3 == "":
            martes_t3 = nombre_paciente
         else:
            print("No hay turnos disponibles.")

   elif opcion == "2":
      dia = input("1=Lunes  2=Martes ")
      nombre_paciente = input("Cancelar turno: ").capitalize()

      if dia == "1": 
         
         if lunes_t1 == nombre_paciente: lunes_t1 = ""
         elif lunes_t2 == nombre_paciente: lunes_t2 = "" 
         elif lunes_t3 == nombre_paciente: lunes_t3 = ""
         elif lunes_t4 == nombre_paciente: lunes_t4 = ""
      elif dia == "2":
         if martes_t1 == nombre_paciente: martes_t1 = ""
         elif martes_t2 == nombre_paciente: martes_t2 = ""
         elif martes_t3 == nombre_correcto: martes_t3 = ""

   elif opcion == "3":
      
      dia = input("1 Lunes  2 Martes: ")

      if dia == "1":
         print("\n --- LUNES ---")
         print("Turno 1:", lunes_t1 if lunes_t1 != "" else "libre.")
         print("Turno 2:", lunes_t2 if lunes_t2 != "" else "libre.")
         print("Turno 3:", lunes_t3 if lunes_t3 != "" else "libre.")
         print("Turno 4:", lunes_t4 if lunes_t4 != "" else "libre.")
      elif dia == "2":
         print("\n --- MARTES ---")
         print("Turno 1:", martes_t1 if martes_t1 != "" else "libre.")
         print("Turno 2:", martes_t2 if martes_t2 != "" else "libre.")
         print("Turno 3:", martes_t3 if martes_t3 != "" else "libre.")

   elif opcion == "4":
      
      lunes_ocupado = 0
      if lunes_t1 != "": lunes_ocupado += 1
      if lunes_t2 != "": lunes_ocupado += 1
      if lunes_t3 != "": lunes_ocupado += 1
      if lunes_t4 != "": lunes_ocupado += 1

      martes_ocupado = 0
      if martes_t1 != "": martes_ocupado += 1
      if martes_t2 != "": martes_t2 += 1
      if martes_t3 != "": martes_ocupado += 1

      lunes_disponibles = 4 - lunes_ocupado
      martes_disponibles = 3 - martes_ocupado

      print("\n --- RESUMEN ---")

      print("Lunes -> Ocupados: ", lunes_ocupado, "| Libres: ", lunes_disponibles)
      print("Martes -> Ocupados: ", martes_ocupado, "| Libres: ", martes_disponibles)

      if lunes_ocupado > martes_ocupado:
         print("Dia con mas turnos: Lunes.")
      elif martes_ocupado > lunes_ocupado:
         print("Dia con mas turnos: Martes.")
      else:
         print("Empate.")

      print("Lunes:", lunes_ocupado)
      print("Martes:", martes_ocupado)

#Ejercicio 4 — “Escape Room: La Bóveda”

nombre = input("Nombre: ")
while not nombre.isalpha():
    nombre = input("Nombre: ")

energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""

racha = 0

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:
    
    if alarma and tiempo <= 3:
       print("\n Sistema bloqueado por alarma.")
       break

    print("\nEnergia:", energia, "Tiempo:", tiempo, "Cerraduras:", cerraduras_abiertas)
    print("Alarma: ", alarma)
    print("Codigo parcial: ", codigo_parcial)

    print("1 Forzar cerradura.")
    print("2 Hackear panel.")
    print("3 Descansar")

    opciones = input("Opcion: ")

    if not opciones.isdigit() or int(opciones) < 1 or int(opciones) > 3:
        print("Error")
        continue

    if opciones == "1":
        energia -= 20
        tiempo -= 2

        if racha == 3:
         alarma = True
         print("La cerradura se trabo! Se activo la alarma.")

        else: 
         if energia < 40:
           numero = input("¡Riesgo! Elegi un numero del 1-3: ")
           while not numero.isdigit() or int(numero) < 1 or int(numero) > 3:
              numero = input("Elegi un numero del 1-3: ")

           if numero == "3": 
              alarma = True
              print("Se activo la alarma.")

         if not alarma:
            cerraduras_abiertas += 1
            print("Abriste una cerradura.")

    elif opciones == "2":
        racha = 0

        energia -= 10
        tiempo -= 3

        print("Hackeando...")

        for i in range(4): 
           print("Paso", i+1)
           codigo_parcial += "A"

        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
           cerraduras_abiertas += 1
           print("El codigo abrio una cerradura.")

    elif opciones == "3":
        racha = 0 

        energia += 15
        if energia > 100:
            energia = 100

        tiempo -= 1

        if alarma:
            energia -= 10
            print("La alarma te quita energia extra.")

if cerraduras_abiertas == 3:
    print("\n GANASTE")
else:
    print("\n PERDISTE")


#Ejercicio 5 — “Escape Room:"La Arena del Gladiador"

nombre = input("Nombre del Gladiador: ")
while not nombre.isalpha():
    print("Error, solo se permiten letras.")
    nombre = input("Nombre del Gladiador: ")

vida_jugador = 100
vida_enemigo = 100
pociones = 3

daño_base = 15
daño_enemigo = 12

turno_jugador = True

print("--- BIENVENIDO A LA ARENA ---")
print("=== INICIO DEL COMBATE ===")

while vida_jugador > 0 and vida_enemigo > 0:
   print("--- NUEVO TURNO ---")
   print(nombre, "(HP:", vida_jugador, ") vs Enemigo (HP:", vida_enemigo, ") | Pociones:", pociones)

   print("Elige una opcion: ")
   print("1 Ataque pesado.")
   print("2 Rafaga veloz.")
   print("3 Curar.")

   opcion_escape = input("Opcion: ")
 
   if opcion_escape == "1":
      if vida_enemigo < 20:
         daño = daño_base * 1.5
         print("¡Golpe critico!")
      else:
         daño = daño_base
      
      vida_enemigo -= 5
      print("¡Atacaste al enemigo por", daño, "puntos de daño!")

   elif opcion_escape == "2":
      print("¡Inicias una rafaga de golpes!")
      for i in range(3):
         vida_enemigo -= 5
         print("> Golpe conectado por 5 de daño")

   elif opcion_escape == "3":
      if pociones > 0:
         vida_jugador += 30
         pociones -= 1
         print("¡Te curaste 30 puntos!")
      else:
         print("¡No te quedan pociones!")

   if vida_enemigo > 0:
      vida_jugador -= daño_enemigo
      print("¡El enemigo te ataco por 12 puntos de daño!")

   if vida_jugador < 0:
      vida_jugador = 0

   if vida_enemigo < 0:
      vida_enemigo = 0

if vida_jugador > 0:
    print("\n ¡VICTORIA!", nombre, "ha ganado la batalla.")
else:
    print("\n DERROTA. Has caido en combate.")