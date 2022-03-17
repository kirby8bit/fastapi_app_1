from fastapi import FastAPI, Form
from fastapi.responses import Response
from fastapi.staticfiles import StaticFiles
#объект response хранит в себе http ответ

users = {
    "katataolu@gmail.com": {
     "name":"danya",
     "password":"123456789"
    },
    "dekem_oleg@gmail.com":{
     "name":"oleg",
     "password":"123456789"
    },
    "nikita_penz1nn@gmail.com":{
     "name":"nikita",
     "password":"123456789"
    },
    "sasha_smvrt@gmail.com":{
     "name":"sasha",
     "password":"123456789"
    }
}

app = FastAPI() #экземпляр приложения fastapi
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def index_page():
    with open('templates/login.html',"r") as f:
        login_page = f.read()
    return Response(login_page,media_type="text/html")

@app.post("/login")
def login_page(user_email : str = Form(...),password : str = Form(...)):

    for e_mail,name_password in users.items():
        if e_mail == user_email:
            if name_password["password"] == password:
                name = name_password["name"]
                return Response(f"your e_mail,username:  {e_mail}!, hello, {name}",media_type="text/html")
            else:
                return Response(f"try again,username:  {e_mail}!",media_type="text/html")
    

