from fastapi import FastAPI
import mangum
import uvicorn

app = FastAPI()
# comment
@app.get("/")
def read_root():
    return {"Hello": "07-02-2024 hello world"}

@app.get("/jenkins")
def read_root():
    return {"Hello": "14-02-2024 hello world"}

handler = mangum.Mangum(app)

if __name__ == "__main__":
   uvicorn.run(app, host="0.0.0.0", port=8080)
