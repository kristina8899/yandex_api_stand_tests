import data
import sender_stand_request


# эта функция меняет значения в параметре Name
def get_kit_body(name):
	current_kit_body = data.kit_body.copy()
	current_kit_body["name"] = name
	return current_kit_body


# Функция для позитивных проверок
def positive_assertion(name):
	kit_body_positive = get_kit_body(name)
	kit_response_positive = sender_stand_request.post_new_user_kit2(kit_body_positive)
	assert kit_response_positive.status_code == 201
	assert kit_response_positive.json()["name"] == name



# Функция для негативных проверок
def negative_assertion(name):
	kit_body_negative = get_kit_body(name)
	kit_response_negative = sender_stand_request.post_new_user_kit2(kit_body_negative)
	assert kit_response_negative.status_code == 400


#1 Допустимое количество символов (1):kit_body = {"name": "a"}200
def test_create_kit_1_symbol_in_name_get_success_response():
	positive_assertion("a")

#2 Допустимое количество символов (511)201
def test_create_kit_511_symbols_in_name_get_success_response():
	positive_assertion(data.kit_body_positive)

#3 Количество символов меньше допустимого (0): 400
def test_3_negative():
	negative_assertion("")

#4 Количество символов больше допустимого (512):400
def test_4_negative():

	negative_assertion(data.kit_name_negative)

#5 Разрешены английские буквы:kit_body = {"name": "QWErty"
def test_create_kit_english_letters_in_name_get_success_response():
	positive_assertion("QWErty")
test_create_kit_english_letters_in_name_get_success_response()

#6 Разрешены русские буквы:kit_body = {"name": "Мария"}
def test_create_kit_russian_letters_in_name_get_success_response():
	positive_assertion("Мария")


#7 Разрешены спецсимволы:kit_body = {"name": ""№%@","}
def test_create_kit_has_special_symbols_in_name_get_success_response():
	positive_assertion("\"№%@\",")


#8Разрешены пробелы:kit_body = {"name": " Человек и КО "}
def test_create_kit_has_space_in_name_get_success_response():
	positive_assertion("Человек и КО")


#9Разрешены цифры:kit_body = {"name": "123"}
def test_create_kit_numeric_name_get_response():
	positive_assertion("123")

#10Передан другой тип параметра (число):kit_body = {"name": 123}
def test_create_kit_numeric_type_name_get_error_response():
	negative_assertion(123)



#11Параметр не передан в запросе:kit_body = {}400
def test_create_kit_empty_name_get_error_response():
	kit_response_negative = sender_stand_request.post_new_user_kit2({})
	assert kit_response_negative.status_code == 400

# название теста
def test_create_kit_no_name_get_error_response():
	current_kit_body_negative_no_name = data.kit_body.copy()
	current_kit_body_negative_no_name.pop("name")
	kit_response_negative = sender_stand_request.post_new_user_kit2(current_kit_body_negative_no_name)
	assert kit_response_negative.status_code == 400


