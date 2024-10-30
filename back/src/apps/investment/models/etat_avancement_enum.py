from enum import Enum

class EtatAvancementName(str, Enum):
    delivered = "Opération livrée"
    processing = "En Chantier"
    aborted = "Abandonné"
    studing = "Etude de maîtrise d'œuvre"