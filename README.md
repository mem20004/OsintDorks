# OsintDorks
Dork generator for Linux/Mac OS

# RUSSIAN

OsintDorks - генератор поисковых запросов для OSINT-разведки

Автор: Mem2004
Лицензия: MIT


О проекте

OsintDorks это инструмент командной строки для автоматической генерации Google Dorks 
специализированных запросов которые помогают находить информацию о человеке в открытых
источниках. Проект создан для образовательных целей и законной разведки по открытым
данным.

Программа позволяет генерировать сотни уникальных поисковых запросов с учетом имени
города и даты рождения цели. Все запросы выводятся прямо в консоль и готовы к
копированию в поисковую систему.


Установка

Откройте терминал и выполните следующие команды:

git clone https://github.com/mem20004/OsintDorks

cd OsintDorks

python3 osintdork.py

Никаких дополнительных библиотек не требуется используется только стандартная
библиотека Python.


Использование

После запуска вы увидите главное меню:

OsintDorks

1. Info Searcher
2. Exit

Выберите пункт 1 чтобы перейти в режим генерации запросов.

Внутри Info Searcher доступны четыре категории:

Категория 1: Social Networks

  1.1 VK - поиск профилей во ВКонтакте
  1.2 Instagram - поиск профилей в Instagram
  1.3 Facebook - поиск профилей в Facebook
  1.4 General - общие запросы по всем соцсетям

Категория 2: Contact Info

  2.1 Phone number - поиск номеров телефонов
  2.2 Email - поиск email адресов
  2.3 All - комбинированный поиск

Категория 3: Location

  3.1 Address - поиск адресов
  3.2 All possible location info - все возможные данные о местоположении

Категория 4: Employment

  4.1 Position - поиск должности
  4.2 Job - поиск места работы
  4.3 Workplace - поиск компании
  4.4 All possible - все возможные данные о работе

После выбора категории и подкатегории программа запросит:

Enter target name - имя цели (обязательное поле)

Затем опциональные данные которые можно пропустить нажав Enter:

City - город проживания цели
Date of birth - дата рождения в формате YYYY-MM-DD

После ввода программа сгенерирует все возможные поисковые запросы и выведет их на
экран. Вы можете копировать любой запрос и вставлять его в Google.


Пример работы

Допустим вы ищете информацию о человеке по имени Иван Петров который живет в Москве
и родился 15 мая 1990 года.

Вы выбираете Social Networks затем VK. Программа спрашивает имя вводите Иван Петров.
Город вводите Москва. Дату рождения вводите 1990-05-15.

Программа генерирует десятки запросов включая такие:

"Иван Петров" вк OR vk
site:vk.com Иван Петров
"Иван Петров" Москва вк
"Иван Петров" 1990-05-15 vk
"Иван Петров" Москва 1990-05-15 site:vk.com

Вы копируете любой из этих запросов вставляете в Google и получаете результаты
поиска.


Количество генерируемых запросов

Для Social Networks при полном заполнении всех полей генерируется около 200 запросов
Для Contact Info около 100 запросов
Для Location около 100 запросов
Для Employment около 100 запросов

Общее количество возможных уникальных запросов превышает 500 штук.



Благодарности

Спасибо всем кто тестирует инструмент и предлагает улучшения. Если вам понравился
проект поставьте звезду на GitHub это поможет другим людям найти его.

Лицензия MIT

# ENGLISH

OsintDorks - search query generator for OSINT reconnaissance

Author: Mem2004
License: MIT


About the project

OsintDorks is a command line tool for automatic generation of Google Dorks
specialized queries that help find information about a person in open
sources. The project is created for educational purposes and lawful open
source intelligence.

The program allows generating hundreds of unique search queries taking into
account the target's name city and date of birth. All queries are printed
directly to the console and ready to be copied into a search engine.


Installation

Open a terminal and run the following commands:

git clone https://github.com/mem20004/OsintDorks

cd OsintDorks

python3 osintdork.py

No additional libraries are required only the standard Python library is used.


Usage

After launching you will see the main menu:

OsintDorks

1. Info Searcher
2. Exit

Select option 1 to enter the query generation mode.

Inside Info Searcher there are four categories:

Category 1: Social Networks

  1.1 VK - search for profiles on VKontakte
  1.2 Instagram - search for profiles on Instagram
  1.3 Facebook - search for profiles on Facebook
  1.4 General - general queries across all social networks

Category 2: Contact Info

  2.1 Phone number - search for phone numbers
  2.2 Email - search for email addresses
  2.3 All - combined search

Category 3: Location

  3.1 Address - search for addresses
  3.2 All possible location info - all possible location data

Category 4: Employment

  4.1 Position - search for job title
  4.2 Job - search for place of work
  4.3 Workplace - search for company
  4.4 All possible - all possible employment data

After selecting a category and subcategory the program will prompt for:

Enter target name - target name (required field)

Then optional data which can be skipped by pressing Enter:

City - target's city of residence
Date of birth - date of birth in YYYY-MM-DD format

After input the program will generate all possible search queries and display
them on the screen. You can copy any query and paste it into Google.


Example

Suppose you are looking for information about a person named Ivan Petrov who
lives in Moscow and was born on May 15 1990.

You select Social Networks then VK. The program asks for the name enter Ivan
Petrov. Enter Moscow as the city. Enter 1990-05-15 as the date of birth.

The program generates dozens of queries including these:

"Ivan Petrov" vk OR vkontakte
site:vk.com Ivan Petrov
"Ivan Petrov" Moscow vk
"Ivan Petrov" 1990-05-15 vk
"Ivan Petrov" Moscow 1990-05-15 site:vk.com

You copy any of these queries paste into Google and get search results.


Number of generated queries

For Social Networks with all fields filled about 200 queries are generated
For Contact Info about 100 queries
For Location about 100 queries
For Employment about 100 queries

The total number of possible unique queries exceeds 500.


Acknowledgments

Thanks to everyone who tests the tool and suggests improvements. If you like
the project star it on GitHub it will help other people find it.

License MIT
