from dataclasses import dataclass

from src.apps.investment.models.etat_avancement_enum import EtatAvancementName


@dataclass
class InvestmentDTO:
    id: int
    ville: str
    etat_d_avancement: EtatAvancementName
