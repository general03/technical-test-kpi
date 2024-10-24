from datetime import datetime
import typer
import json

app = typer.Typer()

from src.apps.investment.models.investment import Investment
from db import engine
from sqlmodel import Session 

@app.callback()
def callback():
    pass


@app.command()
def upload_file(file: str):
    with open(file) as data:
        data = json.load(data)
        
        with Session(engine) as session:
            for row in data:
                if "notification_du_marche" in row:
                    row["notification_du_marche"] = datetime.strptime(row["notification_du_marche"], '%Y-%m-%d')
                
                if "cao_attribution" in row:
                    row["cao_attribution"] = datetime.strptime(row["cao_attribution"], '%Y-%m-%d')

                session.add(Investment(**row))
            session.commit()


if __name__ == "__main__":
    app()
    