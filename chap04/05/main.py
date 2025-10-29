from agents import Agent, Runner
import asyncio

history_tutor_agent = Agent(
    name="歴史の専門家",
    handoff_description="歴史についての質問に答える専門家です",   
    instructions="歴史に関する質問に明確に回答します。重要な出来事と背景を説明します", )

science_tutor_agent = Agent(
    name="科学の専門家",
    handoff_description="科学についての質問に答える専門家です",   
    instructions="科学に関する質問にわかりやすく回答します",
)

triage_agent = Agent(
    name="トリアージエージェント",
    instructions="ユーザーの質問に基づいて、どのエージェントを使用するかを判断します",
    handoffs=[history_tutor_agent, science_tutor_agent],  # このエージェントが振り分け可能なエージェントのリスト
)

async def main():
    user_question = input("質問を入力してください: ")
    result = await Runner.run(triage_agent, input=user_question)
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
    