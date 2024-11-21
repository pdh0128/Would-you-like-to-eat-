from langchain.chains.question_answering.map_rerank_prompt import output_parser
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
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    text = """
        음식의 재료를 줄게 {food} , 음식의 재료로 만들 수 있고 가장 맛있는 음식의 재료와 레시피 그리고 그 음식에 대힌 네 생각도 말해줘
        만약 도구로 음식의 정보를 찾지못하겠다면 너가 알고있는 지식으로 알려줘도 되. 
        출력은 한글로 해주시고 이 형식을 지켜주세요 : {output_format}
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

    try : res = agent_axecutor.invoke({"input" : prompt.format_prompt(food=ingredients)})
    except : return None
    return res['output']
if __name__ == '__main__':
    look_food(['고추', '무'])
