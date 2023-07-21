from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.auth.router import router as auth_router
from app.tests.router import router as test_router
from app.habits.router import router as habit_router
from app.doctors.router import router as doctor_router
from app.config import client, env, fastapi_config

app = FastAPI(**fastapi_config)


@app.on_event("shutdown")
def shutdown_db_client():
    client.close()


app.add_middleware(
    CORSMiddleware,
    allow_origins=env.CORS_ORIGINS,
    allow_methods=env.CORS_METHODS,
    allow_headers=env.CORS_HEADERS,
    allow_credentials=True,
)

app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(test_router, prefix="/tests", tags=["Tests"])
app.include_router(habit_router, prefix="/habits", tags=["Habits"])
app.include_router(doctor_router, prefix="/doctors", tags=["Doctors"])
