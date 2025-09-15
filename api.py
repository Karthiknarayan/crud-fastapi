from fastapi import FastAPI
from model import Team
app= FastAPI()
dummydatabase={
1:{
"number_of_titles":1,
"team":"RCB"
},
2:{
"number_of_titles":5,
"team":"CSK"
}
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
def addTeam(team:Team):
    newid=len(dummydatabase.keys())+1
    dummydatabase[newid]=team
    return dummydatabase
#modify the value in the dummydatabase based on id
@app.put("/modify")
def modifyteam(id:int, team:Team):
    dummydatabase[id]=team
    return dummydatabase