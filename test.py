"""AI thing.DOCSTRING MOMENT"""

import datetime
# import os.path

type_of_request = list(("Help", "Request", "Settings", "nya"))
# settings_parameters = [("version", 0.01),
#                        ("build", "prototype"),
#                        ("accesibilty_enable", False),
#                        ("online_mode", False),
#                        ("developer_mode", False)]

debug_date = datetime.datetime.now()
debug_string_date = debug_date.strftime("%d/%m/%Y %H:%M:%S")

noErrorMessage = "Run Completed || Date: " + debug_string_date + "\n"
# indexErrorMessage = "Error 1: Wrong Index Input || Date: " + debug_string_date + "\n"
# valueErrorMessage = "Error 2: Invalid Input || Date: " + debug_string_date + "\n"
# debugErrorDate = debug_string_date + "\n"

# settings_file_exists = os.path.exists("settingsLog.txt")

# if settings_file_exists is False:
#     settings_log = open("settingsLog.txt", 'x', encoding="UTF-8")
#     i = 0
#     while i < len(settings_parameters):
#         settings_list = str(settings_parameters[i][0]) + "=" +
#                         str(settings_parameters[i][1]) + "\n"
#         settings_log.write(settings_list)
#         i = i + 1
#     settings_log.close()


# def string_to_bool(input_text):
#     if input_text == "True":
#         return True
#     elif input_text == "False":
#         return False


# def setting_string_separator(input_text):
#     setting_array = input_text.split("=")
#     setting_name = setting_array[0]
#     setting_name = setting_name.replace("_", " ")
#     setting_value = setting_array[1]
#     output_text = setting_name.title() + ": " + setting_value.title()
#     return output_text


# def snake_case(text):
#     text = str(text)
#     text = text.lower()
#     text = text.replace(" ", "_")
#     return text


# def overwrite_setting(change):
#     name = snake_case(change[0])
#     i = 0
#     while i < len(settings_parameters):
#         if settings_parameters[i][0] == name:
#             pass
#     print("Done changing" + snake_case(change[0]))


# def data_type_check(text):
#     try:
#         textToInt = int(text)
#     except ValueError:
#         textToInt = None
#     else:
#         return textToInt

#     try:
#         textToFloat = float(text)
#     except ValueError:
#         textToInt = None
#     else:
#         return textToFloat

#     try:
#         textToBool = string_to_bool(text.title)
#     except ValueError:
#         textToBool = None
#     else:
#         return textToBool


# def modifiying_settings():
#     settings_log = open("settingsLog.txt", 'r', encoding="UTF-8")
#     print("\nCurrent settings:")
#     for x in settings_log:
#         print(setting_string_separator(x).strip("\n"))
#     settings_log.close()
#     user_settings_change = input("Type the setting name and value:\nexample:online mode = true\n")
#     print(user_settings_change.split("=")[0])
#     print(user_settings_change.split("=")[1])
#     overwrite_setting(user_settings_change.split("="))


print("Hello,user \nWhat to you need?\n")
print("Please select")

i = 0
while i < len(type_of_request):
    print(str(i) + " - " + type_of_request[i])
    i = i + 1

debug_log = open("debugLog.txt", 'a', encoding="UTF-8")
while True:
    try:
        request_index = input("Number: ")
        request_output = ("You choose " + type_of_request[int(request_index)])
    except ValueError:
        print("Please type a valid number")
        continue
    except IndexError:
        print("Please type a valid number within the range")
        continue
    if int(request_index) < 0:
        print("Please type a positive number")
        continue
    else:
        print(request_output)
        break


# print("Do you wish to change your settings?\n Enter True or False")

# while True:
#     changing_setting = input()
#     bool_changing_setting = string_to_bool(changing_setting)
#     if bool_changing_setting is True:
#         print("Changing some settings")
#         modifiying_settings()
#         break
#     elif bool_changing_setting is False:
#         print("Keeping the default settings")
#         break
#     else:
#         print("Please type True or False:")
#         continue


debug_log = open("debugLog.txt", 'a', encoding="UTF-8")
debug_log.write(noErrorMessage)
debug_log.close()
