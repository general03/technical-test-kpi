import datetime
from sqlmodel import SQLModel, Field


class Investment(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    titreoperation: str
    entreprise: str | None = Field(default=None, nullable=True)
    annee_de_livraison: int | None = Field(default=None, nullable=True)
    ville: str
    mandataire: str | None = Field(default=None, nullable=True)
    ppi: str
    lycee: str
    notification_du_marche: datetime.date | None = Field(default=None, nullable=True)
    codeuai: str
    longitude: float | None = Field(default=None, nullable=True)
    latitude: float | None = Field(default=None, nullable=True)
    etat_d_avancement: str
    montant_des_ap_votes_en_meu: int | None = Field(default=None, nullable=True)
    cao_attribution: datetime.date | None = Field(default=None, nullable=True)
    maitrise_d_oeuvre: str | None = Field(default=None, nullable=True)
    mode_de_devolution: str | None = Field(default=None, nullable=True)
    annee_d_individualisation: int | None = Field(default=None, nullable=True)
    enveloppe_prev_en_meu: float | None = Field(default=None, nullable=True)