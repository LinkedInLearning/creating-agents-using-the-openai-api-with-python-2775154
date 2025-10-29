from agents import Agent, Runner
from pprint import pprint

agent = Agent(name="Assistant", model="gpt-5-mini", instructions="あなたは役に立つAIアシスタントです。")
# result = Runner.run(agent, "プログラミングの楽しさを短歌にしてください。")
# <sys>:0: RuntimeWarning: coroutine 'Runner.run' was never awaited
result = Runner.run_sync(agent, "プログラミングの楽しさを短歌にしてください。")
# print(result.final_output)

# pprint(agent)
pprint(result)