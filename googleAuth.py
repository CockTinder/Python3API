
from oauth2client.client import flow_from_clientsecrets
import httplib2

flow = flow_from_clientsecrets("creds.json",
                               scope=["https://www.googleapis.com/auth/userinfo.email", "profile"],
                               redirect_uri="http://localhost:5000/auth/google/callback")



def googleCallbackUrl():
    return flow.step1_get_authorize_url()

def auth(code):
    creds = flow.step2_exchange(code)
    return creds

#from httplib2 import Http

#test = Http()
#test.credentials.__str__()