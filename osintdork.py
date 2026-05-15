#!/usr/bin/env python3
import os
import shutil
import subprocess

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def center_text(text):
    try:
        width = shutil.get_terminal_size().columns
    except:
        width = 80
    lines = text.split('\n')
    centered = []
    for line in lines:
        if line.strip():
            centered.append(line.center(width))
        else:
            centered.append('')
    return '\n'.join(centered)

def print_logo():
    logo = r"""
 ▒█████    ██████  ██▓ ███▄    █ ▄▄▄█████▓   ▓█████▄  ▒█████   ██▀███   ██ ▄█▀  ██████ 
▒██  ██▒▒██    ▒ ▓██▒ ██ ▀█   █ ▓  ██▒ ▓▒   ▒██▀ ██▌▒██▒  ██▒▓██ ▒ ██▒ ██▄█▒ ▒██    ▒ 
▒██░  ██▒░ ▓██▄   ▒██▒▓██  ▀█ ██▒▒ ▓██░ ▒░   ░██   █▌▒██░  ██▒▓██ ░▄█ ▒▓███▄░ ░ ▓██▄   
▒██   ██░  ▒   ██▒░██░▓██▒  ▐▌██▒░ ▓██▓ ░    ░▓█▄   ▌▒██   ██░▒██▀▀█▄  ▓██ █▄   ▒   ██▒
░ ████▓▒░▒██████▒▒░██░▒██░   ▓██░  ▒██▒ ░    ░▒████▓ ░ ████▓▒░░██▓ ▒██▒▒██▒ █▄▒██████▒▒
░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░░▓  ░ ▒░   ▒ ▒   ▒ ░░       ▒▒▓  ▒ ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░▒ ▒▒ ▓▒▒ ▒▓▒ ▒ ░
  ░ ▒ ▒░ ░ ░▒  ░ ░ ▒ ░░ ░░   ░ ▒░    ░        ░ ▒  ▒   ░ ▒ ▒░   ░▒ ░ ▒░░ ░▒ ▒░░ ░▒  ░ ░
░ ░ ░ ▒  ░  ░  ░   ▒ ░   ░   ░ ░   ░          ░ ░  ░ ░ ░ ░ ▒    ░░   ░ ░ ░░ ░ ░  ░  ░  
    ░ ░        ░   ░           ░                ░        ░ ░     ░     ░  ░         ░  
                                              ░                                        
"""
    print(center_text(logo))

def check_updates():
    clear_screen()
    print_logo()
    print("\n" + center_text("CHECKING FOR UPDATES"))
    try:
        subprocess.run(["git", "fetch"], check=False)
        result = subprocess.run(["git", "status", "-uno"], capture_output=True, text=True)
        if "behind" in result.stdout:
            print("\nUpdate available!")
            choice = input("Download update? (y/n): ").strip().lower()
            if choice == "y":
                subprocess.run(["git", "pull"])
                print("\nUpdate done. Restart the program.")
                input("Press Enter...")
                exit()
        else:
            print("\nYou have the latest version.")
    except:
        print("\nGit not found or not a git repo.")
    input("\nPress Enter...")

