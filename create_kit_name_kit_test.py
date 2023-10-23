import data
import sender_stand_request


# эта функция меняет значения в параметре Name
def get_kit_body(name):
	current_kit_body = data.kit_body.copy()
	current_kit_body["name"] = name
	return current_kit_body


#Функция для позитивных проверок
def positive_assertion(name):
	kit_body_positive = get_kit_body(name)
	kit_response_positive = sender_stand_request.post_new_user_kit2(kit_body_positive)
	print(kit_body_positive)
	assert kit_response_positive.status_code == 201
	print(kit_response_positive.json()["name"] == name)
	assert kit_response_positive.json()["name"] == name



#Функция для негативных проверок
def negative_assertion(name):
	kit_body_negative = get_kit_body(name)
	kit_response_negative = sender_stand_request.post_new_user_kit2(kit_body_negative)
	print(kit_body_negative)
	assert kit_response_negative.status_code == 400


#1Допустимое количество символов (1):kit_body = {"name": "a"}200
def test_create_kit_1_symbol_in_name_get_success_response():
	positive_assertion("a")

print("1 Допустимое количество символов (1):kit_body = {\"name\": \"a\"} 200")
test_create_kit_1_symbol_in_name_get_success_response()

#2Допустимое количество символов (511)201
def test_create_kit_511_symbols_in_name_get_success_response():
	positive_assertion("symbol511")

print("2 Допустимое количество символов (511) 201")
test_create_kit_511_symbols_in_name_get_success_response()

#3Количество символов меньше допустимого (0): 400
def test_3_negative():
	negative_assertion("")

print("3Количество символов меньше допустимого (0): 400")
test_3_negative()

#4Количество символов больше допустимого (512):400
def test_4_negative():

	negative_assertion(data.kit_name_negative)

print("4 Количество символов больше допустимого (512):400")
test_4_negative()

#5Разрешены английские буквы:kit_body = {"name": "QWErty"
def test_create_kit_english_letters_in_name_get_success_response():
	positive_assertion("QWErty")

print("5 Разрешены английские буквы:kit_body = {\"name\": \"QWErty\"")
test_create_kit_english_letters_in_name_get_success_response()

#6Разрешены русские буквы:kit_body = {"name": "Мария"}
def test_create_kit_russian_letters_in_name_get_success_response():
	positive_assertion("Мария")

test_create_kit_russian_letters_in_name_get_success_response()

#7Разрешены спецсимволы:kit_body = {"name": ""№%@","}
def test_create_kit_has_special_symbols_in_name_get_success_response():
	positive_assertion("\"№%@\",")

test_create_kit_has_special_symbols_in_name_get_success_response()

#8Разрешены пробелы:kit_body = {"name": " Человек и КО "}
def test_create_kit_has_space_in_name_get_success_response():
	positive_assertion("Человек и КО")

test_create_kit_has_space_in_name_get_success_response()

#9Разрешены цифры:kit_body = {"name": "123"}
def test_create_kit_numeric_name_get_response():
	positive_assertion("123")

test_create_kit_numeric_name_get_response()

#10Передан другой тип параметра (число):kit_body = {"name": 123}
def test_create_kit_numeric_type_name_get_error_response():
	negative_assertion(123)

test_create_kit_numeric_type_name_get_error_response()

#11Параметр не передан в запросе:kit_body = {}400
def test_create_kit_empty_name_get_error_response():
	kit_response_negative = sender_stand_request.post_new_user_kit2({})
	assert kit_response_negative.status_code == 400

test_create_kit_empty_name_get_error_response()

#   Kit_body doesn't contain any name-field
def test_create_kit_no_name_get_error_response():
	current_kit_body_negative_no_name = data.kit_body.copy()
	#   Deleting a name-field from a query
	current_kit_body_negative_no_name.pop("name")
	negative_assertion_no_name(current_kit_body_negative_no_name)

def negative_assertion_no_name(json):
		print(json)
		kit_response_negative = sender_stand_request.post_new_user_kit2(json)
		assert kit_response_negative.status_code == 400
print (test_create_kit_no_name_get_error_response())

