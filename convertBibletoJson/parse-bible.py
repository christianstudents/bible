from bs4 import BeautifulSoup
import re
import json

# Parameters


Bible = {
    "Gen": {},
    "Exo": {},
    "Lev": {},
    "Num": {},
    "Deut": {},
    "Josh": {},
    "Judg": {},
    "Ruth": {},
    "1 Sam": {},
    "2 Sam": {},
    "1 Kings": {},
    "2 Kings": {},
    "1 Chron": {},
    "2 Chron": {},
    "Ezra": {},
    "Neh": {},
    "Esth": {},
    "Job": {},
    "Psa": {},
    "Prov": {},
    "Eccl": {},
    "S.S": {},
    "Isa": {},
    "Jer": {},
    "Lam": {},
    "Ezek": {},
    "Dan": {},
    "Hosea": {},
    "Joel": {},
    "Amos": {},
    "Oba": {},
    "Jonah": {},
    "Micah": {},
    "Nahum": {},
    "Hab": {},
    "Zeph": {},
    "Hag": {},
    "Zech": {},
    "Mal": {},
    "Matt": {},
    "Mark": {},
    "Luke": {},
    "John": {},
    "Acts": {},
    "Rom": {},
    "1 Cor": {},
    "2 Cor": {},
    "Gal": {},
    "Eph": {},
    "Phil": {},
    "Col": {},
    "1 Thes": {},
    "2 Thes": {},
    "1 Tim": {},
    "2 Tim": {},
    "Titus": {},
    "Philem": {},
    "Heb": {},
    "James": {},
    "1 Pet": {},
    "2 Pet": {},
    "1 John": {},
    "2 John": {},
    "3 John": {},
    "Jude": {},
    "Rev": {}
}

def parseBook(key, refShort, refLong, file):
    verse_loc = 3
    pattern = r'[0-9]'
    with open(file) as fp:
        soup = BeautifulSoup(fp, "html.parser")

    chapters = soup.find_all("div",'bible-text') # finding the chapters
    Bible[key] = {
        "ref": refShort,
        "refLong": refLong,
        "numChapters": len(chapters),
        "chapters": []
    }

    for c in range(0, len(chapters)):
        chapterNum = str(c+1)
        verses = chapters[c].contents[verse_loc].text  # grabbing the text
        verses = re.sub(pattern, '', verses)
        verses = verses.strip()
        verses = verses.split('\n')  # splitting the text into a list of verses
        chapterJson = {"ref": refShort + ' ' + chapterNum,
                       "refLong": refLong + ' ' + chapterNum,
                       "numVerses": len(verses),
                       "verses": []}
        for i in range(0, len(verses)):
            verseNum = str(i+1)
            chapterJson["verses"].append({
                "ref":  refShort + ' ' + chapterNum + ':' + verseNum,
                "refLong": refLong + ' ' + chapterNum + ':' + verseNum,
                "text": verses[i].strip()
            })
        Bible[key]["chapters"].append(chapterJson)

    return


