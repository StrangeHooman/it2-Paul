varer = {
    "A100" : {"navn" : "acer trådløs mus", "pris" : 100, "antall_pa_lager" : 3, "kategori" : "datamus"},
    "B100" : {"navn" : "lenovo legion pro 5", "pris" : 1500, "antall_pa_lager" : 10, "kategori" : "laptop"},
    "B200" : {"navn" : "samsung monitor", "pris" : 2000, "antall_pa_lager" : 2, "kategori" : "dataskjerm"},
    "C050" : {"navn" : "razer musematte", "pris" : 200, "antall_pa_lager" : 7, "kategori" : "tilbehør"},
    "G800" : {"navn" : "razer blackshark v2 pro", "pris" : 800, "antall_pa_lager" : 0, "kategori" : "headset"}
    }

# Jeg valgte denne strukturen fordi det er enkelt å loope gjennom alle varene og finne ut av alle spesifikasjoner
# Jeg bruker varenummer heller enn navn for hvert objekt fordi disse gjerne er mer unike enn navnet (noen varer kan ha lignende eller til og med like navn)

def vis_lager(lager):
    for key in lager.keys():
        if lager[key]["antall_pa_lager"] > 0:
            print(f"Varenummer: {key}, navn: {lager[key]["navn"]}, pris: {round(lager[key]["pris"], 2)}, antall på lager: {lager[key]["antall_pa_lager"]}, kategori: {lager[key]["kategori"]}")

def selg_vare(lager, varenummer, antall):
    try:
        if (lager[varenummer]["antall_pa_lager"] - antall) < 0:
            print(f"Ikke nok varer på lager!")
            return False

        else:
            lager[varenummer]["antall_pa_lager"] -= antall
            print(f"Kunden må betale {lager[varenummer]["pris"] * antall}kr")
            return True

    except KeyError:
        print(f"Ingen vare med varenummeret {varenummer}!")
        return False

def lav_beholdning(lager, grense=5):
    liste_lite_lager = [("placeholder", 0)]
    navn_liste_lite_lager = []
    for value in lager.values():
        if value["antall_pa_lager"] < grense:

            antall = value["antall_pa_lager"]

            for i in range(len(liste_lite_lager)):
                if antall > liste_lite_lager[i][1]:

                    liste_lite_lager.insert(i, (value["navn"], antall))

                elif i == (len(liste_lite_lager) - 1):

                    liste_lite_lager.append((value["navn"], antall))

    for i in range(len(liste_lite_lager)):
        if liste_lite_lager[i][0] == "placeholder":
            continue
        else:
            navn_liste_lite_lager.append(liste_lite_lager[i][0])

    return navn_liste_lite_lager
    

vis_lager(varer)
print("\nSalg 1:", selg_vare(varer, "C050", 5))
print("Salg 2:", selg_vare(varer, "C600", 5))
print("Salg 3:", selg_vare(varer, "C050", 10))

print(f"\n{lav_beholdning(varer)}")
