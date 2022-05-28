# animal = {"강아지":"dog","고양이":"cat","새":"bird","코끼리":"elephant"}

# while True:
#   word = input("단어를 입력하세요(종료:0):")
#   if word == "0":
#     print("종료되었습니다.")
#     break
#   elif word not in animal.keys():
#     print("사전에 없는 단어입니다.")
#   elif word in animal.keys(): 
#     print(word,":",animal[word])

mydict = {}  

fp = open("c:\\pythontest\\movie_data.txt","r",encoding='cp949')

for line in fp.readlines():
  line = line.strip()
  x = line.split('|')
  mydict[x[0]] = x[1], x[2], x[3], x[4], x[5], x[6], x[7] #value

fp.close()

while True:
  word = input("영화 이름 입력(종료:0):")
  if word == "0":
    print("종료되었습니다.")
    break

  elif word in mydict.keys(): 
    print(mydict[word])
    print("-----------------------------")
  elif word not in mydict.keys():
    print("데이터베이스에 없는 영화입니다")
    print("-----------------------------")