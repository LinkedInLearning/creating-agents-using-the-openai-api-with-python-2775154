import asyncio
from pydantic import BaseModel
from agents import (
    Agent,
    GuardrailFunctionOutput,
    OutputGuardrailTripwireTriggered,
    RunContextWrapper,
    Runner,
    output_guardrail,
)

class MessageOutput(BaseModel):     #エージェントの出力型
    response: str

class MathOutput(BaseModel):    #ガードレールの出力型
    reasoning: str
    is_math: bool

guardrail_agent = Agent(        #ガードレール用エージェント
    name="Guardrail check",
    instructions="数学に関する回答が含まれているかどうかを判断してください。数学に関する質問には、方程式を解くこと、高度な計算、数学的概念の説明などが含まれます。",
    output_type=MathOutput,
)
@output_guardrail
async def math_guardrail( #エージェントの出力を受け取り、結果を返すガードレール関数
    ctx: RunContextWrapper, agent: Agent, output: MessageOutput
) -> GuardrailFunctionOutput:
    result = await Runner.run(guardrail_agent, output.response, context=ctx.context)

    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=result.final_output.is_math,
    )

agent = Agent(
    name="テクニカルサポート",
    instructions="あなたはテクニカルサポートエージェントです。ユーザーの技術的な質問に丁寧に回答してください",
    output_guardrails=[math_guardrail],
    output_type=MessageOutput,
)

async def main():
    try:
        # await Runner.run(agent, "PCが起動しません。どうすればいいですか？")
        await Runner.run(agent, "方程式 x^2 - 4 = 0 を解いてください")
        print("Guardrail 作動せず")

    except OutputGuardrailTripwireTriggered:
        print("Math output guardrail 作動しました")


if __name__ == "__main__":
    asyncio.run(main())