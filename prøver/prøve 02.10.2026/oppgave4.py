while True:
    try:
        alder = int(input("Hvor gammel er du? "))
        break

    except ValueError:
        print("Skriv et tall!")

pris: int = 0

if alder < 12:
    pris = 80

elif alder >= 12 and alder <= 30:
    studentbevis: str = input("Har du studentbevis? ja/nei ").lower()

    if studentbevis == "ja" or studentbevis == "j":
        pris = 110

elif alder >= 67:
    pris = 100

if pris == 0:
    pris = 150

print(f"Biletten koster {pris}kr")
