# prototipo_bienestar.py
# ---------------------------------
# Prototipo funcional en Python puro
# Plataforma de Bienestar Mental UVG
# ---------------------------------

usuarios = {}
mensajes = []

def menu_principal():
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
    print("Usuario registrado con éxito.")

def login():
    print("\n--- Iniciar sesión ---")
    usuario = input("Usuario: ")
    contrasena = input("Contraseña: ")
    if usuarios.get(usuario) == contrasena:
        print(f"\n¡Bienvenido {usuario}! 👋")
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
        "🌿 Respira profundo 3 veces cuando sientas ansiedad.",
        "🤝 Hablar con un amigo puede ayudarte a liberar tensiones.",
        "💪 Pedir ayuda es un signo de fortaleza, no de debilidad.",
        "😴 Descansa al menos 7 horas al día."
    ]
    for t in tips:
        print("-", t)

def podcast():
    print("\n--- Podcast semanal ---")
    episodios = [
        "🎧 Episodio 1: Manejo del estrés académico",
        "🎧 Episodio 2: Rompiendo el estigma de la salud mental",
        "🎧 Episodio 3: Balance entre trabajo y estudio"
    ]
    for ep in episodios:
        print("-", ep)

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
            print("Mensaje enviado ✅")
        elif opcion == "3":
            break
        else:
            print("Opción inválida.")

# --- Iniciar programa ---
menu_principal()
