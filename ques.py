ques_list = [
    "What is the capital of India?",
    "What is Economic capital of India?",
    "Which Indian states have snow?"
]

ans_list = ["New Delhi", "Mumbai", {"Kashmir", "Himachal Pradesh", "Uttarakhand"}]

opt_list = [
    ["New Delhi", "Mumbai", "Kolkata", "London"],
    ["Mumbai", "New Delhi", "Ujjain", "Varanasi"],
    ["Kashmir", "Himachal Pradesh", "Uttarakhand", "Kerala"]
]

marks = []

print('For Single Option, Just Type the Word. For Multi-Option, write words SEPARATED BY COMMAS eg \'a, b, c\'')

for i in range(len(ques_list)):
    print(ques_list[i], '\n', opt_list[i])
    ans = input('')
    
    if ans_list[i] == ans or ans_list[i] == set(ans.split(', ')):
        marks.append(5)
    else:
        marks.append(-1)

for i in range(len(ques_list)):
    print(ques_list[i], marks[i])

print('result: ', sum(marks))