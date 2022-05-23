from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
# BUTTONS FOR ADMIN TEAM KB
from aiogram.utils import callback_data

newadmin_button = InlineKeyboardButton(text='Добавить админа', callback_data='newadmin_button')
kickadmin_button = InlineKeyboardButton(text='Исключить админа', callback_data='kickadmin_button')
list_admin_button = InlineKeyboardButton(text='Список админов', callback_data='listadmin_button')

# ADMIN TEAM
team_markup = InlineKeyboardMarkup(1)
team_markup.insert(newadmin_button)
team_markup.insert(kickadmin_button)
team_markup.insert(list_admin_button)

#BUTTONS FOR questions_kb

questions_list = InlineKeyboardButton(text='Список вопросов', callback_data='questions_list')
new_question_button = InlineKeyboardButton(text='Добавить вопрос', callback_data='new_question')
change_q_button = InlineKeyboardButton(text='Изменить/Удалить вопрос', callback_data='change_question')

# questions_kb
questions_markup = InlineKeyboardMarkup(1)
questions_markup.insert(questions_list)
questions_markup.insert(change_q_button)
questions_markup.insert(new_question_button)
