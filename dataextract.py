import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.transfermarkt.co.in/vergleich/vereineBegegnungen/statistik/131_418"

headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "lxml")

rows = soup.select("table tbody tr")

data = []

for row in rows:
    try:
        cols = row.find_all("td")
        
        #Competition (logo alt text)
        competition = row.select_one("img.wettbewerblogo")["alt"]

        # Matchday = FIRST hidden desktop column
        matchday = cols[2].get_text(strip=True)

        # Date = mobile date column (show-for-small)
        date = row.select_one("td.zentriert.show-for-small").get_text(strip=True)   

        #Home Team (6th td → first anchor inside)
        home_team = cols[5].find("a")["title"]

        #Away Team (9th td → first anchor inside)
        away_team = cols[8].find("a")["title"]

        #Attendance
        attendance = row.select_one("td.rechts").get_text(strip=True)

        #Result
        result = row.select_one("a.ergebnis-link").get_text(strip=True)

        #SAFE RESULT EXTRACTION
        result_tag = row.select_one("a.ergebnis-link span")

        if result_tag:
            result = result_tag.get_text(strip=True)
            span_class = result_tag.get("class", [])

            if "greentext" in span_class:
                winner = "FC Barcelona"
            elif "redtext" in span_class:
                winner = "Real Madrid"
            else:
                winner = "Draw"
        else:
            result = "Not played"
            winner = "TBD"

        data.append([
            competition,
            matchday,
            date,
            home_team,
            away_team,
            attendance,
            result,
            winner
        ])

    except Exception as e:
        print("Skipped row:", e)

# create dataframe
df = pd.DataFrame(data, columns=[
    "Competition",
    "Matchday",
    "Date",
    "Home Team",
    "Away Team",
    "Attendance",
    "Result",
    "Winner"
])

df.to_csv("matches.csv", index=False, encoding="utf-8")
df.to_excel("matches.xlsx", index=False)

print("✅ Scraping Finished!")
print(df.head())