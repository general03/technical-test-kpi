from typing import Any, Dict, List
from db import engine
from sqlmodel import Session, select

from ..models.etat_avancement_enum import EtatAvancementName
from ..models.investment import Investment


class InvestmentRepository:

    def get(self, id: int | None = None, ville: str | None = None, etat_d_avancement: EtatAvancementName | None = None) -> List[Dict[str, Any]]:
        with Session(engine) as session:
            statement = select(Investment)
            if id:
                statement = statement.where(Investment.id == id)            
            if ville:
                statement = statement.where(Investment.ville == ville)
            if etat_d_avancement:
                statement = statement.where(Investment.etat_d_avancement == etat_d_avancement)
            results = session.exec(statement)
            data = results.all()
        return [el.model_dump() for el in data]
    
    def put(self, id: int, data: Investment) -> bool | ValueError:
        with Session(engine) as session:
            statement = session.get(Investment, id)
            if not statement:
                raise ValueError("Investment not found")
            
            hero_data = data.model_dump(exclude_unset=True)
            statement.sqlmodel_update(hero_data)
            session.add(statement)
            session.commit()
            session.refresh(statement)
            return True

