import telegram
from dotenv import load_dotenv #dotenv는 환경변수 관리를 돕는 라이브러이이다.
import os
import asyncio


env_path = 'secret/.env'
load_dotenv(dotenv_path=env_path)

#텔레그램 챗봇 api키와, 나와 연결되어 있는 chatId
token = os.getenv("TELEGRAM_API_KEY")
chatId = os.getenv("CHAT_ID")

async def main():
    bot = telegram.Bot(token)
    await bot.send_message(chat_id= chatId, text="Hello World")

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())
#비동기 작업을 관리하고 실행하는 asyncio라이브러리를 사용한다.

#별도의 웹페이지를 만드는 대신, 모든 조작을 텔레그램으로 할 것이다.