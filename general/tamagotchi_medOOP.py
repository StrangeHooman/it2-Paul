class Kjaeledyr:
    def __init__(self, navn):
        self.navn = navn
        self.sult = 5
        self.energi = 5
        self.glede = 5

    def status(self):
        if self.sult > 7:
            print(f"{self.navn} er sulten.")

        if self.energi < 3:
            print(f"{self.navn} er sliten")

        if self.glede < 3:
            print(f"{self.navn} er ulykkelig")

        print(f"{self.navn}:\n Sult: {self.sult}, Energi: {self.energi}, Glede: {self.glede}")


    def mate(self):
        self.sult -=3
        self.glede += 1

    def leke(self):
        if self.energi > 2:
            self.glede += 3
            self.energi -= 2
            self.sult += 1

    def sove(self):
        self.energi += 4
        self.sult += 1

    def tid(self):
        self.sult += 1
        self.glede -= 1

    def clamp_vals(self):
        self.sult = clamp(self.sult, 0, 10)
        self.energi = clamp(self.energi, 0, 10)
        self.glede = clamp(self.glede, 0, 10)

def clamp(num, min, max):
    return max(min, min(num, max))


alle_dyr = [Kjaeledyr("Dimbus"), Kjaeledyr("Pusur")]


while True:
    for object in alle_dyr:
        object.status()

    try:
        action = int(input(f"""
1: Mate, 2: Leke, 3: Sove, 4: Adopter, 0: Avsultt
Velg: """))

        action_reference = None

        if action == 1:
            action_reference = Kjaeledyr.mate
        
        elif action == 2:
            action_reference = Kjaeledyr.leke

        elif action == 3:
            action_reference = Kjaeledyr.sove

        elif action == 4:
            alle_dyr.append(Kjaeledyr(input("Hva skal dyret hete? ")))

        elif action == 0:
            break

        else:
            print(f"Ugyldig kommando ({action}). Du må skrive et tall")


        if action_reference != None:
            print(f"Dyr du eier:")

            dyrenavn = []
            
            for dyr in alle_dyr:
                print(dyr.navn)
                dyrenavn.append(dyr.navn)

            dyr = input("Hvilket dyr vil du gjenomføre handlingen på? ")

            if dyr in dyrenavn:
                action_reference(alle_dyr[dyrenavn.index(dyr)])
        for dyr in alle_dyr:
            dyr.tid()
    except ValueError:
        print("Du må skrive et tall")

