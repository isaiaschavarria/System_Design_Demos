import jwt
from datetime import datetime, timedelta

SECRET_KEY = "clave-super-secreta"
ALGORITHM = "HS256"

data = {"sub": "admin", "exp": datetime.utcnow() + timedelta(minutes=5)}

token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
print("Token generado:", token)

# Decodifica el token generado
decoded = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
print("Token decodificado:", decoded)
