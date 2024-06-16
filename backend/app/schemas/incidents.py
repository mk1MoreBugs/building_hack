from pydantic import BaseModel, Field


class BaseIncident(BaseModel):
    name: str
    team_name: str
    date: str
    description: str
    description: str


class WorkerIncident(BaseIncident):
    team_name: str


class TechniqueIncident(BaseIncident):
    technique_name: str
