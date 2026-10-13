while True:
    try:
        bilett_antall = int(input("Hvor mange biletter vil du ha fra 1 til 10? "))

        if bilett_antall not in range(1, 11):
            print("Du må skrive inn et tall mellom 1 og 10!\n")

        else:
            break

    except ValueError:
        print("Du må skrive inn et heltall!\n")

print(f"Totalpris er: {bilett_antall * 150}kr")