def generate_social_dorks(platform, name, city, birthdate):
    dorks = []
    if platform == "vk":
        dorks = [
            f"{name} вк OR vk", f"+{name} +вк -twitter", f"site:vk.com {name}",
            f'intitle:"{name} вк"', f'intitle:"{name} vk"', f'inurl:vk {name}',
            f'"{name} вк" | "{name} vk"', f"{name} (вк OR vk) -одноклассники",
            f"inurl:club {name} вк", f"inurl:public {name} vk", f"allintitle:{name} вк",
            f'intitle:"вк" intitle:"{name}"', f"site:vk.com intitle:\"{name}\"",
            f"{name} site:vk.com inurl:id", f'"{name}" +"вконтакте" | +"vk.com"',
            f"{name} (vk OR vkontakte) -site:twitter.com", f'intitle:"{name}" (вк | vk)',
            f'inurl:profile | inurl:user | inurl:id "{name}" (vk)',
        ]
    elif platform == "instagram":
        dorks = [
            f"{name} инстаграм OR instagram", f"+{name} +instagram -facebook", f"site:instagram.com {name}",
            f'intitle:"{name} инстаграм"', f'intitle:"{name} instagram"', f'inurl:instagram {name}',
            f'"{name} инстаграм" | "{name} instagram"', f"{name} (instagram OR инстаграм) -twitter",
            f"inurl:p {name} instagram", f"allintitle:{name} instagram", f'intitle:"instagram" intitle:"{name}"',
            f"site:instagram.com intitle:\"{name}\"", f"{name} site:instagram.com inurl:u",
            f'"{name}" +"instagram.com" | +"instagr"', f"{name} (instagram OR ig) -site:youtube.com",
            f'intitle:"{name}" (инстаграм | instagram)', f'inurl:profile | inurl:user | inurl:id "{name}" (instagram)',
        ]
    elif platform == "facebook":
        dorks = [
            f"{name} фейсбук OR facebook", f"+{name} +фейсбук -linkedin", f"site:facebook.com {name}",
            f'intitle:"{name} фейсбук"', f'intitle:"{name} facebook"', f'inurl:facebook {name}',
            f'"{name} фейсбук" | "{name} facebook"', f"{name} (facebook OR фейсбук) -linkedin",
            f"inurl:profile.php {name} facebook", f"allintitle:{name} facebook", f'intitle:"facebook" intitle:"{name}"',
            f"site:facebook.com intitle:\"{name}\"", f"{name} site:facebook.com inurl:profile.php",
            f'"{name}" +"facebook.com" | +"fb.com"', f"{name} (facebook OR fb) -site:reddit.com",
            f'intitle:"{name}" (фейсбук | facebook)', f'inurl:profile | inurl:user | inurl:id "{name}" (facebook)',
        ]
    elif platform == "general":
        dorks = [
            f"{name} соц сети OR social networks", f'"{name} соцсети" | "{name} social networks"',
            f'"{name}" (вк | vk | инстаграм | instagram | фейсбук | facebook)',
            f'intitle:"{name}" (вк | vk | инстаграм | instagram | фейсбук | facebook)',
        ]
    if city:
        for d in [f"{name} {city} вк | vk", f"{name} {city} инстаграм | instagram", f"{name} {city} фейсбук | facebook", f"{name} {city} соц сети | social networks", f"site:vk.com {name} {city}", f"site:instagram.com {name} {city}", f"site:facebook.com {name} {city}", f'intitle:"{name}" intitle:"{city}" (вк | vk)', f'intitle:"{name}" intitle:"{city}" (инстаграм | instagram)', f'intitle:"{name}" intitle:"{city}" (фейсбук | facebook)', f'"{name} {city}" +вк -twitter', f'"{name} {city}" +instagram -facebook', f'"{name} {city}" +фейсбук -linkedin', f"inurl:vk {name} {city}", f"inurl:instagram {name} {city}", f"inurl:facebook {name} {city}", f"allintitle:{name} {city} вк", f"allintitle:{name} {city} instagram", f"allintitle:{name} {city} facebook", f"{name} {city} site:vk.com inurl:id", f"{name} {city} site:instagram.com inurl:u", f"{name} {city} site:facebook.com inurl:profile.php", f'"{name} {city}" (вконтакте | vk.com)', f'"{name} {city}" (instagram.com | instagr)', f'"{name} {city}" (facebook.com | fb.com)']:
            dorks.append(d)
    if birthdate:
        for d in [f"{name} {birthdate} вк | vk", f"{name} {birthdate} инстаграм | instagram", f"{name} {birthdate} фейсбук | facebook", f"{name} {birthdate} соц сети | social networks", f"site:vk.com {name} {birthdate}", f"site:instagram.com {name} {birthdate}", f"site:facebook.com {name} {birthdate}", f'intitle:"{name}" intitle:"{birthdate}" (вк | vk)', f'intitle:"{name}" intitle:"{birthdate}" (инстаграм | instagram)', f'intitle:"{name}" intitle:"{birthdate}" (фейсбук | facebook)', f'"{name} {birthdate}" +вк -twitter', f'"{name} {birthdate}" +instagram -facebook', f'"{name} {birthdate}" +фейсбук -linkedin', f"inurl:vk {name} {birthdate}", f"inurl:instagram {name} {birthdate}", f"inurl:facebook {name} {birthdate}", f"allintitle:{name} \"{birthdate}\" вк", f"allintitle:{name} \"{birthdate}\" instagram", f"allintitle:{name} \"{birthdate}\" facebook", f"{name} {birthdate} site:vk.com inurl:id", f"{name} {birthdate} site:instagram.com inurl:u", f"{name} {birthdate} site:facebook.com inurl:profile.php", f'"{name}" "{birthdate}" (вконтакте | vk.com)', f'"{name}" "{birthdate}" (instagram.com | instagr)', f'"{name}" "{birthdate}" (facebook.com | fb.com)', f'"{name} {birthdate}"', f'intitle:"{name}" intitle:"{birthdate}"', f'intext:"{name}" intext:"{birthdate}"', f'"{name}" "{birthdate}" -facebook -instagram -vk', f"site:vk.com \"{name} {birthdate}\"", f"site:instagram.com \"{name} {birthdate}\"", f"site:facebook.com \"{name} {birthdate}\"", f'intitle:"{name}" "{birthdate}"', f'"{name}" inurl:birthday "{birthdate}"', f'inurl:profile "{name}" "{birthdate}"', f'inurl:user "{name}" "{birthdate}"', f'allintext:"{name}" "{birthdate}"', f'"{name} родился {birthdate}" | "{name} родилась {birthdate}"', f'"{name}" "день рождения" "{birthdate}"', f'"{name}" "birthday" "{birthdate}"', f'"{name}" "date of birth" "{birthdate}"', f'"{name}" "{birthdate}" -twitter -linkedin', f'intitle:"{name}" inurl:"birthday" "{birthdate}"', f'"{name}" "{birthdate}" site:ok.ru', f'filetype:pdf "{name}" "{birthdate}"', f'"{name}" "{birthdate}" inurl:about', f'"{name}" "{birthdate}" inurl:id', f'intitle:"profile" "{name}" "{birthdate}"', f'"{name}" "{birthdate}" -forum -blog', f'"{name}" "родился" "{birthdate}" | "{name}" "род." "{birthdate}"']:
            dorks.append(d)
    return dorks

