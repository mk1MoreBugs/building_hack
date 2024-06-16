from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.app.dependencies import session_db
from backend.app.schemas.incidents import WorkerIncident, TechniqueIncident


router = APIRouter(
    prefix="/violations",
    tags=["violations"],
)


@router.get("/worker")
async def read_beaches(db_session: Session = Depends(session_db)) -> list[WorkerIncident]:
    pass


@router.get("/technique")
async def read_beaches(db_session: Session = Depends(session_db)) -> list[TechniqueIncident]:
    pass


@router.post("/worker")
async def read_beaches(data: WorkerIncident, db_session: Session = Depends(session_db)):
    pass


@router.post("/technique")
async def read_beaches(data: TechniqueIncident, db_session: Session = Depends(session_db)):
    pass


@router.put("/worker")
async def read_beaches(data: WorkerIncident, db_session: Session = Depends(session_db)):
    pass


@router.put("/technique")
async def read_beaches(data: TechniqueIncident, db_session: Session = Depends(session_db)):
    pass
