from urllib.request import urlopen
import json
url = "https://tmi.twitch.tv/group/user/mizkif/chatters"
response = urlopen(url)
data_json = json.loads(response.read())
chatters = data_json["chatters"]
viewers = chatters["viewers"]

url = "https://gist.githubusercontent.com/ErobbDaily/3a56e08909fb86ae296a145e89cb8170/raw/9c92b70694766bf4a6738084472ea626aabeccce/gistfile1.txt"
response = urlopen(url)
data_json = json.loads(response.read())
names = data_json["names"]

botList=[]

for x in range(len(viewers)):
	for y in range(len(names)):
		try:
			if viewers[x].startswith(names[y]):
				viewer = viewers[x].replace(names[y],"")
				if viewer[0].isnumeric():
					viewer=viewer[1:]
					if viewer[0].isalpha():
						viewer=viewer[1:]
						for z in range(len(names)):
							if viewer.startswith(names[z]):
								print(viewers[x])
								botList.append(viewers[x])
								pass
		except:
			pass		


import time
print(len(botList))
with open("Mizkif_Bot_List.txt", "a") as text_file:
    print(time.time(),": ",len(botList),"\n", file=text_file)


