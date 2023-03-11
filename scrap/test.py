# """AI thing.DOCSTRING MOMENT"""

# import datetime
# # import os.path

# type_of_request = list(("Help", "Request", "Settings", "nya"))

# debug_date = datetime.datetime.now()
# debug_string_date = debug_date.strftime("%d/%m/%Y %H:%M:%S")
# noErrorMessage = "Run Completed || Date: " + debug_string_date + "\n"

# nya ='TEST TEXT'
# print(f'{nya.lower()}')
# print("Hello,user \nWhat to you need?\n")
# print("Please select")

# i = 0
# while i < len(type_of_request):
#     print(str(i) + " - " + type_of_request[i])
#     i = i + 1

# debug_log = open("debugLog.txt", 'a', encoding="UTF-8")
# while True:
#     try:
#         request_index = input("Number: ")
#         request_output = ("You choose " + type_of_request[int(request_index)])
#     except ValueError:
#         print("Please type a valid number")
#         continue
#     except IndexError:
#         print("Please type a valid number within the range")
#         continue
#     if int(request_index) < 0:
#         print("Please type a positive number")
#         continue
#     if int(request_index) == 3:
#         print(".,__,.........,__,.....╭¬¬¬¬¬━━╮")
#         print("`•.,¸,.•*¯`•.,¸,.•*|:¬¬¬¬¬¬::::|:^--------^ ")
#         print("`•.,¸,.•*¯`•.,¸,.•*|:¬¬¬¬¬¬::::||｡◕ ‿‿ ◕｡| ")
#         print("-........--\"\"-.......--\"╰O━━━━O╯╰--O-O--╯")
#         break
#     else:
#         print(request_output)
#         break

# debug_log = open("debugLog.txt", 'a', encoding="UTF-8")
# debug_log.write(noErrorMessage)
# debug_log.close()
import datetime

time = datetime.datetime.now()
output = time.strftime('%I:%M %p')
print(output)

time = datetime.datetime.now()
output = time.strftime('%B %d %Y')
print(output)

months_en =['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
months_tl =['Enero', 'Pebrero', 'Marso', 'Abril', 'Mayo', 'Hunyo', 'Hulyo', 'Agosto', 'Setyembre', 'Oktubre', 'Nobyembre', 'Disyembre']

month_en = 'January'

def translate_month(month_en):
    i = months_en.index(month_en)
    print (months_tl[i])

translate_month('January')