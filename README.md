# LostArk-Discord-Bot
파이썬 문법 연습 + 크롤링 연습
# 2020.03.16
 * @길드원... 명령어 !길드원... 명령어로 대체
 * !길드원업데이트 추가
    - 길드원 목록을 txt로 관리하여 길드원을 불러올때마다 매번 크롤링 하던 작업을 로컬에서 처리하도록 수정
    - 해당 명령어 입력시 기존 @길드원 명령어가 하던 작업 대체
 * !길드원 명령어 수정
    - 해당 명령어 입력시 memberList.txt로부터 길드원 리스트를 읽어와서 출력해줌
# 2020.03.05
 * ~~@길드원, @길드원추가 [닉네임], @길드원삭제 [닉네임] 기능 추가
    - ~~@길드원 명령어 입력 시 미리 저장해둔 길드원들의 닉네임을 가지고 크롤링
    - ~~상당히 느림;; 수정예정
# 2020.02.10
 * Music bot 대응 업데이트
    - !p !s 명령어 입력 시, 존재하지 않는 명령어 문구 출력 제거
# 2020.02.08
 * !강화 명령어 추가
    - !강화 [확률] 입력 시 강화 시뮬레이션
# 2020.02.05
 * ~~!골드 명령어 추가~~
    - ~~마리 상점 연계하여 손익 계산(예정)~~
 * !골드 명령어 삭제
 * !마리 명령어 수정
    - !마리 [크리스탈 구매 가격] 입력 시, 현재 마리의 비밀상점에 있는 목록의 아이템들을 골드 가격으로 환산해줌
 * !골드 명령어 추가
    - !골드 [크리스탈 판매 가격] 입력 시, 로얄 크리스탈 또는 에그머니로 구매할 수 있는 골드의 가격 출력
 * !전정 명령어 수정
    - Markdown으로 출력되도록 수정
# 2020.02.04
 * First Release
 * 코드 효율성 낮음
 * 수정할 코드 많음
 * 코드 readability 낮음
 * !주사위 명렁어 추가
    - 1~100까지 무작위 숫자 출력
 * !전정 [닉네임] 명령어 추가
    - 전투 정보실의 기본 정보들 출력 (랭킹 포함)
 * !마리 명령어 추가
    - 마리의 비밀상점 목록 출력
 * !캘린더 명령어 추가
    - 곧 시작하는 캘린더의 이벤트 10개를 출력
 * !미스틱 명령어 추가
    - 1~8번 중 무작위 3명을 중복 없이 출력 (아크 숨결 당첨)
