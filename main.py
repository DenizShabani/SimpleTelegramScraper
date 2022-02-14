'''
=============TELEGRAM SCRAPER===================
Public group scraper
Coded by- github.com/denizshabani
Apologies if anything in the code is dumb :)
Will try maintaining as much as possible :)
Copy with credits
************************************************
'''


from types import NoneType
from telethon.sync import TelegramClient
from telethon.tl.types import UserStatusRecently, ChannelParticipantsAdmins, UserStatusLastMonth, UserStatusLastWeek, UserStatusOffline, UserStatusOnline, UserStatusEmpty
import csv
from time import sleep
from telethon.tl.functions.channels import GetFullChannelRequest
import datetime
from colorama import Fore,Style

r = Fore.RED
g = Fore.GREEN
b = Fore.BLUE
d = Style.RESET_ALL

today = datetime.datetime.now()
yesterday = today - datetime.timedelta(days=1)

API_ID = 0000000000000 # API_ID as an integer
API_HASH = "00000000000" # API_HASH as a string
PHONE = "00000000000" # Phone number as a string without + or 00 /Ex: 12025550163
GROUP_NAME = "0000000000000" # Group username /Ex: for t.me/random then write random

c = TelegramClient("session", API_ID,API_HASH)
c.start(PHONE)
group = c.get_entity(GROUP_NAME)

choice = int(input(f"\n{g}How would you like to obtain the users?\n\n{r}[{b}0{r}]{g} All users\n{r}[{b}1{r}]{g} Active Users(online today and yesterday)\n{r}[{b}2{r}]{g} Users active in the last week\n{r}[{b}3{r}]{g} Users active in the last month\n{r}[{b}4{r}]{g} Non-active users(not active in the last month) \n\nYour choice: "))
members = []
members = c.iter_participants(group, aggressive=True)

channel_full_info = c(GetFullChannelRequest(group))
cont = channel_full_info.full_chat.participants_count

def write(group,member):
    if member.username:
        username = member.username
    else:
        username = ''
    if isinstance(member.status,UserStatusOffline):
        writer.writerow([username, member.id, member.access_hash, group.title, group.id,member.status.was_online])
    else:
        writer.writerow([username, member.id, member.access_hash, group.title, group.id,type(member.status).__name__])


with open("members\\admins.csv", "w", encoding='UTF-8') as f:
    writer = csv.writer(f, delimiter=",", lineterminator="\n")
    writer.writerow(['username', 'user id', 'access hash', 'group', 'group id','status'])
    for member in c.iter_participants(group, filter=ChannelParticipantsAdmins):    
        if not member.bot:
            write(group,member)
f.close()

with open("members\\members.csv", "w", encoding='UTF-8') as f:
    writer = csv.writer(f, delimiter=",", lineterminator="\n")
    writer.writerow(['username', 'user id', 'access hash', 'group', 'group id','status'])
    if choice == 0:
        try:
            for index,member in enumerate(members):
                print(f"{index+1}/{cont}", end="\r")
                if index%100 == 0:
                    sleep(3)
                if not member.bot:
                    write(group,member)                   
        except:
            print("\nThere was a FloodWaitError, but check members.csv. More than 95%% of members should be already added.")
    elif choice == 1:
        try:
            for index,member in enumerate(members):
                print(f"{index+1}/{cont}", end="\r")
                if index%100 == 0:
                    sleep(3)
                if not member.bot:
                    if isinstance(member.status, (UserStatusRecently,UserStatusOnline)):
                        write(group,member)
                    elif isinstance(member.status,UserStatusOffline):
                        d = member.status.was_online                    
                        today_user = d.day == today.day and d.month == today.month and d.year == today.year
                        yesterday_user = d.day == yesterday.day and d.month == yesterday.month and d.year == yesterday.year
                        if today_user or yesterday_user:
                            write(group,member)
        except:
            print("\nThere was a FloodWaitError, but check members.csv. More than 95%% of members should be already added.")
    elif choice == 2:
        try:
            for index,member in enumerate(members):
                print(f"{index+1}/{cont}", end="\r")
                if index%100 == 0:
                    sleep(3)
                if not member.bot:
                    if isinstance(member.status, (UserStatusRecently,UserStatusOnline,UserStatusLastWeek)):
                        write(group,member)
                    elif isinstance(member.status,UserStatusOffline):
                        d = member.status.was_online
                        for i in range(0,7):
                            current_day = today - datetime.timedelta(days=i)
                            correct_user = d.day == current_day.day and d.month == current_day.month and d.year == current_day.year
                            if correct_user:
                                write(group,member)
        except:
            print("\nThere was a FloodWaitError, but check members.csv. More than 95%% of members should be already added.")
    elif choice == 3:
        try:
            for index,member in enumerate(members):
                print(f"{index+1}/{cont}", end="\r")
                if index%100 == 0:
                    sleep(3)
                if not member.bot:
                    if isinstance(member.status, (UserStatusRecently,UserStatusOnline,UserStatusLastWeek,UserStatusLastMonth)):
                        write(group,member)
                    elif isinstance(member.status,UserStatusOffline):
                        d = member.status.was_online
                        for i in range(0,30):
                            current_day = today - datetime.timedelta(days=i)
                            correct_user = d.day == current_day.day and d.month == current_day.month and d.year == current_day.year
                            if correct_user:
                                write(group,member)
        except:
            print("\nThere was a FloodWaitError, but check members.csv. More than 95%% of members should be already added.")
    elif choice == 4:
        try:
            all_users = []
            active_users = []
            for index,member in enumerate(members):
                print(f"{index+1}/{cont}", end="\r")
                all_users.append(member)
                if index%100 == 0:
                    sleep(3)
                if not member.bot:
                    if isinstance(member.status, (UserStatusRecently,UserStatusOnline,UserStatusLastWeek,UserStatusLastMonth)):
                        active_users.append(member)
                    elif isinstance(member.status,UserStatusOffline):
                        d = member.status.was_online
                        for i in range(0,30):
                            current_day = today - datetime.timedelta(days=i)
                            correct_user = d.day == current_day.day and d.month == current_day.month and d.year == current_day.year
                            if correct_user:                            
                                active_users.append(member)
            for member in all_users:
                if member not in active_users:
                    write(group,member)
        except:
            print("\nThere was a FloodWaitError, but check members.csv. More than 95%% of members should be already added.")
                
f.close()

print(f"\nUsers saved in the csv file.\n")
