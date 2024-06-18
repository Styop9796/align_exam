from fastapi import FastAPI
import uvicorn

from employee_identification.main import app as app1
from service2.main import app as app2

app_one = FastAPI()
app_two = FastAPI()

app_one.mount("/app1", app1)
app_two.mount("/app2", app2)

if __name__ == "__main__":
    # Run each FastAPI application using uvicorn in separate threads or processes
    uvicorn.run(app_one, host="0.0.0.0", port=8800, log_level="info", reload=True)
    uvicorn.run(app_two, host="0.0.0.0", port=9000, log_level="info", reload=True)
