from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def home():
    return {"page":"Home"}
@app.get("/about")
def about():
    return {"page":"About","author":"Dhanu"}
@app.get("/health")
def health():
    return{"status":"ok"}
# POST request
@app.post("/create")
def create_something():
    return {"message":"created"}
#Path parameters
@app.get("/student/{usn}")
def get_result(usn):
    return {"Result":"Distinction","usn":usn}