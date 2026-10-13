aktiviteter = [("løping", 10), ("svømming", 20)]

def registrer():
    global aktiviteter

    type = input("Hvilken økttype vil du registere? ")
    while True:
        try:

            tid = int(input("Hvor lenge? "))

            if tid <= 0:
                raise TypeError

            break

        except TypeError:
            print("Økttiden må være et heltall over 0")


    aktiviteter.append((type, tid))


def vis_aktiviteter():
    global aktiviteter
    for i in range(len(aktiviteter)):
        print(f"Økt type: {aktiviteter[i][0]:15}|     økt lengde: {aktiviteter[i][1]}")


def statistikk():
    global aktiviteter
    per_aktivitet = {}
    favoritt = ("Ingen aktivitieter", 0)
    total_tid = 0

    for aktivitet in aktiviteter:
        per_aktivitet[aktivitet[0]] = per_aktivitet.get(aktivitet[0], 0) + aktivitet[1]
        total_tid += aktivitet[1]

        if favoritt[1] < aktivitet[1]:
            favoritt = aktivitet

    print(f"Du har trent i totalt {total_tid} minutter.")
    print(f"Din mest trente aktivitet er {favoritt[0]} med {favoritt[1]} minutter.")
    print(f"Dine sammenlagte treningsøkter per økttype: ")

    for key in per_aktivitet.keys():
        print(f"Økttype: {key:15}|     sammenlagt tid: {per_aktivitet[key]}")

    


def main():
    
    while True:

        command = input("""
--- Treningslogg ---
1: Registrer økt
2: Vis alle økter
3: Statistikk
4: Avslutt
Velg: """)

        print("")

        if command == "1":
            registrer()

        elif command == "2":
            vis_aktiviteter()

        elif command == "3":
            statistikk()

        elif command == "4":
            break

        else:
            print("Ugyldig menyvalg! Skriv et tall som representerer operasjonen du vil utføre!\n")

        input("Fortsett")

main()
