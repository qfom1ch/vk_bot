import vk_api
from vk_api.longpoll import VkLongPoll

from config import TOKEN

vk_session = vk_api.VkApi(token=TOKEN)
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)
