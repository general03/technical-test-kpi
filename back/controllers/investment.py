from fastapi import APIRouter
from fastapi.responses import JSONResponse

from src.apps.investment.services.investment import InvestmentService
from src.apps.investment.models.etat_avancement_enum import EtatAvancementName

router = APIRouter(
    prefix="/investment",
    tags=["investment"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
@router.get("/{id}")
async def get(id: int | None = None, ville: str | None = None, etat_d_avancement: EtatAvancementName | None = None):
    investment = InvestmentService()
    # it will be better to pass DTO
    data = investment.get_investment(id, ville, etat_d_avancement)
    if data:
        return {"data": data}
    return JSONResponse(status_code=404, content={"error": "No data found with parameters"})


    
 