# app.py

def mostrar_menu():
    print("\n🤖 Multiservicios 24/7")
    print("📍 Zona: San Pedro y Santa Catarina")
    print("\n¿Cómo podemos ayudarte?")
    print("1. Ver servicios")
    print("2. Cotizar")
    print("3. WhatsApp")
    print("4. Salir")


def ver_servicios():
    print("\n🔧 Servicios disponibles:")
    print("- Plomería")
    print("- Electricidad")
    print("- Reparaciones")


def cotizar():
    print("\n💬 Para cotizar:")
    problema = input("Describe tu problema (ej. fuga, corto circuito, lavabo roto): ")
    colonia = input("Indícanos tu colonia: ")

    print("\n⏳ Procesando tu solicitud...")
    print(f"📋 Problema: {problema}")
    print(f"📍 Colonia: {colonia}")
    print("📞 En breve te damos tu cotización al 8183567556")


def whatsapp():
    print("\n📱 Contáctanos por WhatsApp:")
    print("👉 8183567556")


def iniciar_bot():
    print("👋 Hola, bienvenido a Multiservicios 24/7")

    while True:
        mostrar_menu()
        opcion = input("\nSelecciona una opción: ")

        if opcion == "1":
            ver_servicios()

        elif opcion == "2":
            cotizar()

        elif opcion == "3":
            whatsapp()

        elif opcion == "4":
            print("\n👋 Gracias por contactarnos. ¡Hasta luego!")
            break

        else:
            print("\n❌ Opción no válida, intenta de nuevo.")


if _name_ == "_main_":
    iniciar_bot()