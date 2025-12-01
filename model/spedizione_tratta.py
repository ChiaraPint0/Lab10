from dataclasses import dataclass

@dataclass

class SpedizioneTratta():
    id_hub_origine: int
    id_hub_destinazione: int
    media_valore_merce: float

    def __str__(self):
        return f"{self.id_hub_origine,self.id_hub_destinazione,self.media_valore_merce,self.contatore_tratte}"

    def __repr__(self):
        return f"{self.id_hub_origine,self.id_hub_destinazione,self.media_valore_merce,self.contatore_tratte}"


