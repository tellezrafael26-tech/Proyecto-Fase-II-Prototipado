# Comentarios
# UNIVERSIDAD DEL VALLE DE GUATEMALA
# Departamento de Ingenieria Civil
# CC2005- 30
# Autores: Rafael Téllez, Irvin González, Andrés Morales, Rodrigo Martínez y Allison Figueroa 
# Fecha: 24/09/25
# Proyecto2 : Prototipado
# Descripción: salud Mental en los Universitarios entre los 18 a 23 años, catedráticos y estudiantes que trabajan y estudian

usuarios = {}   # Diccionario de usuarios
mensajes = []   # Lista de mensajes del chat

def mostrar_problema():
    print("\n=== PROBLEMA IDENTIFICADO ===")
    print("Los estudiantes universitarios enfrentan dificultades para acceder a apoyo en salud mental.")
    print("Muchos experimentan estrés, ansiedad o desmotivación, pero no buscan ayuda profesional")
    print("por miedo, poca disponibilidad de citas o la creencia de que 'no es algo grave'.")
    print("Esto puede causar bajo rendimiento, aislamiento, abandono de estudios y hasta conductas de riesgo.")
    print("\n=== SOLUCIÓN EN ESTE PROTOTIPO ===")
    print("✔ Acceso rápido y sencillo a una plataforma de apoyo.")
    print("✔ Recursos emocionales disponibles en todo momento (24/7).")
    print("✔ Podcast semanal para educación y sensibilización.")
    print("✔ Chat de acompañamiento entre estudiantes para disminuir el estigma.")
    print("-------------------------------------------------------------")

def menu_principal():
    mostrar_problema()
    while True:
        print("\n=== Bienestar Mental UVG ===")
        print("1. Registrarse")
        print("2. Iniciar sesión")
        print("3. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            login()
        elif opcion == "3":
            print("Gracias por usar la plataforma. ¡Cuídate!")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

def registrar_usuario():
    print("\n--- Registro ---")
    usuario = input("Elige un nombre de usuario: ")
    if usuario in usuarios:
        print("Ese usuario ya existe. Intenta con otro.")
        return
    contrasena = input("Elige una contraseña: ")
    usuarios[usuario] = contrasena
    print("Usuario registrado con éxito. Ahora tienes acceso a apoyo en salud mental.")

def login():
    print("\n--- Iniciar sesión ---")
    usuario = input("Usuario: ")
    contrasena = input("Contraseña: ")
    if usuarios.get(usuario) == contrasena:
        print(f"\n¡Bienvenido {usuario}")
        dashboard(usuario)
    else:
        print("Usuario o contraseña incorrectos.")

def dashboard(usuario):
    while True:
        print(f"\n=== Menú Principal ({usuario}) ===")
        print("1. Recursos emocionales 24/7")
        print("2. Podcast semanal")
        print("3. Chat de acompañamiento")
        print("4. Cerrar sesión")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            recursos()
        elif opcion == "2":
            podcast()
        elif opcion == "3":
            chat(usuario)
        elif opcion == "4":
            print("Sesión cerrada.")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

def recursos():
    print("\n--- Recursos emocionales 24/7 ---")
    tips = [
        " Respira profundo 3 veces cuando sientas ansiedad.",
        " Hablar con un amigo puede ayudarte a liberar tensiones.",
        " Pedir ayuda es un signo de fortaleza, no de debilidad.",
        " Descansa al menos 7 horas al día."
        " Piensa antes de actuar"
    ]
    for t in tips:
        print("-", t)
    print("\nEstos recursos brindan apoyo inmediato, sin necesidad de esperar una cita.")

def podcast():
    print("\n--- Podcast semanal ---")
    episodios = [
        "🎧 Episodio 1: Manejo del estrés académico",
        "🎧 Episodio 2: Rompiendo el estigma de la salud mental",
        "🎧 Episodio 3: Balance entre trabajo y estudio"
    ]
    for ep in episodios:
        print("-", ep)
    print("\nEl podcast ofrece educación y sensibilización continua sobre salud mental.")

def chat(usuario):
    print("\n--- Chat de acompañamiento ---")
    while True:
        print("\n1. Ver mensajes")
        print("2. Escribir mensaje")
        print("3. Volver al menú principal")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            print("\nMensajes en el chat:")
            if not mensajes:
                print("No hay mensajes todavía.")
            else:
                for m in mensajes:
                    print(f"{m['usuario']}: {m['texto']}")
        elif opcion == "2":
            texto = input("Escribe tu mensaje: ")
            mensajes.append({"usuario": usuario, "texto": texto})
            print("Mensaje enviado  Este espacio busca reducir la soledad y el estigma.")
        elif opcion == "3":
            break
        else:
            print("Opción inválida.")

# Iniciar programa
menu_principal()

