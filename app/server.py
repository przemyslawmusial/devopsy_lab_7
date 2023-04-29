from fastapi import FastAPI, HTTPException, status, Response
from pydantic import BaseModel
import math

app = FastAPI()


class InputDataModel(BaseModel):
    a: float
    b: float


@app.post("/odejmowanie", status_code=status.HTTP_200_OK)
async def odejmowanie(request: InputDataModel):
    msg = "sukces"
    wynik = request.a - request.b
    return {"wynik": wynik, "msg": msg}


@app.post("/mnozenie", status_code=status.HTTP_200_OK)
async def mnozenie(request: InputDataModel):
    msg = "sukces"
    wynik = request.a * request.b
    return {"wynik": wynik, "msg": msg}


@app.post("/dzielenie", status_code=status.HTTP_200_OK)
async def dzielenie(request: InputDataModel, response: Response):
    msg = "sukces"
    try:
        if math.isclose(request.b, 0):
            msg = "nie dziel przez 0 typie"
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="nie dziel przez 0 typie")
        wynik = request.a / request.b

    except HTTPException as e:
        response.status_code = e.status_code
        return {"wynik": None, "msg": msg}
    return {"wynik": wynik}
