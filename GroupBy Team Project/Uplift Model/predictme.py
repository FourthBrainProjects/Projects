

from pydantic import BaseModel

class predictme(BaseModel):
      history: float
      recency: int
      treatment:int