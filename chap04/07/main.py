import asyncio
from agents import Agent, Runner, FileSearchTool
agent = Agent(
    name='file search agent',
    instructions='ファイルから情報を検索して答えます',
    model='gpt-5-mini',
    tools=[FileSearchTool(
        # Vector StoreオブジェクトのID
        vector_store_ids=['vs_688c4d284eb88191afaa8e8830a80cf8'],
    )]
)
# agent = Agent(
#     name='file search agent',
#     instructions='ファイルから情報を検索して答えます',
#     model='gpt-5-mini',
#     tools=[FileSearchTool(
#         # Vector StoreオブジェクトのID
#         vector_store_ids=['vs_68e71f621a808191bb7e8a8d21517fc3'],
#     )]
# )
async def main():
    result = await Runner.run(
        agent,
        'Limitationsについて教えて',
        # '交通費は全部でいくらですか？',
    )
    print(result)
    
if __name__ == '__main__':
    asyncio.run(main())