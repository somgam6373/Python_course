#리스트 추가: append
#리스트 삭제: remove
#항목이 리스트 안에 있는지 체크: if ~ in ~
#리스트 삭제: del ~
#리스트 마지막 항목: pop
#리스트 탐색하기: index(순서가 나타남)
#리스트 정렬하기: sort
#해당되는 값의 개수: count
#리스트의 길이: len



score = [50, 30, 90, 70, 60]
idx, val, cnt = 0, 0, 0

print("현재 입력된 점수는")
print(score, "이고, 모두", len(score), '개 입니다.')

print()
print("append 연습")
val = int(input('append 할 값 : '))
score.append(val)
print(score)

print()
print("insert 연습")
idx = int(input("insert할 위치 : "))
val = int(input("insert 할 값 : "))
score.append(val)
print(score)

print()
print("index 연습")
val = int(input("찾고 싶은 값 : "))
idx = score.index(val)
print(score)
print("%d는 %d번째 위치하고 있습니다." % (val, idx))

print()
print("remove 연습")
val = int(input("삭제하고 싶은 값 : "))
score.remove(val)
print(score)

print()
print("del 연습")
idx = int(input("삭제할 위치 : "))
del(score[idx])
print(score)

print()
print("count 연습")
val = int(input("갯수를 알고 싶은 값 : "))
cnt = score.count(val)
print(score)
print("%d는 %d번 나옵니다." %(val, cnt))

print()
print("reverse sort 연습")
score.reverse()
print(score)