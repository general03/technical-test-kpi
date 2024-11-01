from typing import Any, Dict, List

from back.dto.investment_dto import InvestmentDTO
from ..models.investment import Investment
from ..repositories.investment import InvestmentRepository


class InvestmentService:

    def get_investment(self, dto: InvestmentDTO) -> List[Dict[str, Any]]:
        """Get the investment from attributs inside InvestmentDTO

        Args:
            dto (InvestmentDTO): The investiment attributs 

        Returns:
            List[Dict[str, Any]]: List of data with attribut name as key and value as content
        """
        investment_repository = InvestmentRepository()
        return investment_repository.get(dto.id, dto.ville, dto.etat_d_avancement)
    
    def put_investment(self, id: int, data: Investment) -> bool | ValueError:
        """Update the investment with attributs inside Investment objet

        Args:
            id (int): The id of the investment to update
            data (Investment): The content to update in the investment

        Returns:
            bool | ValueError: True if no error occured, ValueError exception otherwiser
        """
        investment_repository = InvestmentRepository()
        return investment_repository.put(id, data)