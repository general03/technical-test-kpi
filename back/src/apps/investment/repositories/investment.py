from db import engine
from sqlmodel import Session, select

from ..models.etat_avancement_enum import EtatAvancementName
from ..models.investment import Investment


class InvestmentRepository:

    def get(self, id: int | None = None, ville: str | None = None, etat_d_avancement: EtatAvancementName | None = None):
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
        return data
