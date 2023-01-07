"""
obj = open('filename/filepath','filemode')

filemode:
'read mode':-we can read the content of the existing file with read mode.
write mode :-we can write the content in the existing file or we can create the file and then write it.
                but the existing content will overwrite with new content.
append mode :-we can write the content in the existing file or we can create the file and then write it.
                but the existing content will as it is and new content add in the last of the file.



# Read the content of the existing file.
file_obj = open('file1.txt','r')
data = file_obj.read()
print(data)
print('file_name :',file_obj.name)
print('file_mode :',file_obj.mode)
file_obj.close()

# write content of file.
# case 1 :-file dose not exist :when we open the file with write mode then will create the new file
            #and add the content to the file.
str1 = "my name is Arati, and i am pursuing the bi course from my tech focus"
file_obj2 = open('new_write.txt','w')
file_obj2.write(str1)
file_obj2.close()

# case 2 :if file is already exist:
new_content1 = 'We believe in collaboration and team work. ' \
               'We see ourselves as an extended team of our clients and ' \
               'collaborate with all the stakeholders of the project.'
file_obj3 = open('new_write.txt','w')
file_obj3.write(new_content1)

# create python file :
str3 = "print('hello world')"
file_obj4 = open('test_programs.py','w')
file_obj4.write(str3)
file_obj4.close()


# append mode : write content to file with the append mode:
# case 1 : if file dose not exist then append create new file and (append ) add content to the file.

str4 = 'Being the CTO of the Company.'
file_obj5 = open('new_append_file.txt','a')
file_obj5.write(str4)
file_obj5.close()

#case 2 :if the file alredy exits then append mode will
# add content to file at the end of the file

str5 = '\n An enthusiastic, people person with over 6 years of experience,'
file_obj5 = open('new_append_file.txt','a')
file_obj5.write(str5)
file_obj5.close()


# Read binary mode(rb)
# Open the image and its content:
file_obj6 =open('C:/Users/HP/Desktop/identity_photo_NEW.jpg','rb')
data = file_obj6.read()
print(data)
print('file_mode :',file_obj6.mode)
file_obj6.close()


# context manager :it has its own enter and exit method ,so no need to close the file specifically.
with open('file2.txt','r') as new_file:
    data = new_file.read()
    print(data)

str7 = 'abahfjfheshjdksjdkjd'
with open('file2.txt', 'w') as new_file1:
    new_file1.write(str7)

# open file for with read and write the operation with r+.

str8 = 'Process finished with exit code 0'
with open('file2.txt','r+') as new_file11:
    data = new_file11.write(str8)
    print(data)
# here we perform the read and write operatios both using the r+ mode(read and write)


# open file with read and write operation with w+
# we can not read the content of file because the w+ mode overwrite the all the content of the perticulr file
# so that we can not read the content of the file(file is empty)
str9 = 'fejaksAk[qpwosidjxnmPWOSKDJCMXPOIDJXM,[POSK'
with open('file1.txt','w+') as file:
    data = file.read()
    print(data)

# a+ mode with read operation:
# it will not change the content of the file
str10 = '\ndhgasdhj;aslhdgcvbosiahdgb \n'
with open('file2.txt','a+') as file1:
    data = file1.read()
    print(data)

# a+ mode with write operation:
# it will add the content at the end of the file like append mode
str10 = '\ndhgasdhj;aslhdgcvbosiahdgb \n'
with open('file2.txt','a+') as file1:
    file1.write(str10)



# Create different extension file:
file_extension = ['txt','png','xls','mp3','json']
for ext in file_extension:
    for i in range(1,3):
        filename = f"test_file_{i}.{ext}"
        str1 = 'lkdjashgdfvlpoiugsyadvb'*100
        file_obj = open(f"{filename}",'w')
        file_obj.write(str1)
        file_obj.close()
"""
# read file using function
def read_file_data(file_name = 'file2.txt'):
    with open(file_name,'r') as file:
        """
        # read specific byte of data
        print(file.read(20))
        
        #read  lines of the data
        file_line= file.readlines()
        print(file_line)

        #read 5 lines from the data
        for i in range(5):
            file_line =file.readlines()
            print(file_line,end='')
        
#         # Read list of lines
        file_lines = file.readlines()
        print(file_lines)
        for line in file_lines:
            print(line, end="")
        
# read_file_data()


# read last two lines of the data:
def read_last_2lines(file_name = 'file2.txt'):
    with open(file_name,'r') as file:
        data = file.readlines()
        last_two_lines = data[-2:]
        # print(last_two_lines,end='')
        for lines in last_two_lines:
            print(lines,end='')
read_last_2lines()

# # move file lines which are divide by 3 to next file
def move_data(file_name ="file2.txt",target_file = "tar_file.txt"):
    with open(file_name,'r') as file:
        temp = ''
        read_line = (file.readlines())
    for i in range(len(read_line)):
        # print(i)
        if (i+1)%2 == 0:
            temp = temp + read_line[i]
    # print(temp)

    with open(target_file,'w') as file:
        file.write(temp)
move_data()

# # Write a python program to move even lines and odd lines in two different file
def move_even_odd_data_separately(file_name ="file2.txt",even_file = "ev_file.txt",odd_file = "odd_file.txt"):
    with open(file_name,'r') as file:
        temp1 =''
        temp2 =''
        read_line =file.readlines()
    for i in range(len(read_line)):
        # print(i)
        if i%2 == 0:
            temp1 = temp1 + read_line[i]
        else:
            temp2 = temp2 + read_line[i]
    # print(temp1)
    #
    # print('*'*100)
    # print(temp2)

    with open(even_file,'w') as file:
        file.write(temp1)

    with open(odd_file,'w') as file:
        file.write(temp2)

move_even_odd_data_separately()


# # Write a python program to get all the email id from given file.
def move_email_data(file_name ="file1.txt",tarfile = 'email.txt'):
    with open(file_name,'r') as file:
        temp = ''
        data_lines  = file.readlines()
        # for line in data_lines:
        #     print(line,end='')

    for i in range(len(data_lines)):
        if '@' in data_lines[i]:
            temp = temp + data_lines[i]
    print(temp)

    with open(tarfile,'w') as file:
        file.write(temp)
move_email_data()


# Write a python program to get all the mobile numbers from given file.
def move_mobile_data(file_name ="file1.txt",tarfile1 = 'mobile.txt'):
    with open(file_name,'r') as file:
        temp1 = ''
        data_lines  = file.readlines()
        # for line in data_lines:
        #     print(line,end='')
    for line in data_lines:
        # print(line)
        temp = line.split(' ')
        # print(temp)
        for i in range(len(temp)):
            if temp[i].isnumeric() == True and len(temp[i]) == 10:
                temp1 = temp1 + temp[i]+ '\n'
    print(temp1)


    with open(tarfile1,'w') as file:
        file.write(temp1)
move_mobile_data()
"""

# # Write a python program to replace word 'Python' with 'Java'
# def replace_data(file_name="file1.txt", rep_file="replace.txt"):
#     with open(file_name, 'r') as file:
#         temp = ''
#         # data_lines = file.readlines()
#         # output = data_lines.r
#         # for line in data_lines:
#         #     print(line,end='')
#     # for i in range(len(data_lines)):
#     #     temp  = temp + 'python'
#     # print(temp)
#         # if 'python' in data_lines[i]:
#
#
#     # print(temp)
#
#
# # replace_data()