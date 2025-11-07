from agents import Agent, WebSearchTool, FileSearchTool
from my_funcs import get_current_weather

func_call_agent = Agent(
    name="weather agent",
    instructions="現在の天気についての質問に関数を呼び出して答えます。質問に答えられない場合はtriage agentにHandOffします",
    handoff_description="お天気の専門家です。現在の天気についての質問にopenweathermapを使って回答します",
    model="gpt-5-mini",
    tools=[get_current_weather],
)
web_search_agent = Agent(
    name="web search agent",
    instructions="最新の情報をウェブ検索して答えます。質問に答えられない場合はtriage agentにHandOffします",
    handoff_description="ウェブ検索して情報を取得する能力の高いエージェントです",
    model="gpt-5-mini",
    tools=[WebSearchTool()],
)
doc_search_agent = Agent(
    name="file search agent",
    instructions='menuファイルから情報を検索して答えます。質問に答えられない場合はtriage agentにHandOffします',
    handoff_description="飲食店のメニューから情報を取得して答えるエージェントです",
    model='gpt-5-mini',
    tools=[FileSearchTool(
        # Vector StoreオブジェクトのID
        vector_store_ids=['vs_68e87556362c81919de6c23c4868b5ac'],
    )]
)
triage_agent = Agent(
    name="triage agent",
    instructions="ユーザーの質問に基づいて、どのエージェントにHandOffするか判断します",
    model="gpt-5-mini",
    handoffs=[func_call_agent,web_search_agent,doc_search_agent],  # このエージェントが振り分け可能な専門エージェントのリスト
)

#相互handoffの設定
func_call_agent.handoffs=[triage_agent]
web_search_agent.handoffs=[triage_agent]
doc_search_agent.handoffs=[triage_agent]