from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import os
import duckdb
from projects import projects
import httpx
from selectolax.parser import HTMLParser

app = FastAPI(title="Data Analytics Portfolio Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')

app.mount("/data", StaticFiles(directory=data_dir), name="data")

@app.get("/")
def read_root():
    return {"message": "Backend is running!"}

@app.get("/files")
def list_data_files():
    files = []
    for fname in os.listdir(data_dir):
        if os.path.isfile(os.path.join(data_dir, fname)):
            files.append(fname)
    return {"files": files}

@app.get("/files/{filename}")
def get_data_file(filename: str):
    file_path = os.path.join(data_dir, filename)
    if os.path.exists(file_path):
        return FileResponse(file_path)
    return {"error": "File not found"}

@app.get("/projects")
def get_projects():
    return {"projects": projects}

@app.get("/projects/{project_id}")
def get_project(project_id: int):
    for project in projects:
        if project["id"] == project_id:
            return project
    return {"error": "Project not found"}

@app.post("/sql")
async def run_sql(request: Request):
    data = await request.json()
    query = data.get("query", "")
    if not query.strip().lower().startswith("select"):
        return JSONResponse({"error": "Only SELECT queries are allowed."}, status_code=400)
    con = duckdb.connect()
    # Register all CSV files in data_dir
    for fname in os.listdir(data_dir):
        if fname.endswith('.csv'):
            con.execute(f"CREATE OR REPLACE VIEW \"{fname}\" AS SELECT * FROM read_csv_auto('{os.path.join(data_dir, fname).replace('\\', '/')}')")
    try:
        result = con.execute(query).fetchdf().to_dict(orient="records")
        return {"result": result}
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=400)

@app.get("/scraping")
def scraping_demo():
    url = "https://httpbin.org/html"
    try:
        resp = httpx.get(url, timeout=10)
        html = HTMLParser(resp.text)
        title = html.css_first('h1').text() if html.css_first('h1') else 'No title found'
        return {"url": url, "title": title}
    except Exception as e:
        return {"error": str(e)} 