def generate_contact_dorks(name, city, birthdate):
    dorks = []
    base = [f'"{name}" "тел"', f'"{name}" "моб"', f'"{name}" "+7"', f'"{name}" "phone"', f'"{name}" "mobile"', f'"{name}" "email"', f'"{name}" "почта"', f'"{name}" "@"', f'"{name}" "e-mail"', f'"{name}" "gmail.com"', f'"{name}" "mail.ru"', f'"{name}" "yandex.ru"', f'"{name}" "контактный телефон"', f'"{name}" "контактный email"', f'"{name}" "связаться"', f'"{name}" "моя почта"', f'"{name}" "мой телефон"', f'"{name}" "tel:"', f'"{name}" "моб."', f'"{name}" "сотовый"', f'"{name}" "phone number"', f'"{name}" "email address"', f'"{name}" "reach me"', f'"{name}" "call me"', f'"{name}" "контакты"']
    dorks.extend(base)
    if birthdate:
        for d in [f'"{name}" "{birthdate}" "тел"', f'"{name}" "{birthdate}" "моб"', f'"{name}" "{birthdate}" "+7"', f'"{name}" "{birthdate}" "phone"', f'"{name}" "{birthdate}" "mobile"', f'"{name}" "{birthdate}" "email"', f'"{name}" "{birthdate}" "почта"', f'"{name}" "{birthdate}" "@"', f'"{name}" "{birthdate}" "e-mail"', f'"{name}" "{birthdate}" "gmail.com"', f'"{name}" "{birthdate}" "mail.ru"', f'"{name}" "{birthdate}" "yandex.ru"', f'"{name}" "{birthdate}" "контактный телефон"', f'"{name}" "{birthdate}" "контактный email"', f'"{name}" "{birthdate}" "связаться"', f'"{name}" "{birthdate}" "моя почта"', f'"{name}" "{birthdate}" "мой телефон"', f'"{name}" "{birthdate}" "tel:"', f'"{name}" "{birthdate}" "моб."', f'"{name}" "{birthdate}" "сотовый"', f'"{name}" "{birthdate}" "phone number"', f'"{name}" "{birthdate}" "email address"', f'"{name}" "{birthdate}" "reach me"', f'"{name}" "{birthdate}" "call me"', f'"{name}" "{birthdate}" "контакты"']:
            dorks.append(d)
    if city:
        for d in [f'"{name}" "{city}" "тел"', f'"{name}" "{city}" "моб"', f'"{name}" "{city}" "+7"', f'"{name}" "{city}" "phone"', f'"{name}" "{city}" "mobile"', f'"{name}" "{city}" "email"', f'"{name}" "{city}" "почта"', f'"{name}" "{city}" "@"', f'"{name}" "{city}" "e-mail"', f'"{name}" "{city}" "gmail.com"', f'"{name}" "{city}" "mail.ru"', f'"{name}" "{city}" "yandex.ru"', f'"{name}" "{city}" "контактный телефон"', f'"{name}" "{city}" "контактный email"', f'"{name}" "{city}" "связаться"', f'"{name}" "{city}" "моя почта"', f'"{name}" "{city}" "мой телефон"', f'"{name}" "{city}" "tel:"', f'"{name}" "{city}" "моб."', f'"{name}" "{city}" "сотовый"', f'"{name}" "{city}" "phone number"', f'"{name}" "{city}" "email address"', f'"{name}" "{city}" "reach me"', f'"{name}" "{city}" "call me"', f'"{name}" "{city}" "контакты"']:
            dorks.append(d)
    if city and birthdate:
        for d in [f'"{name}" "{birthdate}" "{city}" "тел"', f'"{name}" "{birthdate}" "{city}" "моб"', f'"{name}" "{birthdate}" "{city}" "+7"', f'"{name}" "{birthdate}" "{city}" "phone"', f'"{name}" "{birthdate}" "{city}" "mobile"', f'"{name}" "{birthdate}" "{city}" "email"', f'"{name}" "{birthdate}" "{city}" "почта"', f'"{name}" "{birthdate}" "{city}" "@"', f'"{name}" "{birthdate}" "{city}" "e-mail"', f'"{name}" "{birthdate}" "{city}" "gmail.com"', f'"{name}" "{birthdate}" "{city}" "mail.ru"', f'"{name}" "{birthdate}" "{city}" "yandex.ru"', f'"{name}" "{birthdate}" "{city}" "контактный телефон"', f'"{name}" "{birthdate}" "{city}" "контактный email"', f'"{name}" "{birthdate}" "{city}" "связаться"', f'"{name}" "{birthdate}" "{city}" "моя почта"', f'"{name}" "{birthdate}" "{city}" "мой телефон"', f'"{name}" "{birthdate}" "{city}" "tel:"', f'"{name}" "{birthdate}" "{city}" "моб."', f'"{name}" "{birthdate}" "{city}" "сотовый"', f'"{name}" "{birthdate}" "{city}" "phone number"', f'"{name}" "{birthdate}" "{city}" "email address"', f'"{name}" "{birthdate}" "{city}" "reach me"', f'"{name}" "{birthdate}" "{city}" "call me"', f'"{name}" "{birthdate}" "{city}" "контакты"']:
            dorks.append(d)
    return dorks

