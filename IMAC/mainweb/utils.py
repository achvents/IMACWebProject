import secrets

#Buat random id di custom user model
def custom_id():
    return secrets.token_urlsafe(8)