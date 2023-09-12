from vk_api.keyboard import VkKeyboard, VkKeyboardColor

menu_keyboard = VkKeyboard(inline=True)
menu_keyboard.add_button('Погода', color=VkKeyboardColor.PRIMARY)
menu_keyboard.add_button('Пробка', color=VkKeyboardColor.SECONDARY)
menu_keyboard.add_button('Афиша', color=VkKeyboardColor.NEGATIVE)
menu_keyboard.add_button('Валюта', color=VkKeyboardColor.POSITIVE)


keyboard_confirm = VkKeyboard(inline=True)
keyboard_confirm.add_button('Подтвердить')

keyboard_start = VkKeyboard(one_time=True)
keyboard_start.add_button('Начать')

keyboard_return_menu = VkKeyboard(inline=True)
keyboard_return_menu.add_button('Вернуться в меню')

keyboard_weather = VkKeyboard(inline=True)
keyboard_weather.add_button('Погода на сегодня')
keyboard_weather.add_button('Погода на завтра')
keyboard_weather.add_line()
keyboard_weather.add_button('Вернуться в меню')

keyboard_afisha = VkKeyboard(inline=True)
keyboard_afisha.add_button('Афиша на cегодня')
keyboard_afisha.add_button('Афиша на завтра')
keyboard_afisha.add_line()
keyboard_afisha.add_button('Вернуться в меню')