def generate_location_dorks(name, city, birthdate):
    dorks = []
    base = [f'"{name}" "адрес"', f'"{name}" "проживает"', f'"{name}" "живет"', f'"{name}" "улица"', f'"{name}" "дом"', f'"{name}" "квартира"', f'"{name}" "район"', f'"{name}" "место жительства"', f'"{name}" "address"', f'"{name}" "lives in"', f'"{name}" "residence"', f'"{name}" "home address"', f'"{name}" "проживание"', f'"{name}" "прописан"', f'"{name}" "регистрация"', f'"{name}" "жилплощадь"', f'"{name}" "город"', f'"{name}" "населенный пункт"', f'"{name}" "адрес проживания"', f'"{name}" "где живет"', f'"{name}" "местонахождение"', f'"{name}" "location"', f'"{name}" "living at"', f'"{name}" "currently lives"', f'"{name}" "address:"']
    dorks.extend(base)
    if birthdate:
        for d in [f'"{name}" "{birthdate}" "адрес"', f'"{name}" "{birthdate}" "проживает"', f'"{name}" "{birthdate}" "живет"', f'"{name}" "{birthdate}" "улица"', f'"{name}" "{birthdate}" "дом"', f'"{name}" "{birthdate}" "квартира"', f'"{name}" "{birthdate}" "район"', f'"{name}" "{birthdate}" "место жительства"', f'"{name}" "{birthdate}" "address"', f'"{name}" "{birthdate}" "lives in"', f'"{name}" "{birthdate}" "residence"', f'"{name}" "{birthdate}" "home address"', f'"{name}" "{birthdate}" "проживание"', f'"{name}" "{birthdate}" "прописан"', f'"{name}" "{birthdate}" "регистрация"', f'"{name}" "{birthdate}" "жилплощадь"', f'"{name}" "{birthdate}" "город"', f'"{name}" "{birthdate}" "населенный пункт"', f'"{name}" "{birthdate}" "адрес проживания"', f'"{name}" "{birthdate}" "где живет"', f'"{name}" "{birthdate}" "местонахождение"', f'"{name}" "{birthdate}" "location"', f'"{name}" "{birthdate}" "living at"', f'"{name}" "{birthdate}" "currently lives"', f'"{name}" "{birthdate}" "address:"']:
            dorks.append(d)
    if city:
        for d in [f'"{name}" "{city}" "адрес"', f'"{name}" "{city}" "улица"', f'"{name}" "{city}" "дом"', f'"{name}" "{city}" "квартира"', f'"{name}" "{city}" "район"', f'"{name}" "{city}" "проживает"', f'"{name}" "{city}" "живет"', f'"{name}" "{city}" "место жительства"', f'"{name}" "{city}" "прописан"', f'"{name}" "{city}" "регистрация"', f'"{name}" "{city}" "address"', f'"{name}" "{city}" "lives in"', f'"{name}" "{city}" "residence"', f'"{name}" "{city}" "home address"', f'"{name}" "{city}" "проживание"', f'"{name}" "{city}" "жилплощадь"', f'"{name}" "{city}" "населенный пункт"', f'"{name}" "{city}" "адрес проживания"', f'"{name}" "{city}" "где живет"', f'"{name}" "{city}" "местонахождение"', f'"{name}" "{city}" "location"', f'"{name}" "{city}" "living at"', f'"{name}" "{city}" "currently lives"', f'"{name}" "{city}" "address:"', f'"{name}" "{city}" "ул."']:
            dorks.append(d)
    if city and birthdate:
        for d in [f'"{name}" "{birthdate}" "{city}" "адрес"', f'"{name}" "{birthdate}" "{city}" "улица"', f'"{name}" "{birthdate}" "{city}" "дом"', f'"{name}" "{birthdate}" "{city}" "квартира"', f'"{name}" "{birthdate}" "{city}" "район"', f'"{name}" "{birthdate}" "{city}" "проживает"', f'"{name}" "{birthdate}" "{city}" "живет"', f'"{name}" "{birthdate}" "{city}" "место жительства"', f'"{name}" "{birthdate}" "{city}" "прописан"', f'"{name}" "{birthdate}" "{city}" "регистрация"', f'"{name}" "{birthdate}" "{city}" "address"', f'"{name}" "{birthdate}" "{city}" "lives in"', f'"{name}" "{birthdate}" "{city}" "residence"', f'"{name}" "{birthdate}" "{city}" "home address"', f'"{name}" "{birthdate}" "{city}" "проживание"', f'"{name}" "{birthdate}" "{city}" "жилплощадь"', f'"{name}" "{birthdate}" "{city}" "населенный пункт"', f'"{name}" "{birthdate}" "{city}" "адрес проживания"', f'"{name}" "{birthdate}" "{city}" "где живет"', f'"{name}" "{birthdate}" "{city}" "местонахождение"', f'"{name}" "{birthdate}" "{city}" "location"', f'"{name}" "{birthdate}" "{city}" "living at"', f'"{name}" "{birthdate}" "{city}" "currently lives"', f'"{name}" "{birthdate}" "{city}" "address:"', f'"{name}" "{birthdate}" "{city}" "ул."']:
            dorks.append(d)
    return dorks

