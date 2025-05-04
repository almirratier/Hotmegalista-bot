import os
from aiogram import Bot, Dispatcher, executor, types

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("🤖 Olá! Seja bem-vindo ao Hot Mega Lista!\n\nEnvie o @ do seu canal para cadastro.")

@dp.message_handler(lambda message: message.text.startswith("@"))
async def receive_channel(message: types.Message):
    await message.answer(f"✅ Canal {message.text} recebido! Aguardando aprovação do administrador.")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
    
