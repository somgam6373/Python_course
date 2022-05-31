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
  mydict[x[2]] = x[3:]

fp.close()

while (True):
    movie=input("영화이름 입력  (종료:0):")
    if (movie=='0'):
        break
    else:
        if movie in mydict.keys():
            v=mydict[movie]
            print("Company     : ",v[0])
            print("Release data:",v[1])
            print("Country     :",v[2])
            print("Total screen::",v[3])
            print("Profit      :",v[4])
            print("Total num   :",v[5])
            print("Grade       :",v[6])

            print("----------------------------------------------------------")
        else:
            print("데이터베이스에 없는 영화입니다")
            print("----------------------------------------------------------")