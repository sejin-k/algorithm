def solution(s):
    replace_dic = {'(':1, ')':2, '[':3, ']':4, '{':5, '}':6}
    count = 0
    
    for i in range(len(s)):
        string = s[i:] + s[:i]
        count += check_string(string, replace_dic)
    
    return count

def check_string(string, dic):
    stack = []
    
    for char in string:
        char_num = dic[char]
        if char_num % 2 == 1:
            stack.append(char_num)
        else:
            if len(stack) != 0 and stack[-1] + 1 == char_num:
                stack.pop()
            else:
                break
    else:
        if len(stack) == 0:
            return 1
        
    return 0

solution("}]()[{")   # test case