from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
from langchain.prompts import PromptTemplate
from output_parser.output_parser import Think, think
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub
from langchain.tools import Tool
from tools.tool import search_food
def look_food(ingredients : list):
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.5)
    text = """
        음식의 재료를 줄게: {food} 
        이 재료들로 만들 수 있는 맛있는 음식을 찾아서 그 음식의 이름, 재료, 조리법, 그리고 너의 생각을 말해줘.
        만약 도구로 음식의 정보를 찾기 힘들거나 애매하면 , 너가 알고 있는 지식으로 대신 알려줘.
        최종 출력 형식은 아래와 같이 맞춰서 한글로 제공해줘:
        {output_format}
    """

    tools_from_agent = [
        Tool(
            name="음식 정보 가져오기",
            func=search_food,
            description="너가 음식의 재료로 만들 수 있는 음식을 가져올때 유용할거야"
        )
    ]

    react_prompt = hub.pull("hwchase17/react")
    react_agent = create_react_agent(prompt=react_prompt, llm=llm, tools=tools_from_agent)
    agent_axecutor = AgentExecutor(agent=react_agent, tools=tools_from_agent, verbose=True, output_parser = think)
    prompt = PromptTemplate(template=text, input_variables=['food', 'output_format'], partial_variables={'output_format' : think.get_format_instructions()})

    try :
        ingredients = ", ".join(ingredients)
        res = agent_axecutor.invoke({"input" : prompt.format_prompt(food=ingredients)})
        res = think.parse(res['output'])
        return res
    except :
        look_food(*ingredients)

if __name__ == '__main__':
    res = look_food(['돼지'])