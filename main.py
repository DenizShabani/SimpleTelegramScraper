from telethon.sync import TelegramClient
from telethon.tl.types import UserStatusRecently
import csv
from time import sleep
from telethon.tl.functions.channels import GetFullChannelRequest

API_ID = 00000000 # API_ID as an integer
API_HASH = "00000000000000000000" # API_HASH as a string
PHONE = "00000000000000000000" # Phone number as a string without + or 00 /Ex: 12025550163
GROUP_NAME = "" # Group username /Ex: for t.me/random then write random

c = TelegramClient("session", API_ID,API_HASH)
c.start(PHONE)
group = c.get_entity(GROUP_NAME)

choice = input("Would you like to only obtain the users last seen recently? [y/n] ")
members = []
members = c.iter_participants(group, aggressive = True)

channel_full_info = c(GetFullChannelRequest(group))
cont = channel_full_info.full_chat.participants_count

with open("members\\members.csv", "w", encoding='UTF-8') as f:
    writer = csv.writer(f, delimiter=",", lineterminator="\n")
    writer.writerow(['username', 'user id', 'access hash', 'group', 'group id'])
    if choice == 'y' or choice =='Y':
        for index,member in enumerate(members):
            print(f"{index+1}/{cont}", end="\r")
            if index%100 == 0:
                sleep(3)
            if member.status == UserStatusRecently():
                if member.username:
                    username = member.username
                else:
                    username = ''
                writer.writerow([username, member.id, member.access_hash, group.title, group.id])
    else:
        for index,member in enumerate(members):
            print(f"{index+1}/{cont}", end="\r")
            if index%100 == 0:
                sleep(3)
            if member.username:
                username = member.username
            else:
                username = ''
            writer.writerow([username, member.id, member.access_hash, group.title, group.id])
f.close()

print(f"\nUsers saved in the csv file.\n")
