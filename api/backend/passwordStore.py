from flask import abort
from backend.models import SavedPassword

def store_password(email, domain, password):
    #TODO add 400's for: password already saved domain. change password instead.(or just do it? wdyt)
    #TODO add 400's for anyting else... basically 'debug me'
    if not (domain and password):
        abort(422, "Encountered empty domain name and/or password property. I need both to save your password")
    password_row = SavedPassword.create(email, domain, password)

    return {"email": email, "domain":domain, "passsword":password }



def retrieve_password(email, domain):
    #TODO add 400's for: password already saved domain. change password instead.(or just do it? wdyt)
    #TODO add 400's for anyting else... basically 'debug me'
    if not (domain):
        abort(422, "Encountered empty domain name property. I need it to retrieve the correct password")
    password = SavedPassword.get(email, domain)

    return {"email": email, "password":password}
