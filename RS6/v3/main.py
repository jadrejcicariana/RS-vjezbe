from fastapi import FastAPI
from fastapi import HTTPException
from models import Automobil
from data import automobili

app = FastAPI()


@app.get("/automobili/{id}", response_model=Automobil)
def dohvati_automobil(id: int):
    auto =  next((auto for auto in automobili if auto["id"] == id), None)

    if auto is None:
        raise HTTPException(status_code=404, detail="Automobil nije pronadjen")
    
    return auto


    

