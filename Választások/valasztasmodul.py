class val_adatok:
    def __init__(self, sor):
        vag = sor.split(" ")
        self.kerulet = int(vag[0])
        self.szavazat = int(vag[1])
        self.vezeteknev = int(vag[2])
        self.keresztnev = int(vag[3])
        self.part = int(vag[4])
