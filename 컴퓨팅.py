#리스트 추가: append
#리스트 삭제: remove
#항목이 리스트 안에 있는지 체크: if ~ in ~
#리스트 삭제: del ~
#리스트 마지막 항목: pop
#리스트 탐색하기: index(순서가 나타남)
#리스트 정렬하기: sort
#해당되는 값의 개수: count
#리스트의 길이: len


#스택: 들어간 순서대로 출력
#큐: 가장 최근에 입력된 것부터 출력
#isalpha: 문자열이 알파벳인지 아닌지 판별함
#'while qu:' 의 이유 : qu의 리스트가 없어질 때까지 반복

player = {"name":"anemone",
        "gender":"male",
        "job":"magician",
        "level":"999",}


key = input("접근하고자 하는 키:")

if key in player:
    print(player[key])

elif key not in player:
    print("잘못입력했습니다.")
'''value = player.get("존재하지 않는 키")
print("value")
if value == None:
    print("존재하지 않는 키에 접근했습니다.")'''