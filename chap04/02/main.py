from agents import Agent, Runner, function_tool

@function_tool(description_override="指定の都市の天気を返す関数です")
def get_weather(city: str) -> str:
    return f"{city} の天気は雨です"

agent = Agent(
    name="俳句エージェント",
    instructions="常に俳句で応答してね",
    model="gpt-5-mini",
    tools=[get_weather],
)

result = Runner.run_sync(agent, "東京の天気を教えてください")
print(result.final_output + "\n")
