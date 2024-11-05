from ninja import NinjaAPI

api = NinjaAPI()

@app.get("/api/v1/login")
def login(
    request, 
    uname: str, 
    passwd: str
    ) -> str:

    "API login througn username and password"
    
    '''
    TODO
    '''

@app.get("api/v1/register")
def register(
    request
    ) -> bool:

    "API registet througn token"

    '''
    TODO
    '''

@app.get("api/v1/getAssignments")
def getAssignments(
    request,
    id: str
    ):

    '''
    TODO
    '''
