import math
import os
import glob
import platform
import colorama
import requests
import random
import calendar
import datetime
from datetime import datetime
from datetime import date
from colorama import init, Fore, Back, Style
from time import strftime
from random import *

input_text = ""
currentElement = {}
isShowMenuNeeded = True
file = ""

movementHistory = [0]

def getUserInput():
    userInput = input(Fore.GREEN + f"[Користувач]: ")
    writeToFile(f"[Користувач]: {userInput}\n")
    
    return userInput

def printResponse(text):
    print(Fore.CYAN + f"[Бот]: {text}")
    writeToFile(f"[Бот]: {text}\n")

def createFile():
    global file
    today = datetime.today()
    file = open(f"dialog_{today.strftime('%d_%m_%Y_%H_%M_%S')}.txt", "a")

def writeToFile(text):
    global file
    file.write(text)

def closeFile():
    global file
    file.close()

def printMenuInfo():
    global currentElement

    #if platform.system() == "Windows":
     #   os.system('cls')
    #else:
     #   os.system('clear')

    menuInfo = f""
    menuInfo += "\n------------------------------------------------------------"
    menuInfo += f"\nАктивне вікно: {currentElement['description']}"
    
    listOfWindows = getListOfWindows('string')
    if len(listOfWindows) > 0:
        menuInfo += f"\n\nДоступні вікна: {listOfWindows}"
    
    listOfActions = getListOfActions('string')
    if len(listOfActions) > 0:
        menuInfo += f"\n\nДоступні дії: {listOfActions}"

    menuInfo += f"\n\nДодаткові дії: Назад (н) | Допомога (д, ?) | Вихід (в)"
    menuInfo += "\n------------------------------------------------------------"

    printResponse(menuInfo)

def moveBackward():
    global movementHistory
    if (len(movementHistory) != 0):
         movementHistory.pop()

def moveTo(accessBy):
    global currentElement
    global movementHistory
    newWindowIndex = -1
    
    for i, window in enumerate(currentElement["windows"]):
        if window["accessBy"].lower() == accessBy.lower() or window["description"].lower() == accessBy.lower():
            newWindowIndex = i
            break
            
    if newWindowIndex != -1:
        movementHistory.append(i)
        return True
    else:
        return False
    
def doAction(accessBy):
    global currentElement
    actionIndex = -1
    
    for i, action in enumerate(currentElement["actions"]):
        if action["accessBy"].lower() == accessBy.lower() or action["description"].lower() == accessBy.lower():
            actionIndex = i
            break
            
    if actionIndex != -1:
        currentElement["actions"][actionIndex]["function"]()
        return True
    else:
        return False


def getListOfWindows(type = "array"):
    global currentElement
    listOfWindows = []
    listOfWindowsAsString = ""
    for i, window in enumerate(currentElement["windows"]):
        listOfWindows.append(f"{window['description']} ({window['accessBy']})")
       
        if i < len(currentElement["windows"]):
            listOfWindowsAsString += f"\n"
        
        listOfWindowsAsString += f"""\t- {window['description']} ({window['accessBy']})"""
        
    if type == "string":
        return listOfWindowsAsString
    else:
        if type == "array":
            return listOfWindows

def setCurrentElement():
    global currentElement
    for i, elementIndex in enumerate(movementHistory):
        if i == 0:
            currentElement = menu[elementIndex]
        else:
            currentElement = currentElement["windows"][elementIndex]

def getListOfActions(type = "array"):
    global currentElement
    listOfActions = []
    listOfActionsAsString = ""
    for i, action in enumerate(currentElement["actions"]):
        listOfActions.append(f"""{action['description']} ({action['accessBy']})""")
       
        if i < len(currentElement["actions"]):
            listOfActionsAsString += f"\n"
        
        listOfActionsAsString += f"""\t- {action['description']} ({action['accessBy']})"""
        
    if type == "string":
        return listOfActionsAsString
    else:
        if type == "array":
            return listOfActions

def exit():
    global movementHistory 
    movementHistory = []

    return

def getSomeHelp():
    global currentElement
    return currentElement["helpText"]


def printHello():
    printResponse("Привіт")
    return


