'''
def read_file(filename = 'read.txt') :
    with open(filename, 'r') as file :
        #read specific data
        data = file.read(10)
        print(data)
        #output --> my name is

        read specific line of the file
        file_line = file.readline()
        print(file_line)
        output --> my name is amit devadhe

        read 3 lines
        for i in range(3) :
            file_line = file.readline()
            print(file_line, end = '')
            1. my name is amit devadhe
            2. I live in pune
            3. I am from ahmednagar

            read list of lines
            file_lines = file.readlines()
            print(file_lines)
            ['1. my name is amit devadhe\n', '2. I live in pune\n', '3. I am from ahmednagar\n', '4. I love football\n', '5. My tech focus']

            for line in file_lines :
                print(line, end = '')
            1. my name is amit devadhe
            2. I live in pune
            3. I am from ahmednagar
            4. I love football
            5. My tech focus
read_file()

read last 2 lines of file
def last_lines(filename = 'read.txt') :
    with open(filename, 'r') as file :
        file_lines = file.readlines()
        last_2_lines = file_lines[-2 : :]

        for line in last_2_lines :
            print(line, end = '')
last_lines()
4. I love football
5. My tech focus

move file lines which are divided by 3 to next file.
def lines3(filename = 'read.txt', target = 'target.txt') :
    with open(filename, 'r') as file :
        temp = ''
        file_lines = file.readlines()
        for i in range(len(file_lines)) :
            if (i + 1) % 3 == 0 :
                temp = temp + file_lines[i]
    with open(target, 'w') as file1 :
        file1.write(temp)

lines3()
3. I am from ahmednagar
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Write a python program to move even lines and odd lines in two different file
def even_odd_data(filename = 'read.txt', even = 'even.txt', odd = 'odd.txt') :
    with open(filename, 'r') as file :
        tempe = ''
        tempo = ''
        file_lines = file.readlines()
        for i in range(1, len(file_lines)+1) :
            if i  % 2 == 0 :
                tempe = tempe + file_lines[i]
            else :
                tempo = tempo + file_lines[i]

    with open(even, 'w') as filee :
        filee.write(tempe)

    with open(odd, 'w') as fileo :
        fileo.write(tempo)

even_odd_data()
# even.txt
# 2. I live in pune
# 4. I love football

# odd.txt
# 1. my name is amit devadhe
# 3. I am from ahmednagar
# 5. My tech focus
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Write a python get all the email id from given file.
def email(filename = 'read.txt') :
    with open(filename, 'r') as file :
        file_lines = file.readlines()
        temp = ''
        for line in file_lines :
            if '@' in line :
                temp = temp + line
    print(temp, end = '')

email()
# 2. devadheamit@gmail.com
# 4. amitdevadhe3299@gmail.com
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Write a python program to replace word 'Python' with 'Java'
def replace(filename = 'read.txt', target = 'target.txt') :
    with open(filename, 'r') as file :
        output = file.read()
        print(output.replace('python', 'java'))
replace()
# This is python course.        --> original sentence
# This is java course.      --> After replace
---------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Write a python program to get all the mobile numbers from given file.
def mobile(filename = 'read.txt', target = 'phone.txt') :
    with open(filename, 'r') as file :
        file_lines = file.readlines()
        temp = ''
        for line in file_lines :
            sp = line.split(' ')
            for word in sp :
                if word.isnumeric() == True and len(word) == 10 :
                    temp = temp + word + '\n'
    with open(target, 'w') as file2 :
        file2.write(temp)

mobile()
# 9673592202
# 9674592202
# 7387184600
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