def generate_employment_dorks(name, city, birthdate):
    dorks = []
    base = [f'"{name}" "работа"', f'"{name}" "место работы"', f'"{name}" "должность"', f'"{name}" "компания"', f'"{name}" "трудоустройство"', f'"{name}" "работает в"', f'"{name}" "кем работает"', f'"{name}" "профессия"', f'"{name}" "сфера деятельности"', f'"{name}" "job"', f'"{name}" "position"', f'"{name}" "company"', f'"{name}" "works at"', f'"{name}" "occupation"', f'"{name}" "employment"', f'"{name}" "должность:"', f'"{name}" "место работы:"', f'"{name}" "работает"', f'"{name}" "трудится"', f'"{name}" "штат"', f'"{name}" "сотрудник"', f'"{name}" "специалист"', f'"{name}" "менеджер"', f'"{name}" "директор"', f'"{name}" "рабочее место"']
    dorks.extend(base)
    if birthdate:
        for d in [f'"{name}" "{birthdate}" "работа"', f'"{name}" "{birthdate}" "место работы"', f'"{name}" "{birthdate}" "должность"', f'"{name}" "{birthdate}" "компания"', f'"{name}" "{birthdate}" "трудоустройство"', f'"{name}" "{birthdate}" "работает в"', f'"{name}" "{birthdate}" "кем работает"', f'"{name}" "{birthdate}" "профессия"', f'"{name}" "{birthdate}" "сфера деятельности"', f'"{name}" "{birthdate}" "job"', f'"{name}" "{birthdate}" "position"', f'"{name}" "{birthdate}" "company"', f'"{name}" "{birthdate}" "works at"', f'"{name}" "{birthdate}" "occupation"', f'"{name}" "{birthdate}" "employment"', f'"{name}" "{birthdate}" "должность:"', f'"{name}" "{birthdate}" "место работы:"', f'"{name}" "{birthdate}" "работает"', f'"{name}" "{birthdate}" "трудится"', f'"{name}" "{birthdate}" "штат"', f'"{name}" "{birthdate}" "сотрудник"', f'"{name}" "{birthdate}" "специалист"', f'"{name}" "{birthdate}" "менеджер"', f'"{name}" "{birthdate}" "директор"', f'"{name}" "{birthdate}" "рабочее место"']:
            dorks.append(d)
    if city:
        for d in [f'"{name}" "{city}" "работа"', f'"{name}" "{city}" "место работы"', f'"{name}" "{city}" "должность"', f'"{name}" "{city}" "компания"', f'"{name}" "{city}" "трудоустройство"', f'"{name}" "{city}" "работает в"', f'"{name}" "{city}" "кем работает"', f'"{name}" "{city}" "профессия"', f'"{name}" "{city}" "сфера деятельности"', f'"{name}" "{city}" "job"', f'"{name}" "{city}" "position"', f'"{name}" "{city}" "company"', f'"{name}" "{city}" "works at"', f'"{name}" "{city}" "occupation"', f'"{name}" "{city}" "employment"', f'"{name}" "{city}" "должность:"', f'"{name}" "{city}" "место работы:"', f'"{name}" "{city}" "работает"', f'"{name}" "{city}" "трудится"', f'"{name}" "{city}" "штат"', f'"{name}" "{city}" "сотрудник"', f'"{name}" "{city}" "специалист"', f'"{name}" "{city}" "менеджер"', f'"{name}" "{city}" "директор"', f'"{name}" "{city}" "рабочее место"']:
            dorks.append(d)
    if city and birthdate:
        for d in [f'"{name}" "{birthdate}" "{city}" "работа"', f'"{name}" "{birthdate}" "{city}" "место работы"', f'"{name}" "{birthdate}" "{city}" "должность"', f'"{name}" "{birthdate}" "{city}" "компания"', f'"{name}" "{birthdate}" "{city}" "трудоустройство"', f'"{name}" "{birthdate}" "{city}" "работает в"', f'"{name}" "{birthdate}" "{city}" "кем работает"', f'"{name}" "{birthdate}" "{city}" "профессия"', f'"{name}" "{birthdate}" "{city}" "сфера деятельности"', f'"{name}" "{birthdate}" "{city}" "job"', f'"{name}" "{birthdate}" "{city}" "position"', f'"{name}" "{birthdate}" "{city}" "company"', f'"{name}" "{birthdate}" "{city}" "works at"', f'"{name}" "{birthdate}" "{city}" "occupation"', f'"{name}" "{birthdate}" "{city}" "employment"', f'"{name}" "{birthdate}" "{city}" "должность:"', f'"{name}" "{birthdate}" "{city}" "место работы:"', f'"{name}" "{birthdate}" "{city}" "работает"', f'"{name}" "{birthdate}" "{city}" "трудится"', f'"{name}" "{birthdate}" "{city}" "штат"', f'"{name}" "{birthdate}" "{city}" "сотрудник"', f'"{name}" "{birthdate}" "{city}" "специалист"', f'"{name}" "{birthdate}" "{city}" "менеджер"', f'"{name}" "{birthdate}" "{city}" "директор"', f'"{name}" "{birthdate}" "{city}" "рабочее место"']:
            dorks.append(d)
    return dorks

