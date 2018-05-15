# -*- coding: utf-8 -*-
import json

from vk_api.vk_api import VkApi

class VK:
    def __init__(self, username, password):
        self.vk = VkApi(login=username, password=password)
        self.vk.auth()

    def send_message(self, chat_id, message):
        return self.vk.method(
            'messages.send',
            {'chat_id': chat_id, 'message': message}
        )

    def get_messages(self, value):
        return self.vk.method(
            'messages.get',
            value
        )

    def kick_user(self, chat_id, user_id):
        return self.vk.method(
            'messages.removeChatUser',
            {'chat_id': chat_id, 'user_id': user_id}
        )

    def invite_user(self, chat_id, user_id):
        return self.vk.method(
            'messages.addChatUser',
            {'chat_id': chat_id, 'user_id': user_id}
        )