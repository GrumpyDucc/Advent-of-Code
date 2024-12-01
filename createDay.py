from os import makedirs, rename, listdir, path
from requests import get
from bs4 import BeautifulSoup

def makePy(year, title, part):
    match(part):
        case 1:
            if not path.exists(f"{year}/{title}/part{part}.py"):
                open("template.py", "r").read()
                open(f"{year}/{title}/part{part}.py", "w").write(f'')
        case 2:
            if not path.exists(f"{year}/{title}/part{part}.py") and path.getsize(f"{year}/{title}/part{part}.py") == 0:
                open(f"{year}/{title}/part{part}.py", "w").write(open(f"{year}/{title}/part1.py", "r").read())

def getPage(year, day, sessionCookie):
    url = f"https://adventofcode.com/{year}/day/{day}"
    headers = {"Cookie": f"session={sessionCookie}"}
    return get(url, headers=headers)

def addPartTwo(year, day):
    part = getPartAndTitle(year, day, sessionCookie, 2)
    #title = listdir(year)[int(day) - 1]
    title = listdir(year)
    open(f"{year}/{title}/part2.txt", "w").write(str(part))
    print(title)
    makePy(year, title, 2)

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
    makePy(year, title, 1)
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
            element =  soup.select_one('body > main > article:nth-child(4)')
            if element: return element.text

sessionCookie = input("Enter your session cookie: ")

if input("Do you want to create all days? [y/n]: ").lower() == "y":
    for year in range(2015, 2023 + 1):
        for day in range(1, 24 + 1):
            makeDay(year, day, sessionCookie)
            print(f"Year {year} day {day} done.")
else:
    try:
        while True:
            yearAndDay = input("Make Part 2 of: [2023 1]: ").split()
            addPartTwo(yearAndDay[0], yearAndDay[1])
    except KeyboardInterrupt: print("\nKeyboardInterrupt")