def BoylMariott():
    printResponse("""Добре, формула для обчислення 'P1 * V1 = P2 * V2',
я можу допомогти визначити P1 або V1. Що би ви хотіли визначити?""")
    input = getUserInput()
    if input == "P1":
        printResponse("Добре, скажіть, будь ласка, значення V1")
        V_one = int(getUserInput())
        printResponse("Добре, тепер P2")
        P_two = int(getUserInput())
        printResponse("Як щодо V2?")
        V_two = int(getUserInput())
        P_one = float(str(P_two * V_two / V_one))
        printResponse(f"Отже, P1={str(P_one)}")

    if input == "V1":
        printResponse("Добре, скажіть, будь ласка, значення P1")
        p_one = int(getUserInput())
        printResponse("Добре, тепер P2")
        p_two = int(getUserInput())
        printResponse("Як щодо V2?")
        v_two = int(getUserInput())
        v_one = float(str(p_two * v_two / p_one))
        printResponse(f"Отже, P1={str(v_one)}")
    return

def stalaKulona():
    printResponse("Добре, формула для обчислення 'F = k * (q1 * q2) / r ^ 2'. Отже, напишіть k.")
    k = int(getUserInput())
    printResponse("Добре, тепер q1")
    q_one = int(getUserInput())
    printResponse("Добре, тепер q2")
    q_two = int(getUserInput())
    printResponse("Як щодо r?")
    r = int(getUserInput())
    F = float(str(q_one * q_two * k / r * r))
    printResponse(f"Отже, F={str(F)}")
    return

def lawOma():
    printResponse("""Добре, формула для обчислення I = V / R, де I - струм, V - напруга, R - опір.
Скажіть V""")
    V = int(getUserInput())
    printResponse("Тепер R")
    R = int(getUserInput())
    I = float(str(V / R))
    printResponse(f"Отже, I={str(I)}")
    return

def stalaGravity():
    printResponse("""Добре, формула для обчислення F = G*m1*m2/r^2.
Скажіть m1""")
    m_one = int(getUserInput())
    printResponse("Тепер m2")
    m_two = int(getUserInput())
    printResponse("Тепер r")
    r = int(getUserInput())
    G = 6.67
    F = float(str((G*m_one*m_two)/r*r))
    printResponse(f"Отже, F={str(F)}")
    return

def distanceBetweenTwoDots():
    printResponse("""Добре, формула для обчислення 'd = sqrt((x2 - x1)^2 + (y2 - y1)^2 + (z2 - z1)^2)', де (x1, y1, z1) та (x2, y2, z2) - координати двох точок.
Отже, напишіть x1""")
    x_one = int(getUserInput())
    printResponse("Добре, тепер х2")
    x_two = int(getUserInput())
    printResponse("Добре, тепер y1")
    y_one = int(getUserInput())
    printResponse("Добре, тепер y2")
    y_two = int(getUserInput())
    printResponse("Добре, тепер z1")
    z_one = int(getUserInput())
    printResponse("Добре, тепер z2")
    z_two = int(getUserInput())
    d = float(str((x_two - x_one) ** 2 + str((y_two - y_one) ** 2) + str((z_two - z_one) ** 2)))
    printResponse(f"Отже, d={str(math.sqrt(d))}")
    return

def lengthArcCircle():
    printResponse("""Добре, формула для обчислення L = r*angle, де r - радіус кола, а angle - кут між двома
точками на колі, який вимірюється в радіанах. Напишіть r""")
    r = int(getUserInput())
    printResponse("Зрозумів, тепер напишіть angle (кут між двома точками на колі)")
    angle = int(getUserInput())
    L = float(str(r * angle))
    printResponse(f"Отже, L={str(L)}")
    return

def segmentLength():
    printResponse("""Добре, формула для обчислення AB = sqrt((x2 - x1)^2 + (y2 - y1)^2),
де (x1, y1) та (x2, y2) - координати двох точок. Отже, напишіть х1""")
    x_one = int(getUserInput())
    printResponse("Добре, тепер х2")
    x_two = int(getUserInput())
    printResponse("Добре, тепер y1")
    y_one = int(getUserInput())
    printResponse("Добре, тепер y2")
    y_two = int(getUserInput())
    AB = float(str((x_two - x_one) ** 2) + str((y_two - y_one) ** 2))
    printResponse(f"Отже, d={str(math.sqrt(AB))}")
    return

def squareCircle():
    printResponse("""Окей, формула для обчислення S = пі * r^2,
де r - радіус кола, а пі - математична константа, що дорівнює приблизно 3,14. Напишіть r.""")
    pi = 3.14
    r = int(getUserInput())
    S = float(str(pi * r ** 2))
    printResponse(f"Отже, S={str(S)}")
    return

