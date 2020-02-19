
class message:
    REQUEST_DATA = "Dime algo : "

    def welcome():
        print("*"*20)
        print("BIENVENIDO A TU PROBADOR DE CONFIANZA")
        print("*"*20)

def main():
    message.welcome()
    while True:
        dato == input(message.REQUEST_DATA)
        print(dato)
        if dato == ("send"):
            print("enviando")
        elif dato==("recive"):
            print("recibiendo")
        else






if __name__ == "__main__":
    main()

    