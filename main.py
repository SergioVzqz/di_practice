from datetime import datetime
from fastapi import FastAPI

from user_info_validate import UserInfoValidate

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome to university admission information validator"}

@app.get("/validator/")
async def validator(birthdate: str = '01/01/2000', gpa: float = '1.0', graduation_date: str = '01/01/2000'):

    result = UserInfoValidate(birthdate, gpa, graduation_date)

    return {"response": result}
