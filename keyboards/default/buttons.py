from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

# button = KeyboardButton('⚡Получить вопрос')
request_button = KeyboardButton('Вопрос Стасу🧐')
give_me_button = KeyboardButton('💡Получить способ для…')
get_p_button = KeyboardButton('✏️ Хочу практику!')

back_button = KeyboardButton('Назад ⬅️')
focus_button = KeyboardButton('📸Фокусирования')
energy_button = KeyboardButton('💥Наполнения энергией')


markup = ReplyKeyboardMarkup(resize_keyboard=True).add(request_button, get_p_button)#, give_me_button)
#markup.add(get_p_button)
# markup.add(request_button)
give_me_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(focus_button, energy_button).add(back_button)

team_button = KeyboardButton('Команда')
questions_button = KeyboardButton('Меню вопросов')
reboot_db = KeyboardButton('Перезагрузить БД')
start_q = KeyboardButton('!Отправить вопрос!')

q_markup = ReplyKeyboardMarkup(resize_keyboard=True).add(questions_button, team_button).add(reboot_db, start_q)
