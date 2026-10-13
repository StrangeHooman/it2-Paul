poeng = {"Ada": 42, "Linus": 17, "Grace": 58, "Alan": 17, "Guido": 33}
poeng_lower = {}

total_poeng = 0
hoyest_poeng = 0
vinner: str

for key in poeng.keys():
    print(f"{key} har {poeng[key]} poeng.")
    total_poeng += poeng[key]

    poeng_lower[key.lower()] = poeng[key]

    if poeng[key] > hoyest_poeng:
        hoyest_poeng = poeng[key]
        vinner = key

print(f"Alle deltakere fikk til sammen {total_poeng} poeng")

print(f"{vinner} vant med {poeng[vinner]} poeng")

navn: str

try:
    navn = input("Skriv navnet til den du vil vite poengsummen av: ").lower()
    print(f"Poengsummen til {navn} er: {poeng_lower[navn]}")

except KeyError:
    print(f"Fant ingen deltaker med navnet {navn}")