def info_searcher():
    while True:
        clear_screen()
        print_logo()
        print("\n" + center_text("Info Searcher"))
        print("\n1. Social Networks")
        print("2. Contact Info")
        print("3. Location")
        print("4. Employment")
        print("5. Back")
        choice = input("\nSelect (1-5): ").strip()
        if choice == "1":
            clear_screen()
            print_logo()
            print("\n" + center_text("Social Networks"))
            print("\n1.1 VK\n1.2 Instagram\n1.3 Facebook\n1.4 General")
            sub = input("\nSelect (1-4): ").strip()
            if sub == "1":
                name = input("\nEnter target name: ").strip()
                if name:
                    print("\nOptional info (press Enter to skip):")
                    city = input("City: ").strip()
                    birthdate = input("Date of birth (YYYY-MM-DD): ").strip()
                    dorks = generate_social_dorks("vk", name, city, birthdate)
                    print(f"\nGenerated {len(dorks)} dorks:\n")
                    for d in dorks:
                        print(d)
                    input("\nPress Enter...")
            elif sub == "2":
                name = input("\nEnter target name: ").strip()
                if name:
                    print("\nOptional info (press Enter to skip):")
                    city = input("City: ").strip()
                    birthdate = input("Date of birth (YYYY-MM-DD): ").strip()
                    dorks = generate_social_dorks("instagram", name, city, birthdate)
                    print(f"\nGenerated {len(dorks)} dorks:\n")
                    for d in dorks:
                        print(d)
                    input("\nPress Enter...")
            elif sub == "3":
                name = input("\nEnter target name: ").strip()
                if name:
                    print("\nOptional info (press Enter to skip):")
                    city = input("City: ").strip()
                    birthdate = input("Date of birth (YYYY-MM-DD): ").strip()
                    dorks = generate_social_dorks("facebook", name, city, birthdate)
                    print(f"\nGenerated {len(dorks)} dorks:\n")
                    for d in dorks:
                        print(d)
                    input("\nPress Enter...")
            elif sub == "4":
                name = input("\nEnter target name: ").strip()
                if name:
                    print("\nOptional info (press Enter to skip):")
                    city = input("City: ").strip()
                    birthdate = input("Date of birth (YYYY-MM-DD): ").strip()
                    dorks = generate_social_dorks("general", name, city, birthdate)
                    print(f"\nGenerated {len(dorks)} dorks:\n")
                    for d in dorks:
                        print(d)
                    input("\nPress Enter...")
            else:
                input("Invalid. Press Enter...")
        elif choice == "2":
            clear_screen()
            print_logo()
            print("\n" + center_text("Contact Info"))
            print("\n2.1 Phone number\n2.2 Email\n2.3 All")
            sub = input("\nSelect (1-3): ").strip()
            if sub in ["1","2","3"]:
                name = input("\nEnter target name: ").strip()
                if name:
                    print("\nOptional info (press Enter to skip):")
                    city = input("City: ").strip()
                    birthdate = input("Date of birth (YYYY-MM-DD): ").strip()
                    dorks = generate_contact_dorks(name, city, birthdate)
                    print(f"\nGenerated {len(dorks)} dorks:\n")
                    for d in dorks:
                        print(d)
                    input("\nPress Enter...")
            else:
                input("Invalid. Press Enter...")
        elif choice == "3":
            clear_screen()
            print_logo()
            print("\n" + center_text("Location"))
            print("\n3.1 Address\n3.2 All possible location info")
            sub = input("\nSelect (1-2): ").strip()
            if sub in ["1","2"]:
                name = input("\nEnter target name: ").strip()
                if name:
                    print("\nOptional info (press Enter to skip):")
                    city = input("City: ").strip()
                    birthdate = input("Date of birth (YYYY-MM-DD): ").strip()
                    dorks = generate_location_dorks(name, city, birthdate)
                    print(f"\nGenerated {len(dorks)} dorks:\n")
                    for d in dorks:
                        print(d)
                    input("\nPress Enter...")
            else:
                input("Invalid. Press Enter...")
        elif choice == "4":
            clear_screen()
            print_logo()
            print("\n" + center_text("Employment"))
            print("\n4.1 Position\n4.2 Job\n4.3 Workplace\n4.4 All possible")
            sub = input("\nSelect (1-4): ").strip()
            if sub in ["1","2","3","4"]:
                name = input("\nEnter target name: ").strip()
                if name:
                    print("\nOptional info (press Enter to skip):")
                    city = input("City: ").strip()
                    birthdate = input("Date of birth (YYYY-MM-DD): ").strip()
                    dorks = generate_employment_dorks(name, city, birthdate)
                    print(f"\nGenerated {len(dorks)} dorks:\n")
                    for d in dorks:
                        print(d)
                    input("\nPress Enter...")
            else:
                input("Invalid. Press Enter...")
        elif choice == "5":
            break
        else:
            input("Invalid. Press Enter...")

def main():
    while True:
        clear_screen()
        print_logo()
        print("\n" + center_text("OsintDorks"))
        print("\n1. Info Searcher")
        print("0. Exit")
        print("99. Check updates")
        choice = input("\nSelect (1/0/99): ").strip()
        if choice == "1":
            info_searcher()
        elif choice == "0":
            print("\nExiting...")
            break
        elif choice == "99":
            check_updates()
        else:
            input("Invalid. Press Enter...")

if __name__ == "__main__":
    main()
