
from fastapi import FastAPI
from model.summary import getSummary
from fastapi import Form
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post('/',response_class=HTMLResponse)
async def read_item(request: Request,data: str =Form(...)):
    if data==None:
        return "enter some text"
    result=getSummary(data)
    print(result)
    return templates.TemplateResponse("summary.html", {"request": request,"result":result})