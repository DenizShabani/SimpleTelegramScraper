from telethon.sync import TelegramClient
from telethon.tl.types import UserStatusRecently
import csv

API_ID = 0000000 # API_ID as an integer
API_HASH = "0000000000000000000" # API_HASH as a string
PHONE = "000000000" # Phone number as a string without + or 00 /Ex: 12025550163
GROUP_NAME = "group_username" # Group username /Ex: for t.me/random then write random

c = TelegramClient("session", API_ID,API_HASH)
c.start(PHONE)
group = c.get_entity("cryptoshiller31")
members = c.get_participants(GROUP_NAME)
print(f"\n{len(members)} users were scraped.\n")

choice = input("Would you like to only obtain the users last seen recently? [y/n] ")
if choice == "y" or "Y":
    new_scraped = []
    for user in members:
        if user.deleted or user.bot or user.scam or not user.status == UserStatusRecently():
            user = []
        else:
            new_scraped.append(user)
    scraped = new_scraped


with open("members\\members.csv", "w", encoding='UTF-8') as f:
    writer = csv.writer(f, delimiter=",", lineterminator="\n")
    writer.writerow(['username', 'user id', 'access hash', 'group', 'group id'])
    if choice == 'y' or 'Y':
        for member in members:
            if member.status == UserStatusRecently():
                if member.username:
                    username = member.username
                else:
                    username = ''
                writer.writerow([username, member.id, member.access_hash, group.title, group.id])
    else:
        for member in members:
            if member.username:
                username = member.username
            else:
                username = ''
            writer.writerow([username, member.id, member.access_hash, group.title, group.id])
f.close()

print(f"\n{len(new_scraped)} users are left and saved in the csv file.\n")