from fastapi import FastAPI
app= FastAPI()
dummydatabase={
1:{"rcb"},
2:{"csk"},
3:{"mi"}
}
@app.get('/')
def returnitems():
    return dummydatabase


    
@app.get("/{id}")
def getitembyid(id : int    ):
    return dummydatabase[id]