def numberPi():
    printResponse("Оскільки число пі є константою, його значення буде 3.14")
    return

def squareRectangle():
    printResponse("Окей, формула для обчислення:S = a * b, де a та b - довжини сторін прямокутника. Скажіть a.")
    a = int(getUserInput())
    printResponse("Добре, тепер b.")
    b = int(getUserInput())
    S = float(str(a * b))
    printResponse(f"Отже, S={str(S)}")
    return

def theLargestOcean():
    printResponse("Тихий океан найбільший за площею: S – 178,7 млн. км2.")
    return

def theLargestMainland():
    printResponse("Євразія — найбільший материк на Землі, що складається з Європи та Азії.")
    return

def theLargestDesert():
    printResponse("""Друга найбільша пустеля- Аравійська,
знаходиться на Аравійському півострові і територіях таких держав, як Єгипет, Саудівська Аравія, Ірак, Сирія та Йорданія.""")
    return

def distanceBetweenDots():
    printResponse("Добре, формула для обчислення відстані: sqrt((x2-x1)^2+(y2-y1)^2). Скажіть х1 ")
    x_one = int(getUserInput())
    printResponse("Добре, тепер х2")
    x_two = int(getUserInput())
    printResponse("Добре, тепер y1")
    y_one = int(getUserInput())
    printResponse("Добре, тепер y2")
    y_two = int(getUserInput())
    AB = float(str((x_two - x_one) ^ 2) + str((y_two - y_one) ^ 2))
    printResponse(f"Отже, AB={str(math.sqrt(AB))}")
    return

def whereIsSahara():
    printResponse("""Країни, у яких розташована Сахара:
Алжир, Єгипет, Лівія, Мавританія, Малі, Марокко, Нігер, Судан, Туніс, Чад.""")
    return

def starTypes():
    printResponse("""Сім основних типів зірок включають O, B, A, F, G, K і M, кольори від синього до червоного.
Існують інші типи класифікацій зірок, такі як спектральна класифікація Єркеса.
Ця класифікація була пізніше, ніж у Гарварді, і має більш конкретну модель при класифікації зірок.""")
    return

def moonMissions():
    printResponse("""Першими, хто побував на Місяці, були учасники місії «Аполлон-11»,
далі були місії: Аполлон-12, Аполлон-14, Аполлон-15, Аполлон-16 та Аполлон-17""")
    return

def blackHoles():
    printResponse("""Чорна діра — астрофізичний об'єкт, який створює настільки потужну силу тяжіння,
що жодні, навіть найшвидші частинки, не можуть покинути його поверхню, в тому числі світло та електромагнітне випромінювання.
Чорні діри зоряних мас утворюються як кінцевий етап еволюції зір,
після повного вигоряння термоядерного палива та припинення термоядерних реакцій зоря теоретично має охолоджуватися,
що призведе до зменшення внутрішнього тиску і стиснення під дією гравітації.""")
    return

def weather():
    # city_name = input()
    printResponse(f"Уведіть назву міста:")
    city_name = getUserInput()

    url = f"https://wttr.in/{city_name}"
    try:
        data = requests.get(url)
        weather = data.text
    except:
        weather = ""

    print(Fore.CYAN + f"[Бот]: Погода в місті {city_name}: {weather}")
    writeToFile(f"[Бот]: Погоду в місті {city_name} можна дізнатись за посиланням: {url} \n")
    return

def getSeason():

    # визначаємо функцію
    def get_season(date):
        month = date.month * 100
        day = date.day
        month_day = month + day  # combining month and day

        if ((month_day >= 301) and (month_day <= 531)):
            season = "Весна"
        elif ((month_day > 531) and (month_day < 901)):
            season = "Літо"
        elif ((month_day >= 901) and (month_day <= 1130)):
            season = "Осінь"
        elif ((month_day > 1130) and (month_day <= 229)):
            season = "Зима"
        else:
            raise IndexError("Недійсні дані")

        return season

    # викликаємо функцію
    x = date.today()
    printResponse(f"{x} -> {get_season(x)}")
    return

def currentMonth():
    current_month = strftime('%B')
    if current_month == "April":
        printResponse("Квітень")
    elif current_month == "May":
        printResponse("Травень")
    return

