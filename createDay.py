from os import makedirs, rename, path
from requests import get
from bs4 import BeautifulSoup

def makePart2(year, title):
    if not path.exists(f"{year}/{title}/part2.py") and open(f"{year}/{title}/part1.txt", "r").read() != "":
        open(f"{year}/{title}/part2.py", "w").write(f'input = open("{year}/{title}/input.txt", "r").read().split("\\n")\nendValue = 0')

def getPage(year, day, sessionCookie):
    url = f"https://adventofcode.com/{year}/day/{day}"
    headers = {"Cookie": f"session={sessionCookie}"}
    return get(url, headers=headers)

def updateDay(year, day, title):
    part = getPartAndTitle(year, day, sessionCookie, 2)
    open(f"{year}/{title}/part1.txt", "w").write(str(part))
    makePart2(year, title)

def createDirectories(year, day, title):
    if path.exists(f"{year}/Day {day}"):
        rename(f"{year}/Day {day}", f"{year}/{title}")
    else:
        makedirs(f"{year}/{title}", exist_ok=True)

def getInput(year, day, sessionCookie):
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    headers = {"Cookie": f"session={sessionCookie}"}
    return get(url, headers=headers).text

def makeDay(year, day, sessionCookie):
    partAndTitle = getPartAndTitle(year, day, sessionCookie, 1)
    title = partAndTitle[1].replace('--- ', '').replace(' ---', '').replace(':', ' -') if partAndTitle else None
    if title is not None:
        title = ''.join(c for c in title if c.isalnum() or c.isspace() or c in ['-', '_'])
    part = partAndTitle[0].replace(partAndTitle[1], '') if partAndTitle else None
    input = getInput(year, day, sessionCookie)

    createDirectories(year, day, title)
    open(f"{year}/{title}/part1.txt", "w").write(str(part))
    makePart2(year, title)
    open(f"{year}/{title}/input.txt", "w").write(str(input))

def getPartAndTitle(year, day, sessionCookie, part):
    """
    Returns the part1 and title of the day or part2.
    """

    page = getPage(year, day, sessionCookie)
    soup = BeautifulSoup(page.text, 'html.parser')

    match(part):
        case 1: 
            element = soup.select_one('body > main > article:nth-child(1)')
            title = soup.select_one('body > main > article > h2')
            if element and title: return element.text, title.text
        case 2: 
            element =  soup.select_one('body > main > article:nth-child(3)')
            if element: return element.text

sessionCookie = input("Enter your session cookie: ")

for year in range(2015, 2023 + 1):
    for day in range(1, 24 + 1):
        makeDay(year, day, sessionCookie)
        print(f"Year {year} day {day} done.")

try: 
    while True:
        yearAndDay = input("Give me part 2 of: [2023 1]: ").split()
        updateDay(yearAndDay[0], yearAndDay[1], sessionCookie)
except KeyboardInterrupt: print("\nKeyboardInterrupt")