parseBook("Gen", "Gen.", "Genesis", "1-genesis.html")
parseBook("Exo", "Exo.", "Exodus", "2-exodus.html")
parseBook("Lev", "Lev.", "Leviticus", "3-leviticus.html")
parseBook("Num", "Num.", "Numbers", "4-numbers.html")
parseBook("Deut", "Deut.", "Deuteronomy", "5-deuteronomy.html")
parseBook("Josh", "Josh.", "Joshua", "6-joshua.html")
parseBook("Judg", "Judg.", "Judges", "7-judges.html")
parseBook("Ruth", "Ruth", "Ruth", "8-ruth.html")
parseBook("1 Sam", "1 Sam.", "1 Samuel", "9-1samuel.html")
parseBook("2 Sam", "2 Sam.", "2 Samuel", "10-2samuel.html")
parseBook("1 Kings", "1 Kings", "1 Kings", "11-1kings.html")
parseBook("2 Kings", "2 Kings", "2 Kings", "12-2kings.html")
parseBook("1 Chron", "1 Chron.", "1 Chronicles", "13-1chronicles.html")
parseBook("2 Chron", "2 Chron.", "2 Chronicles", "14-2chronicles.html")
parseBook("Ezra", "Ezra", "Ezra", "15-ezra.html")
parseBook("Neh", "Neh.", "Nehemiah", "16-nehemiah.html")
parseBook("Esth", "Esth.", "Esther", "17-esther.html")
parseBook("Job", "Job", "Job", "18-job.html")
parseBook("Psa", "Psa.", "Psalms", "19-psalms.html")
parseBook("Prov", "Prov.", "Proverbs", "20-proverbs.html")
parseBook("Eccl", "Eccl.", "Ecclesiastes", "21-ecclesiastes.html")
parseBook("S.S", "S.S.", "Song of Solomon", "22-song_of_songs.html")
parseBook("Isa", "Isa.", "Isaiah", "23-isaiah.html")
parseBook("Jer", "Jer.", "Jeremiah", "24-jeremiah.html")
parseBook("Lam", "Lam.", "Lamentations", "25-lamentations.html")
parseBook("Ezek", "Ezek.", "Ezekiel", "26-ezekiel.html")
parseBook("Dan", "Dan.", "Daniel", "27-daniel.html")
parseBook("Hosea", "Hosea", "Hosea", "28-hosea.html")
parseBook("Joel", "Joel", "Joel", "29-joel.html")
parseBook("Amos", "Amos", "Amos", "30-amos.html")
parseBook("Oba", "Oba.", "Obadiah", "31-obadiah.html")
parseBook("Jonah", "Jonah", "Jonah", "32-jonah.html")
parseBook("Micah", "Micah", "Micah", "33-micah.html")
parseBook("Nahum", "Nahum", "Nahum", "34-nahum.html")
parseBook("Hab", "Hab.", "Habakkuk", "35-habakkuk.html")
parseBook("Zeph", "Zeph.", "Zephaniah", "36-zephaniah.html")
parseBook("Hag", "Hag.", "Haggai", "37-haggai.html")
parseBook("Zech", "Zech.", "Zechariah", "38-zechariah.html")
parseBook("Mal", "Mal.", "Malachi", "39-malachi.html")
parseBook("Matt", "Matt.", "Matthew", "40-matthew.html")
parseBook("Mark", "Mark", "Mark", "41-mark.html")
parseBook("Luke", "Luke", "Luke", "42-luke.html")
parseBook("John", "John", "John", "43-john.html")
parseBook("Acts", "Acts", "Acts", "44-acts.html")
parseBook("Rom", "Rom.", "Romans", "45-romans.html")
parseBook("1 Cor", "1 Cor.", "1 Corinthians", "46-1corinthians.html")
parseBook("2 Cor", "2 Cor.", "2 Corinthians", "47-2corinthians.html")
parseBook("Gal", "Gal.", "Galatians", "48-galatians.html")
parseBook("Eph", "Eph.", "Ephesians", "49-ephesians.html")
parseBook("Phil", "Phil.", "Philippians", "50-philippians.html")
parseBook("Col", "Col.", "Colossians", "51-colossians.html")
parseBook("1 Thes", "1 Thes.", "1 Thessalonians", "52-1thessalonians.html")
parseBook("2 Thes", "2 Thes.", "2 Thessalonians", "53-2thessalonians.html")
parseBook("1 Tim", "1 Tim.", "1 Timothy", "54-1timothy.html")
parseBook("2 Tim", "2 Tim.", "2 Timothy", "55-2timothy.html")
parseBook("Titus", "Titus", "Titus", "56-titus.html")
parseBook("Philem", "Philem.", "Philemon", "57-philemon.html")
parseBook("Heb", "Heb.", "Hebrews", "58-hebrews.html")
parseBook("James", "James", "James", "59-james.html")
parseBook("1 Pet", "1 Pet.", "1 Peter", "60-1peter.html")
parseBook("2 Pet", "2 Pet.", "2 Peter", "61-2peter.html")
parseBook("1 John", "1 John", "1 John", "62-1john.html")
parseBook("2 John", "2 John", "2 John", "63-2john.html")
parseBook("3 John", "3 John", "3 John", "64-3john.html")
parseBook("Jude", "Jude", "Jude", "65-jude.html")
parseBook("Rev", "Rev.", "Revelation", "66-revelation.html")

with open('bible.json', 'w', encoding='utf-8') as f:
    json.dump(Bible, f, ensure_ascii=False, indent=4)