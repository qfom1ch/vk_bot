from .vk_session import vk_session


def send_massage(user_id, text, keyboard=None):
    message_dct = {'user_id': user_id,
                   'message': text,
                   'random_id': 0}
    if keyboard is not None:
        message_dct['keyboard'] = keyboard.get_keyboard()
    vk_session.method('messages.send', message_dct)
