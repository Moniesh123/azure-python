from fastapi import FastAPI

app=FastAPI()
@app.get("/")
def default():
    return{"success ": True,"message":"this is a default page"}

@app.get("/home)")
def home():
    return{"success":True,"message":"this is a home page"}
