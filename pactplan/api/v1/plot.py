import uuid
from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException

from pactplan.depends import db_session
from pactplan.interface import IPlot
from pactplan.models import Plot

PP_AR_PLOT = APIRouter()


@PP_AR_PLOT.get(
    "/",
    response_model=Optional[List[IPlot]])
def get_all_plots(db=Depends(db_session)):
    query = db.query(Plot).all()
    if query is None:
        return []
    return None


@PP_AR_PLOT.get(
    "/{plot_id}",
    response_model=IPlot,
    responses={
        200: {"model": IPlot},
        404: {
            "description": "Plot was not found"
        }
    })
def get_plot(plot_id: uuid.UUID, db=Depends(db_session)):
    query = db.query(Plot).get(plot_id)
    if query is None:
        raise HTTPException(status_code=404, detail="Plot not found")
