# 문자열 데이터를 분석하기 전 처리 함수 만들기
# 1. 공백제거
# 2. 필요없는 문장부호 뺴기
# 3. 대소문자 정리
import re

states = {'Alalbama','Georgia!','Georgia', 'FlorIda', 'south carolina', 'West virgina?'}

def clean_strings(strings):
    results = []
    for string in strings:
        string = string.strip()                  #1
        string = re.sub('[!#?]', '', string)     #2
        string = string.title()                  #3

        results.append(string)
    return results

states = clean_strings(states)
print(states)

############################################################
#data -> f1() -> data2 -> f2() ->
states = {'Alalbama','Georgia!','Georgia', 'FlorIda', 'south carolina', 'West virgina?'}

def title(s):
    return s.title()

def remove_specialch(s):
    return re.sub('[!#?]', '', s)

def strip(s):
    return s.strip()

def clean_string(strings, *funcs):
    results = []
    for string in strings:
        for func in funcs:
            string = func(string)
        results.append(string)
    return results

states = clean_string(states, strip, remove_specialch, title)
print(states)

















