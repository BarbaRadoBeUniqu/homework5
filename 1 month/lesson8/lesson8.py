# работа с файлами
# try:
#     my_file = open('./lesson8/text.txt', 'w')
#     try:
#         my_file.write('Salam')
#         my_file.write('   Vsem')
#     except Exception as e:
#         print(e)
#     finally:
#         my_file.close()    

# except Exception as ex:
#     print(ex)

# with open('./lesson8/text.txt', 'w') as my_file:
#     my_file.write('  This file created by method with ... open')

# with open('./lesson8/text.txt', 'a') as my_file:
    # my_file.write('\n with append')
    # print('\t Salam world', file = my_file)

# with open('./lesson8/text.txt', 'r') as file:
    # for line in file:
    #     print(line, end="")
    # str1 = file.readline()
    # print(str1, end="")
    # str2 = file.readline()
    # print(str2, end = "")

    # line = file.readline()
    # while line:
    #     print(line, end="")
    #     line = file.readline()

    # content = file.read()
    # print(content)

    # contents = file.readlines()
    # print(contents)
    # str3 = contents[2]
    # print(str3)

# with open('./lesson8/text.txt', 'r', encoding='utf8') as file:

FILENAME = "./lesson8/text.txt"
msgs = []
i = 1
msg = input(f'Enter text {i}: ')

while msg != "":
    msg = input(f'Enter text {i+1}: ')
    msgs.append(msg + "\n")
    i += 1

with open(FILENAME, "a") as file:
    for message in msgs:
        file.write(message)

print('Reading file')
with open(FILENAME, "r", encoding="utf8") as file:
    for message in file:
        print(message, end='')