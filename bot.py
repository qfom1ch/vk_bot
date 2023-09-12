import logging

from vk_api.longpoll import VkEventType

from bot.handlers import send_massage
from bot.keyboards import (keyboard_afisha, keyboard_confirm,
                           keyboard_return_menu, keyboard_start,
                           keyboard_weather, menu_keyboard)
from bot.vk_session import longpoll, vk
from services.afisha import get_afisha
from services.currency import get_currency
from services.traffic import get_traffic
from services.wather import get_weather_now, get_weather_tomorrow

logger = logging.getLogger(__name__)

user_city_dct = {}


def main():
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')

    logger.info('Starting bot')

    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            if event.to_me:
                msg = event.text.lower()
                user_id = event.user_id
                user_city = vk.users.get(
                    user_ids=user_id,
                    fields='city')[0]['city']['title']
                try:
                    payload = event.payload
                except AttributeError:
                    payload = None

                if payload == '{"command":"start"}':
                    if user_city is None:
                        send_massage(user_id,
                                     'Укажите город:')
                    else:
                        send_massage(user_id,
                                     f'Вы проживаете в г.{user_city} верно?',
                                     keyboard=keyboard_confirm)

                if msg == 'подтвердить':
                    user_city_dct['user_id'] = user_id
                    user_city_dct['city'] = user_city
                    send_massage(user_id,
                                 'Город успешно зарегистрирован.\n'
                                 'Для того, чтобы изменить город, напишите '
                                 'название нового города в сообщении, '
                                 'в любое время.',
                                 keyboard=keyboard_start)

                if msg not in ['подтвердить', 'начать', 'погода', 'пробка',
                               'афиша', 'валюта', 'погода на сегодня',
                               'погода на завтра', 'вернуться в меню',
                               'афиша на cегодня', 'афиша на завтра']:
                    user_city_dct['user_id'] = user_id
                    user_city_dct['city'] = msg
                    send_massage(user_id,
                                 'Город успешно зарегистрирован.',
                                 keyboard=keyboard_start)

                if msg == 'начать' and payload is None:
                    send_massage(user_id,
                                 'Выберите, что хотите посмотреть:',
                                 keyboard=menu_keyboard)

                if msg == 'вернуться в меню':
                    send_massage(user_id,
                                 'Выберите, что хотите посмотреть:',
                                 keyboard=menu_keyboard)

                if msg == 'погода':
                    send_massage(user_id,
                                 'Выберите, на какой день хотите посмотреть:',
                                 keyboard=keyboard_weather)

                if msg == 'погода на сегодня':
                    try:
                        weather_description, temp = get_weather_now(
                            user_city_dct['city'])
                        send_massage(user_id,
                                     f'В городе '
                                     f'{user_city_dct["city"].capitalize()} '
                                     f'сейчас - {weather_description},'
                                     f' температура - {temp}°C.',
                                     keyboard=keyboard_return_menu)
                    except Exception:
                        send_massage(user_id, 'Возможны технические неполадки,'
                                              ' попробуйте позже.',
                                     keyboard=keyboard_return_menu)

                if msg == 'погода на завтра':
                    try:
                        weather_description, temp = get_weather_tomorrow(
                            user_city_dct['city'])
                        send_massage(user_id,
                                     f'В городе '
                                     f'{user_city_dct["city"].capitalize()} '
                                     f'завтра - {weather_description},'
                                     f' температура - {temp}°C.',
                                     keyboard=keyboard_return_menu)
                    except Exception:
                        send_massage(user_id, 'Возможны технические неполадки,'
                                              ' попробуйте позже.',
                                     keyboard=keyboard_return_menu)

                if msg == 'афиша':
                    send_massage(user_id,
                                 'Выберите, на какой день хотите посмотреть:',
                                 keyboard=keyboard_afisha)

                if msg == 'афиша на cегодня':
                    try:
                        send_massage(user_id, 'Топ событий на сегодня:')

                        for event, type_event, link in (
                                get_afisha(user_city_dct['city'],
                                           tomorrow=False)):
                            send_massage(user_id,
                                         f'{event} - {type_event}, '
                                         f'ссылка: {link}.')

                        send_massage(user_id,
                                     'Выберите, что хотите посмотреть еще:',
                                     keyboard=menu_keyboard)

                    except Exception:
                        send_massage(user_id, 'Возможны технические неполадки,'
                                              ' попробуйте позже.',
                                     keyboard=keyboard_return_menu)

                if msg == 'афиша на завтра':
                    try:
                        send_massage(user_id, 'Топ событий на завтра:')

                        for event, type_event, link in (
                                get_afisha(user_city_dct['city'],
                                           tomorrow=True)):
                            send_massage(user_id,
                                         f'{event} - {type_event}, '
                                         f'ссылка: {link}.')

                        send_massage(user_id,
                                     'Выберите, что хотите посмотреть еще:',
                                     keyboard=menu_keyboard)
                    except Exception:
                        send_massage(user_id, 'Возможны технические неполадки,'
                                              ' попробуйте позже.',
                                     keyboard=keyboard_return_menu)

                if msg == 'валюта':
                    try:
                        for currency, value in get_currency().items():
                            send_massage(user_id,
                                         f'1 USD - '
                                         f'{round(float(value), 2)} '
                                         f'{currency[3:]}')

                        send_massage(user_id,
                                     'Выберите, что хотите посмотреть еще:',
                                     keyboard=menu_keyboard)

                    except Exception:
                        send_massage(user_id, 'Возможны технические неполадки,'
                                              ' попробуйте позже.',
                                     keyboard=keyboard_return_menu)

                if msg == 'пробка':
                    send_massage(user_id,
                                 'Посмотрите здесь:' + ' ' +
                                 get_traffic(user_city_dct['city']))
                    send_massage(user_id,
                                 'Выберите, что хотите посмотреть еще:',
                                 keyboard=menu_keyboard)


if __name__ == "__main__":
    main()
