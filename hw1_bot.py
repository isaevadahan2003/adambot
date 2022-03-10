from aiogram import Bot, executor, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
from decouple import config

# import markups as mp
TOKEN2 = config("TOKEN2")
bot = Bot(TOKEN2)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def hello(message: types.Message):
    markup = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton('python quiz', callback_data='button1')
    markup.add(button1)
    await bot.send_message(message.chat.id, f'Hello my master, {message.from_user.full_name}', reply_markup=markup)


@dp.callback_query_handler(lambda func: func.data == 'button1')
async def quiz_1(call: types.CallbackQuery):
    markup2 = InlineKeyboardMarkup()
    button2 = InlineKeyboardButton('next question', callback_data='button2')
    markup2.add(button2)
    question = "What else is the Python programming language used for??"
    answers = ['For developing mobile applications', "For website development only", "Artificial intelligence",
               "What is a python?"]
    await bot.send_poll(
        call.message.chat.id,
        reply_markup=markup2,
        question=question,
        options=answers,
        is_anonymous=False,
        correct_option_id=2,
        type='quiz',
        open_period=7,
        explanation='Пайтон широкоприменяемый язык програмирования,даже исткусственный интеллект он не обошел стороной',
        explanation_parse_mode=ParseMode.MARKDOWN_V2,

    )


@dp.callback_query_handler(lambda func: func.data == 'button2')
async def quiz_2(call: types.CallbackQuery):
    markup3 = InlineKeyboardMarkup()
    button3 = InlineKeyboardButton('next question:', callback_data='button3')
    markup3.add(button3)
    question = 'Which of the following is not true of OOP principles?'
    answers = ["Inheritance", "Polymorphism", "Encapsulation", "Abstraction", "Cloning"]
    await bot.send_poll(
        call.message.chat.id,
        reply_markup=markup3,
        question=question,
        options=answers,
        is_anonymous=False,
        correct_option_id=4,
        type='quiz',
        open_period=7,
        explanation='Основные принципы ООП: наследование, полиморфизм, инкапсуляция, абстракция',
        explanation_parse_mode=ParseMode.MARKDOWN_V2
    )


@dp.callback_query_handler(lambda func: func.data == 'button3')
async def quiz_2(call: types.CallbackQuery):
    markup3 = InlineKeyboardMarkup()
    button_task = InlineKeyboardButton('go to task:', callback_data='button_task')
    markup3.add(button_task)
    question = 'Which of the following is an immutable data type in python?'
    answers = ['set', 'list', 'str', 'dict', 'byte arrays']
    await bot.send_poll(
        call.message.chat.id,
        reply_markup=markup3,
        question=question,
        options=answers,
        is_anonymous=False,
        correct_option_id=2,
        type='quiz',
        open_period=7,
        explanation='К неизменяемым типам данных относятся: str, int, float, bool, tuple',
        explanation_parse_mode=ParseMode.MARKDOWN_V2
    )


@dp.callback_query_handler(lambda func: func.data == 'button_task')
async def quiz_3(call: types.CallbackQuery):
    markup4 = InlineKeyboardMarkup()
    button_task1 = InlineKeyboardButton('go to solution:', callback_data='button_task1')
    markup4.add(button_task1)
    photo1 = open('media/Снимок экрана 2022-03-10 в 06.19.24.png', 'rb')
    await bot.send_photo(call.message.chat.id, photo=photo1, reply_markup=markup4)


@dp.callback_query_handler(lambda func: func.data == 'button_task1')
async def quiz_3(call: types.CallbackQuery):
    question = 'Output:'
    answers = ['A', "B", 'C', 'Error', 'A, B', "B,C", 'A, C']
    photo2 = open('media/2022-03-10 06.38.05.jpg', 'rb')
    await bot.send_photo(call.message.chat.id, photo=photo2)
    await bot.send_poll(
        call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        correct_option_id=4,
        type='quiz',
        open_period=7,
        explanation="You're loser",
        explanation_parse_mode=ParseMode.MARKDOWN_V2
    )


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)
