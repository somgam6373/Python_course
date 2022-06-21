dic = {"A":['a1','a2','a3'], 'B':['b1','b2']}

for i in range(1):
    num = input(":")
    dic["B"] = ["b1",'b2',num]
    
    for key, value in dic.items():
        if 'b3' in value:
            print(key)