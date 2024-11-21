from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import List, Dict, Any

class Think(BaseModel):
    name : str = Field(description="음식의 이름")
    ingredient : list[str] = Field(description="음식의 재료들")
    recipe : list[str] = Field(description="음식의 레시피들")
    think: str = Field(description="너가 음식에 대해 생각한 것")

    def to_dict(self) -> Dict[str, Any]:
        return {"name" : self.name, "think" : self.think, "ingredient" : self.ingredient, "recipe" : self.recipe}

think = PydanticOutputParser(pydantic_object=Think)