import asyncio
from agents import Agent, Runner

async def main():
    # Agentの作成
    agent = Agent(name="Assistant", model="gpt-5-mini", instructions="あなたは役に立つAIアシスタントです。")

    # Agentの実行
    result = await Runner.run(agent, "プログラミングの楽しさを短歌にしてください。")
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main()) 
