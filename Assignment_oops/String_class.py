class String :

    def first2_last2(self, str1):   # 1
        '''
        This function returns the list containing the suqare of elements of the original list.
        :param str1: input string
        :return: output
        '''
        output = str1[0 : 2] + str1[-2 : ]
        return output

    def max_len_word(self, str1):   # 2
        '''
        This function return the word from the string which has the longest length
        :param str1:
        :return: lword
        '''
        output = str1.split(" ")
        leng = 0
        lword = ""
        for word in output:
            if len(word) > leng:
                leng = len(word)
                lword = word
        return lword

    def check_palindrome(self, str1):   # 3
        '''
        This function returns checks if given string is palindrome or not.
        Palindrome means string and it's reverse is same.
        :param str1:
        :return: True / False
        '''
        return str1[ : : -1] == str1

    def smallest_longest_word(self, str1):  # 4
        '''
        This function returns the longest and smallest word from the string in form of dictionary
        :param str1:
        :return: output
        '''
        output1 = {}
        longest = ""
        shortest = ""
        shleng = len(str1)
        loleng = 0
        output = str1.split(" ")
        for word in output:
            if len(word) <= shleng:
                shortest = word
                shleng = len(word)
            elif len(word) >= loleng:
                longest = word
                loleng = len(word)
        output1['smallest_word'] = shortest
        output1['longest_word'] = longest

        return output1

    def str_len(self, str1):    # 5
        '''
        Return the length of the string by for loop
        :param str1:
        :return: cnt
        '''
        cnt = 0
        for i in str1:
            cnt += 1
        return cnt

    def swap_last_char(self, str1): # 6
        '''
        This function returns swaps the last characters of 2 words.
        :param str1:
        :return: output
        '''
        mid = str1.split(" ")
        output = mid[0][0: -1] + mid[1][-1], "", mid[1][0: -1] + mid[0][-1]
        return output

    def vow_conso_repeate(self, str1):  # 7
        '''
        Function repeates the vowels 3 times and consonants 2 times.
        :param str1:
        :return: temp
        '''
        temp = ""
        vowels = "aeiou"
        output = str1.split(" ")
        for word in output:
            for i in range(len(word)):
                if word[i] in vowels:
                    temp = temp + word[i] * 3
                else:
                    temp = temp + word[i] * 2
            temp = temp + " "
        return temp