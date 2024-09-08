#https://viewer.diagrams.net/index.html?client=1&edit=_blank
#텔레그램 봇이 사용자의 요청에 따라 어떤 동작을 하게 하려면 이런 구조를 생각해야 한다고 한다.
#텔레그램 봇 모듈에서 Updater와 Dispatcher 객체를 사용한다고 함.

#Updater는 사용자로부터 새로운 메시지가 왔는지를 주기적으로 확인합니다. 이러한 방식으로 폴링(polling) 방식

#사용자로부터 어떤 명령어나 메시지가 왔다면 이를 Queue에 저장합니다. Dispatcher는 Update가 Queue에 넣어둔 사용자의 명령이나 메시지를 가져가서 처리하는 역할을 합니다. 
#이때 각 요청에 대한 처리를 담당할 핸들러(Handler) 객체를 미리 지정해두고 요청이 들어오면 지정된 핸들러를 통해 처리

#https://docs.python-telegram-bot.org/en/stable/examples.echobot.html

from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
from dotenv import load_dotenv #dotenv는 환경변수 관리를 돕는 라이브러리다.
import os

env_path = 'secret/.env'
load_dotenv(dotenv_path=env_path)

#텔레그램 챗봇 api키와, 나와 연결되어 있는 chatId
token = os.getenv("TELEGRAM_API_KEY")
chatId = os.getenv("CHAT_ID")

#커맨드 핸들러 정의
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    await update.message.reply_text("Hello! I'm Ready!")

# start 함수의 update와 context 변수는 텔레그램 봇이 수신하는 이벤트와 관련된 정보를 담고 있습니다. 각각의 역할을 아래와 같이 설명할 수 있습니다:

# update (Update 객체):

# update 객체는 봇이 수신한 특정 이벤트(메시지, 명령어, 버튼 클릭 등)에 대한 모든 정보를 포함합니다.
# 예를 들어, 사용자가 /start 명령어를 보냈을 때, 이 명령어와 관련된 모든 데이터(발신자 정보, 채팅 정보, 메시지 내용 등)가 update 객체에 저장됩니다.
# update.message: 사용자가 보낸 메시지 객체로, 메시지 텍스트, 보낸 사람 정보 등을 포함합니다.
# update.effective_chat: 메시지가 발생한 채팅에 대한 정보를 담고 있습니다.
# update.effective_user: 메시지를 보낸 사용자에 대한 정보를 담고 있습니다.
# context (ContextTypes.DEFAULT_TYPE 객체):

# context 객체는 봇의 현재 상태와 관련된 정보를 저장하며, 핸들러에서 공통적으로 접근할 수 있는 데이터를 제공합니다.
# 주로 핸들러 간에 데이터를 공유하거나, 작업 큐에 작업을 추가하는 등의 역할을 합니다.
# context.args: 명령어 뒤에 붙은 인수들을 리스트 형태로 담고 있습니다.
# context.bot: 봇의 인스턴스로, 봇의 메서드를 직접 호출할 수 있습니다. 예를 들어, 메시지 보내기, 파일 전송 등이 가능합니다.
# context.job_queue: 작업을 예약할 수 있는 작업 큐입니다.
# start 함수에서는 update.message.reply_markdown 메서드를 통해 사용자가 보낸 메시지에 대해 응답을 보내고 있습니다. 이때 update 객체를 사용해 사용자의 메시지를 처리하고, context 객체는 필요에 따라 추가 정보를 제공할 수 있습니다.

def main() -> None:
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(token).build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()

#사용자가 /start명령어를 입력하면 Hello! I'm Ready!라고 답장하는 텔레그램 봇이다.
#구조를 보면 웹 프레임워크랑 유사한 부분이 보임.