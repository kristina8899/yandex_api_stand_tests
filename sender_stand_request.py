import configuration
import requests
import data


def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json={"firstName": "Анатолий", "phone": "+79995553322", "address": "г. Москва, ул. Пушкина, д. 10"},
                         headers={"Content-Type": "application/json"})

response = post_new_user(data.user_body);
print(response.status_code)
print(response.json)
