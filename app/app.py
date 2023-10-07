from fastapi import FastAPI, Request
from fastapi.encoders import jsonable_encoder


import uvicorn

app = FastAPI()
@app.get('/')
def default_endpoint(request:Request):
    return jsonable_encoder({
       
        "body": {
            "Service": "Twimbit API",
            "Status": "Active"
        }
    })

@app.get('/ping')  # Use @app.get to define GET routes
def ping(request: Request):
    return jsonable_encoder({
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": {
            "Service": "Twimbit API - test commit",
            "Status": "Active"
        }
    })

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=3751)
