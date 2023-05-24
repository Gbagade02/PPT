def get_Max_repeted_length(string):

    words = string.split()
    
    word_frequency = {}
    for word in words:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1

    word_frequency =sorted(word_frequency.items(), key = lambda x:x[1], reverse = True)

    max_count_words = []
    for i in range(len(word_frequency)):
        if word_frequency[0][1] == word_frequency[i][1]:
            max_count_words.append(word_frequency[i][0])
    
    max_length = len(max_count_words[0])
    temp = max_count_words[0]

    for i in max_count_words:
        if len(i) > max_length:
            max_length = len(i)
            temp = i  

    return max_length


#Test Cases
string = "hello"
print("Output of test case1 is:  ", + get_Max_repeted_length(string))

string = "write write write all the number from from from 1 to 100"
print("Output of test case2 is:  ", + get_Max_repeted_length(string))

string = "apple banana apple banana orange apple banana"
print("Output of test case3 is:  ", + get_Max_repeted_length(string))

