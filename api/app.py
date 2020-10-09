from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from sqlalchemy.exc import IntegrityError
from api import models
from api.database import engine
from api.organizations import routers as org_routers
from api.users import routers as user_routers

def create_app():
    models.Base.metadata.create_all(bind=engine)

    app = FastAPI()
    app.include_router(org_routers.router)
    app.include_router(user_routers.router)
    register_error_handlers(app)
    return app

def register_error_handlers(app):

    # @app.exception_handler(IntegrityError)
    # def generic_exception_handler(request: Request, exc: IntegrityError):
    #     return JSONResponse(
    #         status_code=500,
    #         content={"message": "IntegrityError"},
    #     )

    @app.exception_handler(Exception)
    def generic_exception_handler(request: Request, exc: Exception):
        code = getattr(exc, "status_code", 500)
        message = getattr(exc, "message", getattr(exc, "description", None))
        if not message:
            message = f"{exc.__class__.__name__} {exc}"
        return JSONResponse(
            status_code=500,
            content={
                "code": f"{code}",
                "message": f"{message}"
            },
        )
