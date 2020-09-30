from fastapi import APIRouter

PP_AR_PLOT = APIRouter()


@PP_AR_PLOT.get(
    "/")
def get_all_plots(db: Session = Depends(db_session)):
    query = db.query(Plot).all()
    pass
