from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
    email: str

user = User(name="Toru", age=25, email="toru@example.com")
# user = User(name="Tooru", age="twenty", email="taro@example.com")

# pydantic_core._pydantic_core.ValidationError: 1 validation error for User age
print(user.name)
print(user.email)