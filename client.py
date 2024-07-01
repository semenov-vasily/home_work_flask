import requests


# -----Запросы для записи, получения, изменения и удаления пользователя в бд-----

# -----Запись нового пользователя и его пароля----------
# response = requests.post('http://127.0.0.1:5000/user',
#                          json={'name': 'user_1',
#                                "password": "12345678"}
#                          )
# print(response.status_code)
# print(response.text)


# -----Получение данных о пользователе по его id----------
response = requests.get('http://127.0.0.1:5000/user/1',)
print(response.status_code)
print(response.text)


# -----Изменение данных о пользователе по его id----------
# response = requests.patch('http://127.0.0.1:5000/user/1',
#                          json={'name': 'user_q',
#                                "password": "12345678"}
#                          )
# print(response.status_code)
# print(response.text)


# -----Удаление пользователя по его id----------
# response = requests.delete('http://127.0.0.1:5000/user/1',)
# print(response.status_code)
# print(response.text)


#----------------------------------------------------------------------------
# -----Запросы для записи, получения, изменения и удаления объявлений в бд-----


# -----Запись нового объявления, привязанного к пользователю по его id----------
# response = requests.post('http://127.0.0.1:5000/post', json={'heading': 'Post_1',
#                                     'description': 'text_text_text_1',
#                                     'user_id': 1})
# print(response.status_code)
# print(response.text)


# -----Получение данных об объявлении, по его id----------
response = requests.get('http://127.0.0.1:5000/post/1')
print(response.status_code)
print(response.text)


# -----Изменение значений заголовка, текста, пользователя объявления по его id----------
# response = requests.patch('http://127.0.0.1:5000/post/2',
#                     json={'heading': 'Post_22222',
#                            'description': 'text_text_text_22222',
#                             'user_id': 1
#                             })
# print(response.status_code)
# print(response.text)


# -----Удаление объявления по его id----------
# response = requests.delete("http://127.0.0.1:5000/post/1")
# print(response.status_code)
# print(response.text)