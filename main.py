import sys
from difflib import restore
from math import trunc
from pickle import NEWOBJ

from roles import RolesPreset
from chat_service import ChatService
from config import settings


def choose_role() -> RolesPreset:
    print("Elegi un rol inicial:")
    print("1) Profesor 2) Traductor 3) Programador 4) Asistente")
    sel = input("> ").strip()
    mapping = {
        "1": RolesPreset.PROFESSOR,
        "2": RolesPreset.TRADUCTOR,
        "3": RolesPreset.PROGRAMADOR,
        "4": RolesPreset.ASISTENTE,
    }
    return mapping.get(sel, RolesPreset.ASISTENTE)


def print_help():
    print("\nComandos:")
    print(":rol profesor/traductor/programador/asistente -> Cambiar rol")
    print(":reset                                        -> Limpia la memoria")
    print(":salir                                       -> Salir de la aplicacion\n")


def main():
    print(f"{settings.system_name}")
    role = choose_role()
    chat = ChatService(role=role)
    print_help()

    while True:
        try:
            user = input("Vos: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nSaliendo")
            break

        if not user:
            continue

        if user.lower() in (":salir", "salir", "exit", "quit"):
            print("Saliendo")
            break
        if user.lower() == ":reset":
            chat.reset()
            print("Memoria borrada")
            continue
        if user.lower().startswith(":rol"):
            rest = user.split(" ")
            new_role = (rest[1] if rest else "").lower()
            mapping = {
                "profesor": RolesPreset.PROFESSOR,
                "traductor": RolesPreset.TRADUCTOR,
                "programador": RolesPreset.PROGRAMADOR,
                "asistente": RolesPreset.ASISTENTE,
            }
            if new_role in mapping:
                chat.set_role(mapping[new_role])
                print(f"Cambiado a rol: {new_role}")
            else:
                print("Rol no reconocido. Opciones: profesor, traductor, programador, asistente")
            continue

        if user.lower() == ":help":
            print_help()
            continue

        try:
            answer = chat.ask(user)
            print("Bot:", answer)
        except Exception as e:
            print("Error manejado", e)

if __name__ == "__main__":
    main()

