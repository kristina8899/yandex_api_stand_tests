import configuration
import requests
import data


#Запрос_на_создание_нового_пользователя (код201)
def post_new_user(body):
    response = requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers={"Content-Type": "application/json"}
                         )
    return response

#Запрос на токен
def get_new_user_token():
    response = post_new_user(data.user_body)
    authToken = "Bearer " + response.json().get("authToken")
    return authToken


#Запрос на создание набора "мой" для этого пользователя

def post_new_user_kit(kit_body, authToken):
    print(configuration.URL_SERVICE + configuration.CREATE_USER_KIT)
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_KIT,
                         json=kit_body,
                         headers={
                                "Content-Type": "application/json",
                                "Authorization": authToken
                            }
                         )

#Запрос на создание набора "мой" для этого пользователя с зашитой внутрь автроизацией
def post_new_user_kit2(kit_body):
    return post_new_user_kit(kit_body, get_new_user_token())


