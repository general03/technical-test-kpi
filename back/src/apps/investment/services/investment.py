from typing import Any, Dict, List
from ..models.etat_avancement_enum import EtatAvancementName
from ..repositories.investment import InvestmentRepository


class InvestmentService:

    def get_investment(self, id: int | None = None, ville: str | None = None, etat_d_avancement: EtatAvancementName | None = None) -> List[Dict[str, Any]]:
        investment_repository = InvestmentRepository()
        investment_data_object = investment_repository.get(id, ville, etat_d_avancement)
        return [el.model_dump() for el in investment_data_object]