def stoneScissorsPaper():
    printResponse("Добре, називайте фігуру перші ;)")
    spysok1 = ['камінь', 'ножиці', 'папір']
    d = choice(spysok1)
    a = getUserInput().lower();
    while a != 'камінь' and a != 'ножиці' and a != 'папір':
        # поки не введено камінь, ножиці або папір користувач буде здійснювати введення
        printResponse("Необхідно ввести камінь, ножиці або папір")
        a = getUserInput().lower()  # метод lower введені символи перетворює в нижній регістр
    printResponse(f"А моя фігура {d}")
    if (a == 'камінь' and d == 'ножиці') or (a == 'папір' and d == 'камінь') or (a == 'ножиці' and d == 'папір'):
        printResponse("Гравець переміг")
    elif (a == 'камінь' and d == 'папір') or (a == 'папір' and d == 'ножиці') or (a == 'ножиці' and d == 'камінь'):
        printResponse("РобБот переміг (тобто я :))")
    if a == d:
        printResponse("Нічия")
    return

def poems():
    import random

    list = ["""І день іде, і ніч іде.
    І голову схопивши в руки,
    Дивуєшся, чому не йде
    Апостол правди і науки!""", """Моя люба зоря ронить в серце мені,
    Наче сльози, проміння тремтяче,
    Рвуть серденько моє ті проміння страшні…
    Ох, чого моя зіронька плаче!""", """Є вчора і завтра на моїм лиці.
    І тільки нема сьогодні...
    І ходять навколо стола стільці
    такі самотні-самотні.""", """Зазирну в душу волошки — побачу блакить.
    Зазирну в душу джерела — побачу прохолоду.
    Моє почуття так освітило сонячний день,
    що було видно в небі падучу зірку.""", """Стодола, рів…
    Сто доларів…"""]

    a = random.choice(list)
    printResponse(f"{a}")
    return

def historyGame():
    printResponse("""Отже, це гра питань: хто, де, коли, навіщо, що.
Скажіть 'хто?'""")
    who = getUserInput()
    printResponse("Окей, тепер 'де?'")
    where = getUserInput()
    printResponse("Окей, тепер 'коли?'")
    when = getUserInput()
    printResponse("Окей, тепер 'навіщо?'")
    why = getUserInput()
    printResponse("Окей, тепер 'що?'")
    what = getUserInput()
    import random

    list = [f"""{who} вчив грати {what} {why} {when} {where}""",
            f"""{who} навчився малювати {what} {why} {when} {where}""",
            f"""{who} практикував кулінарії {what} {why} {when} {where}""",
            f"""{who} хотів побачити {what} {why} {when} {where}""",
            f"""{who} мріяв відвідати {what} {why} {when} {where}"""]
    b = random.choice(list)
    printResponse(f"{b}")
    return

def calendar():
    import calendar
    text_cal = calendar.TextCalendar(firstweekday=0)
    year = int(input(Fore.CYAN + "[Bot]: Уведіть рік: "))
    month = int(input(Fore.CYAN + "[Bot]: Уведіть номер місяця: "))
    print(text_cal.formatmonth(year, month))
    return

def Square():
    a = float(getUserInput())
    S = a * a
    printResponse(f"{S}")
    return


