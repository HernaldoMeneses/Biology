'''
Introduction
    nature of life
    180 years ago
    English naturalist Charles darwin
    theory of evolution by natural selection
    core of the science of biology
'''
#1.1 - The Scinece of Life

text_all = []

read_Eng = "."
read_Port = ""
read_Key = {read_Eng:read_Port}
text_all.append(read_Key)

for item in text_all:
    for eng, port in item.items():
        print(f'English: {eng}')
        print(f'Portuguese: {port}\n')