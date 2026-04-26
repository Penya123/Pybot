import chatbot as Pybot
import database 
from datetime import date, time, datetime

print("██████╗░██╗░░░██╗██████╗░░█████╗░████████╗")
print("██╔══██╗╚██╗░██╔╝██╔══██╗██╔══██╗╚══██╔══╝")
print("██████╔╝░╚████╔╝░██████╦╝██║░░██║░░░██║░░░")
print("██╔═══╝░░░╚██╔╝░░██╔══██╗██║░░██║░░░██║░░░")
print("██║░░░░░░░░██║░░░██████╦╝╚█████╔╝░░░██║░░░")
print("╚═╝░░░░░░░░╚═╝░░░╚═════╝░░╚════╝░░░░╚═╝░░░")
print("A little dummy chatbot made in python,\ngo ahead and ask him something about programming :3")

opc = input("What you wanna do? \n" \
            "[1]Chat with him!\n" \
            "[2]Credits OwO\n")

match opc:
    case "1":
        print("Go on and talk to him")
    case "2":
        print("This dump app was made by Jorge Luis.\n" \
        "I built this using the gemini 3 flash preview model\n" \
        "connecting it with its API given free by Google AI Studio.")
    case _:
        print("I guess you want to talk to him anyways")