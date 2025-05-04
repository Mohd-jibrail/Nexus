from pydantic import BaseModel, Field, EmailStr

class SignIn(BaseModel):
    emai: EmailStr = Field(..., alias="email", description="User's email address")
    password: str = Field(
        ..., 
        min_length=8,
        max_length=128,
        regex=r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$",
        description="User's password must be at least 8 characters long and contain at least one letter and one number",
        example="Password@123",
        )

    
class SignUp(BaseModel):
    username: str = Field(
        ...,
        min_length=3,
        max_length=30,
        description="User's username must be between 3 and 30 characters long",
        example="john_doe",
    )
    password: str = Field(
        ...,
        min_length=8,
        max_length=128,
        regex=r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$",
        description="User's password must be at least 8 characters long and contain at least one letter and one number",
        example="Password@123",
    )
    email: EmailStr = Field(
        ...,
        description="User's email address",
        example="john_deo@gmail.com")
    is_active: bool | None = True
    is_admin: bool | None = False