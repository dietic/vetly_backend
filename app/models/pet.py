import datetime
from sqlmodel import Field, SQLModel


class Pet(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    date_of_birth: datetime.date
    user_id: int = Field(nullable=False, foreign_key="user.id")
