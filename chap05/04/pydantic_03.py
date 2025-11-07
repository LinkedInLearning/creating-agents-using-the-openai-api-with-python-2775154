from pydantic import BaseModel, field_validator, EmailStr

class User(BaseModel):
    name: str
    age: int  
    email: EmailStr

    @field_validator('name')
    def name_must_not_be_empty(cls, v):
        if not v.strip():
            raise ValueError("名前は空白にできません")
        return v 
              
    @field_validator('age')
    def age_must_be_over18(cls, v):
        if v < 18:
            raise ValueError("年齢は18歳以上でなければなりません")
        return v


valid_data = {
    "name": "亜里栖",
    "age": 18,
    "email": "alice@example.com"
}
invalid_data = {
    "name": "亜里栖",
    "age": 23,
    "email": "alice@hogecom"
}
# 無効なメールアドレスの場合
try:
    user = User(**invalid_data)
    print(user)
except Exception as e:
    print(e)