menu = [{
    "accessBy": "головне меню",
    "description": "Головне меню",
    "helpText": f"У головному меню...",
    "actions": [
        {
            "accessBy": "друк",
            "description": "Надрукувати \"Привіт\"",
            "function": printHello,
        }
    ],
    "windows": [
        {
            "accessBy": "матем",
            "description": "Математика",
            "helpText": "Тут можна вирішувати різні задачкі по математиці",
            "windows": [

            ],
            "actions": [
                {
                    "accessBy": "відстань між точками",
                    "description": "Обчислення відстані між двома точками в просторі",
                    "function": distanceBetweenTwoDots,
                },
                {
                    "accessBy": "квадрат",
                    "description": "Площа квадрата",
                    "function": Square,
                },
                {
                    "accessBy": "дуга",
                    "description": "Обчислення довжини дуги кола",
                    "function": lengthArcCircle,
                },
                {
                    "accessBy": "відрізка",
                    "description": "Обчислення довжини відрізка між двома точками на площині",
                    "function": segmentLength,
                },
                {
                    "accessBy": "площа кола",
                    "description": "Обчислення площі кола",
                    "function": squareCircle,
                },
                {
                    "accessBy": "пі",
                    "description": "Вивід числа пі",
                    "function": numberPi,
                },
                {
                    "accessBy": "площа прямок",
                    "description": "Обчислення площі прямокутника",
                    "function": squareRectangle,
                },
            ],
        },
        {
            "accessBy": "фіз",
            "description": "Фізика",
            "helpText": "Тут можна вирішувати всякі задачки по фізиці",
            "windows": [
                
            ],
            "actions": [
                {
                    "accessBy": "бойля",
                    "description": "Закон Бойля-Маріотта",
                    "function": BoylMariott,
                },
                {
                    "accessBy": "кулон",
                    "description": "Вивід кулонівської сталої",
                    "function": stalaKulona,
                },
                {
                    "accessBy": "ома",
                    "description": "Закон Ома",
                    "function": lawOma,
                },
                {
                    "accessBy": "гравітац",
                    "description": "Вивести гравітаційну сталу",
                    "function": stalaGravity,
                },
            ],
        },
        {
            "accessBy": "геогр",
            "description": "Географія",
            "helpText": "Тут можна вирішувати всякі задачки з географії",
            "windows": [

            ],
            "actions": [
                {
                    "accessBy": "найбільший океан",
                    "description": "Який океан найбільший за площею",
                    "function": theLargestOcean,
                },
                {
                    "accessBy": "найбільший материк",
                    "description": "Який материк найбільший за площею",
                    "function": theLargestMainland,
                },
                {
                    "accessBy": "пустеля",
                    "description": "Країна, у якій знаходиться найбільша пустеля після Сахари",
                    "function": theLargestDesert,
                },
                {
                    "accessBy": "відстань між точками",
                    "description": "Знайти відстань між двома точками А (x1, y1) та В (x2, y2)",
                    "function": distanceBetweenDots,
                },
                {
                    "accessBy": "сахара",
                    "description": "Де знаходиться Сахара",
                    "function": whereIsSahara,
                },
            ],
        },
        {
            "accessBy": "астроном",
            "description": "Астрономія",
            "helpText": "Тут можна вирішувати всякі задачки з астрономії",
            "windows": [

            ],
            "actions": [
                {
                    "accessBy": "типи зір",
                    "description": "Які типи зір відомі в астрономії",
                    "function": starTypes,
                },
                {
                    "accessBy": "місії",
                    "description": "Які наукові місії здійснювалися на Місяці",
                    "function": moonMissions,
                },
                {
                    "accessBy": "чорні дії",
                    "description": "Що таке чорні діри та як вони виникають",
                    "function": blackHoles,
                },
            ],
        },
        {
            "accessBy": "загал",
            "description": "Загальні",
            "helpText": "Тут можна ставити всякі загальні питання та завдання",
            "windows": [

            ],
            "actions": [
                {
                    "accessBy": "погода",
                    "description": "Яка зараз погода",
                    "function": weather,
                },
                {
                    "accessBy": "пора року",
                    "description": "Яка зараз пора року",
                    "function": getSeason,
                },
                {
                    "accessBy": "місяць",
                    "description": "Який зараз місяць",
                    "function": currentMonth,
                },
                {
                    "accessBy": "пограти",
                    "description": "Пограти у камінь-ножиці-папір",
                    "function": stoneScissorsPaper,
                },
                {
                    "accessBy": "вірш",
                    "description": "Зачитати вірш",
                    "function": poems,
                },
                {
                    "accessBy": "історія",
                    "description": "Гра «історія»",
                    "function": historyGame,
                },
                {
                    "accessBy": "календар",
                    "description": "Календарик",
                    "function": calendar,
                },
            ]
        }
    ]
}]
pattern = "*.txt"
files = glob.glob(pattern)
for file in files:
    os.remove(file)

createFile()
printResponse(f"Привіт, користувач, мене звати РобБот")
while True:
    if len(movementHistory) == 0:
        break
    
    setCurrentElement()
    
    if isShowMenuNeeded == True:
        printMenuInfo()

        isShowMenuNeeded = False

    try:
        input_text = getUserInput()
    except KeyboardInterrupt:
        break
    
    if input_text.lower() == "д" or input_text.lower() == "?" or input_text.lower() == "допомога":
        printResponse(getSomeHelp())
        continue

    if input_text.lower() == "н" or input_text.lower() == "назад":
        isShowMenuNeeded = True
        moveBackward()
        continue
    
    if input_text.lower() == "в" or input_text.lower() == "вихід":
        exit()
        continue
    
    if moveTo(input_text) == True:
        isShowMenuNeeded = True
        continue
    else:
        if doAction(input_text.lower()) == True:
            continue
        else:
            printResponse("Такого вікна або дії немає!")
            continue

printResponse("Бувай")
closeFile()

    
    
    


    







