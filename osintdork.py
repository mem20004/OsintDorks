#!/usr/bin/env python3
import os
import shutil
import subprocess
import sys

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
                                                                   Author: Mem2004
"""
    print(center_text(logo))

def check_updates():
    clear_screen()
    print_logo()
    print("\n" + center_text("CHECKING FOR UPDATES"))
    try:
        result = subprocess.run(["git", "pull"], capture_output=True, text=True, cwd=os.path.dirname(os.path.abspath(__file__)))
        if result.stdout:
            print(result.stdout)
        if result.stderr:
            print(result.stderr)
        if "Already up to date" in result.stdout:
            print("\nYou are already on the latest version.")
        elif "Updating" in result.stdout:
            print("\nUpdate successful! Restart the program to apply changes.")
        else:
            print("\nUpdate check completed.")
    except FileNotFoundError:
        print("\nGit not found. Make sure git is installed and run from the cloned repository.")
    except Exception as e:
        print(f"\nError: {e}")
    input("\nPress Enter to continue...")

def generate_social_dorks(platform, name, city="", birthdate=""):
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
            f"{name} инстаграм OR instagram", f"+{name} +instagram -facebook",
            f"site:instagram.com {name}", f'intitle:"{name} инстаграм"', f'intitle:"{name} instagram"',
            f'inurl:instagram {name}', f'"{name} инстаграм" | "{name} instagram"',
            f"{name} (instagram OR инстаграм) -twitter", f"inurl:p {name} instagram",
            f"allintitle:{name} instagram", f'intitle:"instagram" intitle:"{name}"',
            f"site:instagram.com intitle:\"{name}\"", f"{name} site:instagram.com inurl:u",
            f'"{name}" +"instagram.com" | +"instagr"', f"{name} (instagram OR ig) -site:youtube.com",
            f'intitle:"{name}" (инстаграм | instagram)', f'inurl:profile | inurl:user | inurl:id "{name}" (instagram)',
        ]
    elif platform == "facebook":
        dorks = [
            f"{name} фейсбук OR facebook", f"+{name} +фейсбук -linkedin", f"site:facebook.com {name}",
            f'intitle:"{name} фейсбук"', f'intitle:"{name} facebook"', f'inurl:facebook {name}',
            f'"{name} фейсбук" | "{name} facebook"', f"{name} (facebook OR фейсбук) -linkedin",
            f"inurl:profile.php {name} facebook", f"allintitle:{name} facebook",
            f'intitle:"facebook" intitle:"{name}"', f"site:facebook.com intitle:\"{name}\"",
            f"{name} site:facebook.com inurl:profile.php", f'"{name}" +"facebook.com" | +"fb.com"',
            f"{name} (facebook OR fb) -site:reddit.com", f'intitle:"{name}" (фейсбук | facebook)',
            f'inurl:profile | inurl:user | inurl:id "{name}" (facebook)',
        ]
    elif platform == "general":
        dorks = [
            f"{name} соц сети OR social networks", f'"{name} соцсети" | "{name} social networks"',
            f'"{name}" (вк | vk | инстаграм | instagram | фейсбук | facebook)',
            f'intitle:"{name}" (вк | vk | инстаграм | instagram | фейсбук | facebook)',
        ]
    if city:
        city_dorks = [
            f"{name} {city} вк | vk", f"{name} {city} инстаграм | instagram", f"{name} {city} фейсбук | facebook",
            f"{name} {city} соц сети | social networks", f"site:vk.com {name} {city}", f"site:instagram.com {name} {city}",
            f"site:facebook.com {name} {city}", f'intitle:"{name}" intitle:"{city}" (вк | vk)',
            f'intitle:"{name}" intitle:"{city}" (инстаграм | instagram)', f'intitle:"{name}" intitle:"{city}" (фейсбук | facebook)',
            f'"{name} {city}" +вк -twitter', f'"{name} {city}" +instagram -facebook', f'"{name} {city}" +фейсбук -linkedin',
            f"inurl:vk {name} {city}", f"inurl:instagram {name} {city}", f"inurl:facebook {name} {city}",
            f"allintitle:{name} {city} вк", f"allintitle:{name} {city} instagram", f"allintitle:{name} {city} facebook",
            f"{name} {city} site:vk.com inurl:id", f"{name} {city} site:instagram.com inurl:u",
            f"{name} {city} site:facebook.com inurl:profile.php", f'"{name} {city}" (вконтакте | vk.com)',
            f'"{name} {city}" (instagram.com | instagr)', f'"{name} {city}" (facebook.com | fb.com)',
        ]
        dorks.extend(city_dorks)
    if birthdate:
        bd_dorks = [
            f"{name} {birthdate} вк | vk", f"{name} {birthdate} инстаграм | instagram", f"{name} {birthdate} фейсбук | facebook",
            f"{name} {birthdate} соц сети | social networks", f"site:vk.com {name} {birthdate}",
            f"site:instagram.com {name} {birthdate}", f"site:facebook.com {name} {birthdate}",
            f'intitle:"{name}" intitle:"{birthdate}" (вк | vk)', f'intitle:"{name}" intitle:"{birthdate}" (инстаграм | instagram)',
            f'intitle:"{name}" intitle:"{birthdate}" (фейсбук | facebook)', f'"{name} {birthdate}" +вк -twitter',
            f'"{name} {birthdate}" +instagram -facebook', f'"{name} {birthdate}" +фейсбук -linkedin',
            f"inurl:vk {name} {birthdate}", f"inurl:instagram {name} {birthdate}", f"inurl:facebook {name} {birthdate}",
            f"allintitle:{name} \"{birthdate}\" вк", f"allintitle:{name} \"{birthdate}\" instagram",
            f"allintitle:{name} \"{birthdate}\" facebook", f"{name} {birthdate} site:vk.com inurl:id",
            f"{name} {birthdate} site:instagram.com inurl:u", f"{name} {birthdate} site:facebook.com inurl:profile.php",
            f'"{name}" "{birthdate}" (вконтакте | vk.com)', f'"{name}" "{birthdate}" (instagram.com | instagr)',
            f'"{name}" "{birthdate}" (facebook.com | fb.com)', f'"{name} {birthdate}"', f'intitle:"{name}" intitle:"{birthdate}"',
            f'intext:"{name}" intext:"{birthdate}"', f'"{name}" "{birthdate}" -facebook -instagram -vk',
            f"site:vk.com \"{name} {birthdate}\"", f"site:instagram.com \"{name} {birthdate}\"",
            f"site:facebook.com \"{name} {birthdate}\"", f'intitle:"{name}" "{birthdate}"', f'"{name}" inurl:birthday "{birthdate}"',
            f'inurl:profile "{name}" "{birthdate}"', f'inurl:user "{name}" "{birthdate}"', f'allintext:"{name}" "{birthdate}"',
            f'"{name} родился {birthdate}" | "{name} родилась {birthdate}"', f'"{name}" "день рождения" "{birthdate}"',
            f'"{name}" "birthday" "{birthdate}"', f'"{name}" "date of birth" "{birthdate}"', f'"{name}" "{birthdate}" -twitter -linkedin',
            f'intitle:"{name}" inurl:"birthday" "{birthdate}"', f'"{name}" "{birthdate}" site:ok.ru',
            f'filetype:pdf "{name}" "{birthdate}"', f'"{name}" "{birthdate}" inurl:about', f'"{name}" "{birthdate}" inurl:id',
            f'intitle:"profile" "{name}" "{birthdate}"', f'"{name}" "{birthdate}" -forum -blog',
            f'"{name}" "родился" "{birthdate}" | "{name}" "род." "{birthdate}"',
        ]
        dorks.extend(bd_dorks)
    return dorks

def generate_contact_dorks(name, city="", birthdate=""):
    dorks = [f'"{name}" "{kw}"' for kw in ["тел","моб","+7","phone","mobile","email","почта","@","e-mail","gmail.com","mail.ru","yandex.ru","контактный телефон","контактный email","связаться","моя почта","мой телефон","tel:","моб.","сотовый","phone number","email address","reach me","call me","контакты"]]
    if birthdate:
        dorks.extend([f'"{name}" "{birthdate}" "{kw}"' for kw in ["тел","моб","+7","phone","mobile","email","почта","@","e-mail","gmail.com","mail.ru","yandex.ru","контактный телефон","контактный email","связаться","моя почта","мой телефон","tel:","моб.","сотовый","phone number","email address","reach me","call me","контакты"]])
    if city:
        dorks.extend([f'"{name}" "{city}" "{kw}"' for kw in ["тел","моб","+7","phone","mobile","email","почта","@","e-mail","gmail.com","mail.ru","yandex.ru","контактный телефон","контактный email","связаться","моя почта","мой телефон","tel:","моб.","сотовый","phone number","email address","reach me","call me","контакты"]])
    if city and birthdate:
        dorks.extend([f'"{name}" "{birthdate}" "{city}" "{kw}"' for kw in ["тел","моб","+7","phone","mobile","email","почта","@","e-mail","gmail.com","mail.ru","yandex.ru","контактный телефон","контактный email","связаться","моя почта","мой телефон","tel:","моб.","сотовый","phone number","email address","reach me","call me","контакты"]])
    return dorks

def generate_location_dorks(name, city="", birthdate=""):
    dorks = [f'"{name}" "{kw}"' for kw in ["адрес","проживает","живет","улица","дом","квартира","район","место жительства","address","lives in","residence","home address","проживание","прописан","регистрация","жилплощадь","город","населенный пункт","адрес проживания","где живет","местонахождение","location","living at","currently lives","address:"]]
    if birthdate:
        dorks.extend([f'"{name}" "{birthdate}" "{kw}"' for kw in ["адрес","проживает","живет","улица","дом","квартира","район","место жительства","address","lives in","residence","home address","проживание","прописан","регистрация","жилплощадь","город","населенный пункт","адрес проживания","где живет","местонахождение","location","living at","currently lives","address:"]])
    if city:
        dorks.extend([f'"{name}" "{city}" "{kw}"' for kw in ["адрес","улица","дом","квартира","район","проживает","живет","место жительства","прописан","регистрация","address","lives in","residence","home address","проживание","жилплощадь","населенный пункт","адрес проживания","где живет","местонахождение","location","living at","currently lives","address:","ул."]])
    if city and birthdate:
        dorks.extend([f'"{name}" "{birthdate}" "{city}" "{kw}"' for kw in ["адрес","улица","дом","квартира","район","проживает","живет","место жительства","прописан","регистрация","address","lives in","residence","home address","проживание","жилплощадь","населенный пункт","адрес проживания","где живет","местонахождение","location","living at","currently lives","address:","ул."]])
    return dorks

def generate_employment_dorks(name, city="", birthdate=""):
    dorks = [f'"{name}" "{kw}"' for kw in ["работа","место работы","должность","компания","трудоустройство","работает в","кем работает","профессия","сфера деятельности","job","position","company","works at","occupation","employment","должность:","место работы:","работает","трудится","штат","сотрудник","специалист","менеджер","директор","рабочее место"]]
    if birthdate:
        dorks.extend([f'"{name}" "{birthdate}" "{kw}"' for kw in ["работа","место работы","должность","компания","трудоустройство","работает в","кем работает","профессия","сфера деятельности","job","position","company","works at","occupation","employment","должность:","место работы:","работает","трудится","штат","сотрудник","специалист","менеджер","директор","рабочее место"]])
    if city:
        dorks.extend([f'"{name}" "{city}" "{kw}"' for kw in ["работа","место работы","должность","компания","трудоустройство","работает в","кем работает","профессия","сфера деятельности","job","position","company","works at","occupation","employment","должность:","место работы:","работает","трудится","штат","сотрудник","специалист","менеджер","директор","рабочее место"]])
    if city and birthdate:
        dorks.extend([f'"{name}" "{birthdate}" "{city}" "{kw}"' for kw in ["работа","место работы","должность","компания","трудоустройство","работает в","кем работает","профессия","сфера деятельности","job","position","company","works at","occupation","employment","должность:","место работы:","работает","трудится","штат","сотрудник","специалист","менеджер","директор","рабочее место"]])
    return dorks

def get_name_and_extra(section, sub_section=""):
    name = input("\nEnter target name: ").strip()
    if not name:
        print("Name is required!")
        input("Press Enter to continue...")
        return
    print("\nOptional info (press Enter to skip each):")
    city = input("City: ").strip()
    birthdate = input("Date of birth (YYYY-MM-DD): ").strip()
    if section == "social":
        dorks = generate_social_dorks(sub_section, name, city, birthdate)
    elif section == "contact":
        dorks = generate_contact_dorks(name, city, birthdate)
    elif section == "location":
        dorks = generate_location_dorks(name, city, birthdate)
    elif section == "employment":
        dorks = generate_employment_dorks(name, city, birthdate)
    else:
        dorks = []
    print(f"\nGenerated {len(dorks)} dorks:\n")
    for dork in dorks:
        print(dork)
    input("\nPress Enter to continue...")

def info_searcher():
    while True:
        clear_screen()
        print_logo()
        print("\n" + center_text("Info Searcher"))
        print("\n1. Social Networks")
        print("2. Contact Info")
        print("3. Location")
        print("4. Employment")
        print("0. Back to main menu")
        choice = input("\nSelect option (1-4, 0): ").strip()
        if choice == "0":
            break
        elif choice == "1":
            clear_screen()
            print_logo()
            print("\n" + center_text("Social Networks"))
            print("\n1.1 VK")
            print("1.2 Instagram")
            print("1.3 Facebook")
            print("1.4 General")
            sub = input("\nSelect (1-4): ").strip()
            if sub == "1":
                get_name_and_extra("social", "vk")
            elif sub == "2":
                get_name_and_extra("social", "instagram")
            elif sub == "3":
                get_name_and_extra("social", "facebook")
            elif sub == "4":
                get_name_and_extra("social", "general")
            else:
                input("Invalid. Press Enter...")
        elif choice == "2":
            clear_screen()
            print_logo()
            print("\n" + center_text("Contact Info"))
            print("\n2.1 Phone number")
            print("2.2 Email")
            print("2.3 All")
            sub = input("\nSelect (1-3): ").strip()
            if sub in ["1","2","3"]:
                get_name_and_extra("contact")
            else:
                input("Invalid. Press Enter...")
        elif choice == "3":
            clear_screen()
            print_logo()
            print("\n" + center_text("Location"))
            print("\n3.1 Address")
            print("3.2 All possible location info")
            sub = input("\nSelect (1-2): ").strip()
            if sub in ["1","2"]:
                get_name_and_extra("location")
            else:
                input("Invalid. Press Enter...")
        elif choice == "4":
            clear_screen()
            print_logo()
            print("\n" + center_text("Employment"))
            print("\n4.1 Position")
            print("4.2 Job")
            print("4.3 Workplace")
            print("4.4 All possible")
            sub = input("\nSelect (1-4): ").strip()
            if sub in ["1","2","3","4"]:
                get_name_and_extra("employment")
            else:
                input("Invalid. Press Enter...")
        else:
            input("Invalid option. Press Enter...")

def main():
    while True:
        clear_screen()
        print_logo()
        print("\n" + center_text("OsintDorks"))
        print("\n1. Info Searcher")
        print("99. Check for updates (git pull)")
        print("0. Exit")
        main_choice = input("\nSelect: ").strip()
        if main_choice == "1":
            info_searcher()
        elif main_choice == "99":
            check_updates()
        elif main_choice == "0":
            print("\nExiting...")
            break
        else:
            input("Invalid. Press Enter...")

if __name__ == "__main__":
    main()
