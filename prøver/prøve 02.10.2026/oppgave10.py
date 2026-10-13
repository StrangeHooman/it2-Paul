aktiviteter = []

def registrer():
    global aktiviteter

    type = input("Hvilken økttype vil du registere? ")
    tid = input("Hvor lenge? ")

    aktiviteter.append((type, tid))

    main()

def vis_aktiviteter():
    global aktiviteter
    for i in range(len(aktiviteter)):
        print(f"Økt type: {aktiviteter[i][0]}, økt lengde: {aktiviteter[i][1]}")

    main()

def statistikk():
    global aktiviteter

    main()


def main():
    
    while True:

        command = input("""
--- Treningslogg ---
1: Registrer økt
2: Vis alle økter
3: Statistikk
4: Avslutt
Velg: """)

        if command == "1":
            registrer()

        elif command == "2":
            vis_aktiviteter()

        elif command == "4":
            break

main()
