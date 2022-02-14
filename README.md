# SimpleTelegramScraper

This simple python script scrapes accounts from public groups via Telegram API and saves them in a CSV file with their username, usersID, access hash, groupName, groupID and last seen online.

You can choose to scrape all members, active members(users online today and yesterday), members active in the last week, past month or not active members.

It can scrape more than 95% of users in a group! Bots are not included in the CSV file. The admins are also saved separately on admins.csv file.

It can sometimes occur that towards the end a bug occurs due to FloodWaitError, however, by this time more than 95% of users are already scraped :)

IT ONLY WORKS FOR PUBLIC GROUPS!!!

# How to use

* Install Requirements

`pip install -r requirements.txt`

* Change the literals in the beginning of the script as explained in the script(API_ID, API_HASH, PHONE, GROUP_NAME)

* Run the command

`python main.py`

# Buy me a coffee

If you liked this and would like to see more projects of a similar nature then I would really appreciate it if you support me. If you cannot then please starr this project :D

For crypto donations please contact me :)

https://www.buymeacoffee.com/denizshabani

# Warning

* This tool is official and completely free to use. Do not buy if anyone tries to sell by copying script

# News

* If you need any help then please write in this groupchat https://t.me/GitHubScriptsHelp
