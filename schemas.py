from pydantic import BaseModel, Field


class CustomerBase(BaseModel):
    name: str
    address: str
    age: int = Field(gt=0)
    description: str | None


class CustomerGet(CustomerBase):
    id: int = Field(gt=0)


class CustomerPatch(BaseModel):
    name: str | None = None
    address: str | None = None
    age: int | None = Field(gt=0, default=None)
    description: str | None = None
