from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import List, Dict, Any

class Think(BaseModel):
    name : str = Field(description="음식의 이름")
    ingredient : list[str] = Field(description="음식의 재료들")
    recipe : list[str] = Field(description="음식의 레시피들")
    think: str = Field(description="너가 음식에 대해 생각한 것")

    def to_dict(self) -> Dict[str, Any]:
        return {"name" : self.name, "ingredient" : self.ingredient, "recipe" : self.recipe, "think" : self.think}

think = PydanticOutputParser(pydantic_object=Think)

if __name__ == "__main__":
    output = """
    {
      "name": "김치찌개",
      "ingredient": ["김치", "돼지고기", "두부", "양파", "대파"],
      "recipe": ["1. 돼지고기와 양파를 볶는다", "2. 김치를 넣고 끓인다", "3. 두부와 대파를 넣고 마무리한다"],
      "think": "매콤하고 맛있다."
    }
    """

    parsed_result = think.parse(output)

    # 파싱된 결과 확인
    print(parsed_result)
    print(parsed_result.to_dict())  # 딕셔너리 형식으로 출력