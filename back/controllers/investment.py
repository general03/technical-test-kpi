from fastapi import APIRouter
from fastapi.responses import JSONResponse

from back.dto.investment_dto import InvestmentDTO
from src.apps.investment.models.investment import Investment
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
    investment_dto = InvestmentDTO(id, ville, etat_d_avancement)
    data = investment.get_investment(investment_dto)
    if data:
        return {"data": data}
    return JSONResponse(status_code=404, content={"error": "No data found with parameters"})


@router.put("/{id}", response_model=Investment)
async def put(id: int, item: Investment):
    investment = InvestmentService()
    result = investment.put_investment(id, item)
    return JSONResponse(result)

 
 