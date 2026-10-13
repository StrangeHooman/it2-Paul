# Feil
try:

# Må caste alder til int
    alder = input("Hvor gammel er du? ")

# Mangler ":"
    if alder >= 18
        print("Du er myndig.")

# Trenger to "="
    elif alder = 17:
        print("Du blir myndig neste år!")
    else:
        print(f"Du blir myndig om {18 - alder} år.")


# Rettet
except:


    alder = int(input("Hvor gammel er du? "))

    if alder >= 18:
        print("Du er myndig.")
    elif alder == 17:
        print("Du blir myndig neste år!")
    else:
        print(f"Du blir myndig om {18 - alder} år.")
