'''
dic = {"강아지":"dog", "고양이":"cat", "새":"bird", "코끼리":"elephant"}

while True:
    word = input("단어를 입력하시오(종료:0):")
    
    if word == '0':
        print("종료되었습니다.")
        break
    elif word in dic:
        print(word," : ",dic[word])
    elif word not in dic:
        print("사전에 없는 단어입니다.")
'''
mydict = {}

fp = open("c:\\python_test\\animal_dictionary","r", encoding = 'cp949')
for line in fp.readlines():
    line = line.strip()
    x = line.split(".")
    mydict[x[0]] = x[1]

fp.close()

print(mydict)




