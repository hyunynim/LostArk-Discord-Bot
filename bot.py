import discord
import asyncio
import urllib.request
from bs4 import BeautifulSoup
from urllib import parse
import random
import time

client = discord.Client()
gold = 0

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("정신개조 의자에 앉아서 생각")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
        if message.content.startswith("!"):
                msg = message.content.split(" ")
                msg[0] = msg[0][1:]
                if msg[0] == "뻐큐":
                        await message.channel.send("맛있네요!")
                elif msg[0] == "공포의로붕이":
                        await message.channel.send("저런.. 또 실패하셨나요?")
                elif msg[0] == "등장":
                        await message.channel.send("-비슈타르-")
                elif msg[0] == "ㅈㅁ":
                        await message.channel.send("마스터께서는 아라드 대륙을 수호하고 계세요!")
                elif msg[0] == "함말뚝":
                        await message.channel.send("그는 완벽한 멸시장인이에요!")
                elif msg[0] == "단새론":
                        if len(msg) < 2:
                                if random.randrange(1, 10) <= 5:
                                        await message.channel.send("그녀는 지금 예민해졌어요!")
                                else:
                                        await message.channel.send("잠시 소강상태가 되었어요!")
                        else:
                                if msg[1] == "강화":
                                        r = random.randrange(1,100)
                                        await message.channel.send("단새론 님의 강화 성공확률은 ~~~~ " + repr(r) + " 입니다.")
                                        if r <= 10:
                                                await message.channel.send("ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ")
                elif msg[0] == "이호진":
                        await message.channel.send("장인의 기운이 쌓이고 있어요!")
                elif msg[0] == "전사김종성":
                        await message.channel.send("그는 크고 거대해요!")
                elif msg[0] == "전김":
                        await message.channel.send("그는 크고 거대해요!")
                elif msg[0] == "당진스라소니":
                        await message.channel.send("또 쌀먹하러 오셨네요!")
                elif msg[0] == "동물맨":
                        await message.channel.send("또 쌀먹하러 오셨네요!")
                elif msg[0] == "아르카라마":
                        await message.channel.send("모코코 좀 그만 캐세요!")
                elif msg[0] == "짱쭌이":
                        if len(msg) < 2:
                                await message.channel.send("사사게를 리프레쉬 해봐야겠어요!")
                        else:
                                if msg[1] == "강화":
                                        r = random.randrange(1,100)
                                        await message.channel.send("짱쭌이 님의 강화 성공확률은 ~~~~ " + repr(r) + " 입니다.")
                                        if r <= 10:
                                                await message.channel.send("ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ")
                elif msg[0] == "비슈타르":
                        await message.channel.send("등장!")
                elif msg[0] == "전정":
                        resText = "```"
                        profileUrl = "https://lostark.game.onstove.com/Profile/Character/"
                        await message.channel.send(msg[1] + "님의 전투정보실 링크에요!\n" + profileUrl + msg[1] + "\n각인은 제대로 표시되지 않을 수 있다는 점! 알아두세용!\n")
                        encStr = parse.quote(msg[1])
                        profileUrl = profileUrl + encStr
                        req = urllib.request.urlopen(profileUrl)
                        res = req.read()

                        soup = BeautifulSoup(res, 'html.parser')  # BeautifulSoup 객체생성

                        loahaeUrl = "https://loahae.com/profile/"
                        loahaeUrl = loahaeUrl + encStr
                        req2 = urllib.request.urlopen(loahaeUrl)
                        res2 = req2.read()
                        soup2 = BeautifulSoup(res2, 'html.parser')  # BeautifulSoup 객체생성
                        serverName = soup.find_all('div', class_='game-info__server')
                        serverName = [each_line.get_text().strip() for each_line in serverName[:20]]
                        guildName = soup.find_all('div', class_='game-info__guild')
                        guildName = [each_line.get_text().strip() for each_line in guildName[:20]]
                        className = soup.find_all('div', class_='game-info__class')
                        className = [each_line.get_text().strip() for each_line in className[:20]]
                        levelInfoItem = soup.find_all('div', class_='level-info__item')
                        levelInfoItem = [each_line.get_text().strip() for each_line in levelInfoItem[:20]]
                        levelInfoExpd = soup.find_all('div', class_='level-info__expedition')
                        levelInfoExpd = [each_line.get_text().strip() for each_line in levelInfoExpd[:20]]
                        ability = soup.find_all('div', class_='profile-ability-basic')
                        ability = [each_line.get_text().strip() for each_line in ability[:20]]
                        abilArray = ability[0].split('\n')
                        resText += msg[1] + "[" + serverName[0][3:] + "/" + guildName[0][2:] + "] - " + className[0][3:] + "\n"
                        resText += "레벨: " + levelInfoItem[0][6:] + "(" + levelInfoExpd[0][6:] + ")" + "\n"
                        abil1 = ""
                        for i in abilArray:
                                if '힘 ' in i[:2] or '지능 ' in i[:2] or '체력 ' in i[:4]:
                                        abil1 = abil1 + i + "\n"
                        resText += abil1 + "\n"

                        abilityBattle = soup.find_all('div', class_='profile-ability-battle')
                        abilityBattle = [each_line.get_text().strip() for each_line in abilityBattle[:]]
                        abil2Array = abilityBattle[0].split('\n')
                        abil2 = ""
                        for i in abil2Array:
                                if '치명 ' in i[:4] or '특화 ' in i[:4] or '제압 ' in i[:4] or '신속 ' in i[:4] or '인내 ' in i[:4] or '숙련 ' in i[:4]:
                                        abil2 = abil2 + i + "\n"
                        resText += abil2 + "\n"

                        abilityEngrave = soup.find_all('div', class_='profile-ability-engrave')
                        abilityEngrave = [each_line.get_text().strip() for each_line in abilityEngrave[:]]
                        abil3Array = abilityEngrave[0].split('\n')
                        abil3 = ""
                        for i in abil3Array:
                                if 'Lv' in i or '펫' in i[:4]:
                                        abil3 += i + "\n"
                        resText += abil3 + "\n"
                        rank1 = soup2.find_all('div', class_='infobox infobox-l')
                        rank1 = [each_line.get_text().strip() for each_line in rank1[:10]]
                        for i in rank1:
                                for j in i.split("\n"):
                                        resText += j + " - "
                                resText = resText[:len(resText) - 2]
                                resText += "\n"
                        rank2 = soup2.find_all('div', class_='infobox infobox-r')
                        rank2 = [each_line.get_text().strip() for each_line in rank2[:10]]
                        for i in rank2:
                                for j in i.split("\n"):
                                        resText += j + " - "
                                resText = resText[:len(resText) - 2]
                                resText += "\n"
                        resText += "```"
                        await message.channel.send(resText)
                elif msg[0] == "마리":
                        gold = 0
                        if len(msg) < 2:
                                await message.channel.send("명령어를 !마리 [현재 크리스탈 구매 가격]으로 입력하면 마리의 상점 가격을 골드로 환산할 수 있어요!")
                        elif msg[1].isdigit():
                                gold = int(msg[1])
                        else:
                                await message.channel.send("명령어를 !마리 [현재 크리스탈 구매 가격]으로 입력하면 마리의 상점 가격을 골드로 환산할 수 있어요!")
                        mariUrl = "https://lostark.game.onstove.com/Shop/Mari"
                        req = urllib.request.urlopen(mariUrl)
                        res = req.read()
                        soup = BeautifulSoup(res, 'html.parser')  # BeautifulSoup 객체생성
                        itemName = soup.find_all('span', class_='item-name')  # 데이터에서 태그와 클래스를 찾는 함수
                        itemName = [each_line.get_text().strip() for each_line in itemName[:20]]
                        itemPrice = soup.find_all('span', class_='amount')  # 데이터에서 태그와 클래스를 찾는 함수
                        itemPrice = [each_line.get_text().strip() for each_line in itemPrice[:20]]
                        str = "```"
                        for i in range(0, 6):
                                str += itemName[i] + "[크리스탈 " + itemPrice[i] + "개] = " + repr(int(int(itemPrice[i]) * (gold / 95.0))) + "골드\n"
                        str += "```"
                        await message.channel.send(str)
                elif msg[0] == "주사위":
                        r = random.randrange(1,100)
                        await message.channel.send(message.author.name + "님의 주사위는 ~~~~ " + repr(r) + " 입니다. (1-100)")
                        if r <= 10:
                                await message.channel.send("ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ")
                elif msg[0] == "로붕이":
                        r = random.randrange(1,100)
                        await message.channel.send("로붕이 님의 강화 성공확률은 ~~~~ " + repr(r) + " 입니다.")
                        if r <= 10:
                                await message.channel.send("ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ")
                elif msg[0] == "미스틱":
                        await message.channel.send("아크 숨결 당첨자는~~~~~~~~~~~")
                        resStr = ""
                        time.sleep(2 + random.randrange(2, 4))
                        mystic = [1, 2, 3, 4, 5, 6, 7, 8]
                        random.shuffle(mystic)
                        for i in range(0, 3):
                                resStr += repr(mystic[i]) + "번 "
                        await message.channel.send(":star2: " + resStr + ":star2:")
                elif msg[0] == "캘린더":
                        url = "http://m.inven.co.kr/lostark/timer/"
                        req = urllib.request.urlopen(url)
                        res = req.read()
                        soup = BeautifulSoup(res, 'html.parser')  # BeautifulSoup 객체생성
                        str = "```이제 곧 시작되는 10개의 캘린더입니다.\n"
                        tm = soup.find_all('a', class_='info')
                        tm = [each_line.get_text().strip() for each_line in tm[:10]]
                        for i in tm:
                                for j in i.split("\n"):
                                        str += j + " - "
                                str = str[:len(str) - 2]
                                str += "\n"
                        str += "```"
                        await message.channel.send(str)
                elif msg[0] == "골드":
                        gold = 0
                        if len(msg) < 2:
                                await message.channel.send("명령어를 !골드 [크리스탈 판매 가격]으로 입력하면 어떻게 골드를 구매하는 것이 더 흑우가 될 수 있는 지 알 수 있어요!")
                        elif msg[1].isdigit():
                                gold = int(msg[1])
                                str = "```"
                                str += "로얄 크리스탈로 구매 시 100골드당 " + repr(int(2750 / (gold / 100.0))) + "원 + 마일리지\n"
                                str += "로얄 크리스탈 에그머니로 구매 시 100골드당 " + repr(int(2475 / (gold / 100.0))) + "원 + 마일리지```"
                                await message.channel.send(str)
                        else:
                                await message.channel.send("명령어를 !골드 [크리스탈 판매 가격]으로 입력하면 어떻게 골드를 구매하는 것이 더 흑우가 될 수 있는 지 알 수 있어요!")
                elif msg[0] == "강화":
                        if len(msg) < 2:
                                await message.channel.send("명령어를 !강화 [확률]로 입력하면 강화 시뮬레이션을 해볼 수 있어요!")
                        elif msg[1].isdigit():
                                r = random.randrange(1,100)
                                await message.channel.send("강화 결과는...")
                                time.sleep(2 + random.randrange(2, 4))
                                await message.channel.send("성공!" if r <= int(msg[1]) else "장인의 기운이 쌓여가네요..")
                        else:
                                await message.channel.send("명령어를 !골드 [크리스탈 판매 가격]으로 입력하면 어떻게 골드를 구매하는 것이 더 흑우가 될 수 있는 지 알 수 있어요!")
                elif msg[0] == "정보":
                        url = "https://github.com/hyunynim/LostArk-Discord-Bot/blob/master/README.md"
                        req = urllib.request.urlopen(url)
                        res = req.read()
                        soup = BeautifulSoup(res, 'html.parser')  # BeautifulSoup 객체생성
                        str = "```유머 노예봇 정보입니다.\n"
                        info = soup.find_all('article', class_='markdown-body entry-content p-3 p-md-6')
                        info = [each_line.get_text().strip() for each_line in info[:]]
                        for i in info:
                                str += i
                        str += "```"
                        await message.channel.send(str)
                        await message.channel.send("이 내용은 https://github.com/hyunynim/LostArk-Discord-Bot/blob/master/README.md 에서도 확인할 수 있습니다.")
                elif msg[0] == "p" or msg[0] == "s" or ('0' <= msg[0][1] and msg[0][1] <= '9'):
                        print('Music bot skip mode')
                elif msg[0] == "길드원":
                        try:
                                f = open("memberList.csv", 'r')
                        except:
                                await message.channel.send("```\n길드원 목록을 불러올 수 없습니다.\n@길드원업데이트 명령어를 이용하여 목록을 업데이트해주세요\n```")
                                return
                        resText = "```\n현재까지 추가된 길드원 목록입니다.\n"
                        memberList = f.readlines()
                        for member in memberList:
                                l = member.split(',')
                                for str in l:
                                        resText += str
                                        resText += "\t"
                        f.close()
                        resText += "```"
                        await message.channel.send(resText)
                        await message.channel.send(file=discord.File("memberList.csv"))
                elif msg[0] == "길드원업데이트":
                        await message.channel.send("```\n길드원 목록을 업데이트합니다.\n업데이트에는 다소 시간이 소요될 수 있습니다.```")
                        f = open("member.txt", 'r')
                        f2 = open("memberList.csv", 'w')
                        member = f.readlines()
                        for name in member:
                                profileUrl = "https://lostark.game.onstove.com/Profile/Character/"
                                name = name.rstrip()
                                encStr = parse.quote(name)
                                profileUrl = profileUrl + encStr
                                req = urllib.request.urlopen(profileUrl)
                                res = req.read()
                                soup = BeautifulSoup(res, 'html.parser')  # BeautifulSoup 객체생성
                                className = soup.find_all('div', class_='game-info__class')
                                className = [each_line.get_text().strip() for each_line in className[:20]]
                                levelInfoItem = soup.find_all('div', class_='level-info__item')
                                levelInfoItem = [each_line.get_text().strip() for each_line in levelInfoItem[:20]]
                                levelInfoItem[0] = levelInfoItem[0][6:].replace(",","")
                                tmpList = levelInfoItem[0].split(".")
                                level = tmpList[0]
                                f2.writelines(name + "," + className[0][3:] + "," + level + "\n")
                        f.close()
                        f2.close()
                        await message.channel.send("```\n길드원 목록 업데이트가 완료되었습니다.\n@길드원 명령어를 통해 확인하실 수 있습니다.\n```")
                elif msg[0] == "길드원추가":
                        chk = 0
                        f = open("member.txt", 'r')
                        member = f.readlines()
                        f.close()
                        for name in member:
                                name = name.rstrip()
                                if name == msg[1]:
                                        await message.channel.send("이미 추가된 길드원입니다.")
                                        chk = 1
                                        break
                        if chk == 0:
                                f = open("member.txt", 'w')
                                for name in member:
                                        name = name.rstrip()
                                        f.write(name + "\n")
                                f.write(msg[1] + "\n")
                                await message.channel.send("추가되었습니다.")
                                f.close()
                elif msg[0] == "길드원삭제":
                        f = open("member.txt", 'r')
                        member = f.readlines()
                        f.close()
                        f = open("member.txt", 'w')
                        for name in member:
                                name = name.rstrip()
                                if name == msg[1]:
                                        continue
                                else:
                                        f.write(name + "\n")
                        f.close()
                        await message.channel.send("삭제되었습니다.")
                else:
                        await message.channel.send(msg)
                        str = "```\n!정보\n*---명령어---*\n"
                        str += "!주사위 !전정 [닉네임] !마리 [크리스탈 구매 가격] !캘린더 !미스틱 !골드 [크리스탈 판매 가격\n"
                        str += "!강화 [확률]] !길드원 !길드원업데이트 !길드원추가 [닉네임] !길드원삭제 [닉네임]\n\n"
                        str += "*---정보---*\n"
                        str += "!뻐큐 !공포의로붕이 !ㅈㅁ !함말뚝 !단새론 !이호진 !전사김종성 !전김 !당진스라소니 !동물맨 !아르카라마 !짱쭌이 !로붕이```"
                        await message.channel.send(str)
client.run("TOKEN")
