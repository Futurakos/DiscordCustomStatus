# I AM IN NO WAY RESPONSIBLE FOR GETTING BANNED/TERMINATED ON DISCORD WITH THE USE OF THIS PROGRAM. DON'T ABUSE THEIR API AND SET A HIGH DELAY.

# DiscordCustomStatus
Simple Custom Status Changer For Discord Made By Me.

With this simple program you put in your token, you write some different sentences and the program chooses one randomly and sets it as your Custom Status.

# Example for Use
One use for this is for when you wanna let your friends you are sleeping, you use crontab (https://en.wikipedia.org/wiki/Cron) and you make it open in a specific time you are sleeping and it sets your status to: Sleeping.

# How it works
It sends a request to https://discordapp.com/api/v6/users/@me/settings with special parameters such as custom_status:"The text you put in the code in here"
