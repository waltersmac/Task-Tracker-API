from typing import List, Union
from pydantic import BaseModel

class TestSchema(BaseModel):
    title: str
    description: Union[str, None] = None