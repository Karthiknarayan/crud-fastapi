from fastapi import FastAPI
app= FastAPI()
dummydatabase={
1:{"rcb"},
2:{"csk"},
3:{"mi"}
}
#returns all the object in the dummydatabase
@app.get('/')
def returnTeams():
    return dummydatabase

 #returns the object in the dummydatabase based on id
@app.get("/{id}")
def getTeamById(id : int):
    return dummydatabase[id]

#add the value in the dummydatabase
@app.post("/additem")
def addTeam(team:str):
    newid=len(dummydatabase.keys())+1
    dummydatabase[newid]={team}
    return dummydatabase
