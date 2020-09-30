from typing import List

from fastapi import APIRouter, Depends

from ..depends import db_session
from ..interface import IPlot
from ..models import Plot

PP_AR_PLOT = APIRouter()


@PP_AR_PLOT.get(
    "/",
    response_model=List[IPlot])
def get_all_plots(db=Depends(db_session)):
    query = db.query(Plot).all()
    pass
