from fastmcp import FastMCP
from fastapi import FastAPI , Body
import uvicorn

app = FastAPI()
mcp = FastMCP("Demo server for test")

@mcp.tool()
def multiply(a: int, b: int) -> int:
    return a * b

@app.post("/multiply")
def call_multiply(data: dict=Body(...)):
    return {"result":multiply(data.get("a",0), data.get("b",0))}
    
@app.get("/")    
def home():
    return {"message": "Welcome to the FastMCP server!"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)