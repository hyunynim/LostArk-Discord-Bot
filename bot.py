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
		if msg[0] == "!뻐큐":
			await message.channel.send("맛있네요!")
		elif msg[0] == "!공포의로붕이":
			await message.channel.send("저런.. 또 실패하셨나요?")
		elif msg[0] == "!ㅈㅁ":
			await message.channel.send("마스터께서는 아라드 대륙을 수호하고 계세요!")
		elif msg[0] == "!함말뚝":
			await message.channel.send("그는 완벽한 멸시장인이에요!")
		elif msg[0] == "!단새론":
			if random.randrange(1, 10) < 3:
				await message.channel.send("그녀는 지금 예민해졌어요!")
			else:
				await message.channel.send("잠시 소강상태가 되었어요!")
		elif msg[0] == "!이호진":
			await message.channel.send("장인의 기운이 쌓이고 있어요!")
		elif msg[0] == "!전사김종성":
			await message.channel.send("그는 크고 거대해요!")
		elif msg[0] == "!전김":
			await message.channel.send("그는 크고 거대해요!")
		elif msg[0] == "!당진스라소니":
			await message.channel.send("또 쌀먹하러 오셨네요!")
		elif msg[0] == "!동물맨":
			await message.channel.send("또 쌀먹하러 오셨네요!")
		elif msg[0] == "!아르카라마":
			await message.channel.send("모코코 좀 그만 캐세요!")
		elif msg[0] == "!짱쭌이":
			await message.channel.send("사사게를 리프레쉬 해봐야겠어요!")
		elif msg[0] == "!전정":
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
		elif msg[0] == "!마리":
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
		elif msg[0] == "!주사위":
			r = random.randrange(1,100)
			await message.channel.send(message.author.name + "님의 주사위는 ~~~~ " + repr(r) + " 입니다. (1-100)")
			if r <= 10:
				await message.channel.send("ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ")
		elif msg[0] == "!로붕이":
			r = random.randrange(1,100)
			await message.channel.send("로붕이 님의 강화 성공확률은 ~~~~ " + repr(r) + " 입니다.")
			if r <= 10:
				await message.channel.send("ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ")
		elif msg[0] == "!미스틱":
			await message.channel.send("아크 숨결 당첨자는~~~~~~~~~~~")
			resStr = ""
			time.sleep(2 + random.randrange(2, 4))
			mystic = [1, 2, 3, 4, 5, 6, 7, 8]
			random.shuffle(mystic)
			for i in range(0, 3):
				resStr += repr(mystic[i]) + "번 "
			await message.channel.send(":star2: " + resStr + ":star2:")
		elif msg[0] == "!캘린더":
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
		elif msg[0] == "!골드":
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

		else:
			await message.channel.send("아직 정신개조를 받는 중이라 모르는 단어가 많아요!")
			str = "```*---명령어---*\n"
			str += "!주사위 !전정 [닉네임] !마리 [크리스탈 구매 가격] !캘린더 !미스틱 !골드 [크리스탈 판매 가격]\n\n"
			str += "*---정보---*\n"
			str += "!뻐큐 !공포의로붕이 !ㅈㅁ !함말뚝 !단새론 !이호진 !전사김종성 !전김 !당진스라소니 !동물맨 !아르카라마 !짱쭌이 !로붕이```"
			await message.channel.send(str)

client.run("TOKEN")
