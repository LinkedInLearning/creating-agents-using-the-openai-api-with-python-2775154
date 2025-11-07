from pydantic import BaseModel, field_validator, EmailStr
from email_validator import validate_email, EmailNotValidError

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
    
    @field_validator("email")
    def validate_custom_email(cls, v):
        try:
            allowed_domains = {"gmail.com", "test.com", "sample.com", "example.com"}
            emailinfo = validate_email(v, check_deliverability=False)
            email = emailinfo.normalized
            if emailinfo.ascii_domain not in allowed_domains:
                raise ValueError(f"Only emails from {', '.join(allowed_domains)} are allowed")
            if not email.isascii():
                raise ValueError("Invalid email format")
            return email
        except EmailNotValidError:
            raise ValueError("Invalid email format")

valid_data = {
    "name": "亜里栖",
    "age": 18,
    "email": "alice@gmail.com"
}
valid_data2 = {
    "name": "亜里栖",
    "age": 23,
    "email": "alice@example.com" 
}
invalid_data = {
    "name": "亜里栖",
    "age": 23,
    "email": "alice@exa.com" 
}
# 無効なメールアドレスの場合
user = User(**invalid_data)
print(user)