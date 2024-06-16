from fastapi import FastAPI

from backend.app.routers import incidents

app = FastAPI(swagger_ui_parameters={"syntaxHighlight.theme": "nord"})


app.include_router(incidents.router)
