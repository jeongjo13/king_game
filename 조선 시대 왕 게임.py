import time
import sys
import re

exp = 0 #자신의 현재 경험치 변수
level = 1 #자신의 현재 레벨 변수
nickname = "undefined" #자신의 닉네임
new_start = True #게임을 처음 플레이하는 사용자인지 아닌지
temp = "" #input 받을 때 임시로 값을 저장해 두는 곳
coin = 0 #게임 코인 개수
soldier = 0 #병사 인원 수
servant_list = ["정도전", "황희", "맹사성", "한명회", "신숙주", "김수온", "한백륜", "윤사분", "임사홍", "박원종"]
my_servant_list = ["정도전"]
prince = False #세자 책봉 여부
file_path = "data.txt"

def set_nickname() : #닉네임 설정 함수
    while True : #닉네임이 정상적으로 설정되어 return 명령이 실행되기 전까지는 계속 닉네임 설정 과정만 하기
        nickname_input = input("영어와 숫자로만 된 닉네임을 설정해 주세요: ")
        nickname_check = nickname_input.isalnum() #닉네임이 영어와 숫자로만 이루어져 있는지 확인
        if nickname_check == True : #닉네임이 영어와 숫자로만 이루어져 있다면
            return nickname_input #닉네임 설정값 반환 (추후 "닉네임을 %s로 설정할까요?"와 같은 확인 창도 개발 예정)
        else :
            print("닉네임에는 영어 또는 숫자만 사용할 수 있습니다. 다시 설정해 주세요.") #닉네임 다시 설정 필요
            time.sleep(1)

def set_current_level() : #경험치 값을 통해 현재 레벨을 계산해 주는 함수
    level = exp / 5000 + 1

print("환영합니다! 이 게임은 조선 시대 왕의 삶을 체험해 볼 수 있는 게임입니다.") #게임 설명
time.sleep(2)
temp = input("백업된 게임 파일이 있나요? 있으면 \'예\', 없으면 \'아니오\'\n답변을 입력하세요: ")
if temp == "예" : #게임 백업 파일 불러오기 (아직 미구현)
    print("죄송합니다. 아직 게임 저장 및 불러오기 기능이 지원되지 않습니다.")
else : #게임 초기 셋팅
    print("게임이 처음이시군요! 우선 닉네임부터 설정해 주세요.")
    time.sleep(1)
    nickname = set_nickname() #set_nickname 함수에서 닉네임 설정하고 반환된 값을 닉네임으로 설정
    print("닉네임이 %s(으)로 설정되었습니다. 멋진 닉네임이네요!" % nickname) #닉네임 설정 완료 안내
    print("자, 이제 시작해 볼까요?")

#여기까지 게임 초기 실행 과정
#여기부터 게임하는 거

while True :
    set_current_level()
    print("현재 레벨: %s (%s / %s)\n현재 코인: %s\n현재 병사 수: %s" % (level, exp, level * 5000, coin, soldier))
    temp = input("어느 게임을 하시겠습니까? 1. 정무 처리 / 2. 새로운 신하 등용 / 3. 전투 / 4. 상점 / 5. 세자 책봉 / 6. 게임 종료 / 7. 백업")
    if temp == "1" : #정무 처리
        print("아직 개발 중인 기능입니다. 조금만 기다려 주세요.")
    elif temp == "2" : #새로운 신하 등용
        print("새로운 신하 등용하기: ")
        temp = input("새로운 신하 등용 방식은 두 가지가 있습니다. '렌덤 등용' 또는 '선택 등용' 중 하나를 선택하세요. 렌덤 등용에는 300 코인이, 선택 등용에는 500 코인이 필요합니다.")
        if temp == "렌덤 등용" :
            print("아직 개발 중인 기능입니다. 조금만 기다려 주세요.")
        elif temp == "선택 등용" :
            print("아직 개발 중인 기능입니다. 조금만 기다려 주세요.")
    elif temp == "3" :
        print("아직 개발 중인 기능입니다. 조금만 기다려 주세요.")
    elif temp == "4" :
        print("아직 개발 중인 기능입니다. 조금만 기다려 주세요.")
    elif temp == "5" :
        if prince == False : 
            temp = input("왕자를 세자로 책봉하시겠습니까? 1000 코인이 소모됩니다.\'예\' 또는 \'아니오\' 입력: ")
            if temp == "예" :
                if coin >= 1000 :
                    prince = True
                    print("세자 책봉 완료. 이제 세자를 교육시켜 보세요!")
                else :
                    print("코인이 부족합니다. 다시 시도하세요.")
        else :
            print("아직 개발 중인 기능입니다. 조금만 기다려 주세요.")
    elif temp == "6" :
        sys.exit()
    elif temp == "7" :
        print("게임을 파일에 저장하는 중...")
        with open(file_path, "w") as file :
            file.write("%d %d %s %d %d" % (exp, level, nickname, coin, soldier))
        print("저장 완료. 중요: 아직 신하 목록 저장은 지원되지 않습니다.")
