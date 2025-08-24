from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
from datetime import datetime, timedelta
import jwt  # PyJWT
from jwt import PyJWTError

app = FastAPI()

# Seguridad
SECRET_KEY = "clave-super-secreta-para-demo-en-clase"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
security = HTTPBearer()

# Modelo de usuario
class UserLogin(BaseModel):
    username: str
    password: str

# Crear token JWT
def create_access_token(data: dict, expires_delta: timedelta = timedelta(minutes=50)):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    #Claims
    to_encode.update({"exp": expire, "role": "AdminRole"})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Verificar token
def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    print("CREDENTIALS ", credentials)
    token = credentials.credentials
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        print("PAYLOAD ", payload)
        return payload
    except PyJWTError as ex:
        print(ex)
        raise HTTPException(status_code=401, detail="Token inválido")


# Endpoint para generar el token
@app.post("/login")
def login(user: UserLogin):
    if user.username != "admin" or user.password != "123456":
        raise HTTPException(status_code=400, detail="Credenciales inválidas")
    
    token = create_access_token({"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}

# Público
@app.get("/books/public")
def public_book():
    return {"message": "Cualquier persona puede ver esto"}

# Protegido
@app.get("/books/secure", dependencies=[Depends(verify_token)])
def secure_book():
    return {"message": "Solo con token válido puedes ver esto"}
