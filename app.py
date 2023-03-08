from bs4 import BeautifulSoup
import requests
from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get('/')
def index():
    return {'message': 'Get Live Scores Here'}


@app.get('/score')
def get_score():
    try:
        url = "https://www.cricbuzz.com/cricket-match/live-scores"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        match = soup.find_all('div', class_="cb-col cb-col-100 cb-plyr-tbody cb-rank-hdr cb-lv-main")
        match1 = match[0]
        match1_league = match1.find_all('h2', class_="cb-lv-grn-strip text-bold cb-lv-scr-mtch-hdr")[0].text.strip()
        match1_teams = match1.find_all('h3', class_="cb-lv-scr-mtch-hdr inline-block")[0].text.strip()
        match1_no = match1.find_all('span', class_="text-gray")[0].text.strip()
        match1_venue = match1.find_all('span', class_="text-gray")[1].text.strip()
        match1_team_1 = match1.find_all('div', class_="cb-ovr-flo cb-hmscg-tm-nm")[0].text.strip()
        match1_team_1_det = match1.find_all('div', class_="cb-ovr-flo")[2].text.strip()
        match1_team_2 = match1.find_all('div', class_="cb-ovr-flo")[3].text.strip()
        match1_team_2_det = match1.find_all('div', class_="cb-ovr-flo")[4].text.strip()
        match1_link = url + match1.find("a", {"class": "cb-lv-scrs-well"}).get("href").strip()

        match2 = match[1]
        match2_league = match2.find_all('h2', class_="cb-lv-grn-strip text-bold cb-lv-scr-mtch-hdr")[0].text.strip()
        match2_teams = match2.find_all('h3', class_="cb-lv-scr-mtch-hdr inline-block")[0].text.strip()
        match2_no = match2.find_all('span', class_="text-gray")[0].text.strip()
        match2_venue = match2.find_all('span', class_="text-gray")[1].text.strip()
        match2_team_1 = match2.find_all('div', class_="cb-ovr-flo cb-hmscg-tm-nm")[0].text.strip()
        match2_team_1_det = match2.find_all('div', class_="cb-ovr-flo")[2].text.strip()
        match2_team_2 = match2.find_all('div', class_="cb-ovr-flo")[3].text.strip()
        match2_team_2_det = match2.find_all('div', class_="cb-ovr-flo")[4].text.strip()
        match2_link = url + match2.find("a", {"class": "cb-lv-scrs-well"}).get("href").strip()

        match3 = match[2]
        match3_league = match3.find_all('h2', class_="cb-lv-grn-strip text-bold cb-lv-scr-mtch-hdr")[0].text.strip()
        match3_teams = match3.find_all('h3', class_="cb-lv-scr-mtch-hdr inline-block")[0].text.strip()
        match3_no = match3.find_all('span', class_="text-gray")[0].text.strip()
        match3_venue = match3.find_all('span', class_="text-gray")[1].text.strip()
        match3_team_1 = match3.find_all('div', class_="cb-ovr-flo cb-hmscg-tm-nm")[0].text.strip()
        match3_team_1_det = match3.find_all('div', class_="cb-ovr-flo")[2].text.strip()
        match3_team_2 = match3.find_all('div', class_="cb-ovr-flo")[3].text.strip()
        match3_team_2_det = match3.find_all('div', class_="cb-ovr-flo")[4].text.strip()
        match3_link = url + match3.find("a", {"class": "cb-lv-scrs-well"}).get("href").strip()

        return {
            "match_1": {
                "league": match1_league,
                "teams": match1_teams,
                "no": match1_no,
                "venue": match1_venue,
                "team_1": match1_team_1,
                "team_1_det": match1_team_1_det,
                "team_2": match1_team_2,
                "team_2_det": match1_team_2_det,
                "link": match1_link
            },
            "match_2": {
                "league": match2_league,
                "teams": match2_teams,
                "no": match2_no,
                "venue": match2_venue,
                "team_1": match2_team_1,
                "team_1_det": match2_team_1_det,
                "team_2": match2_team_2,
                "team_2_det": match2_team_2_det,
                "link": match2_link
            },
            "match_3": {
                "league": match3_league,
                "teams": match3_teams,
                "no": match3_no,
                "venue": match3_venue,
                "team_1": match3_team_1,
                "team_1_det": match3_team_1_det,
                "team_2": match3_team_2,
                "team_2_det": match3_team_2_det,
                "link": match3_link
            },
        }

    except:
        return "Unable To Fetch Data!!"


if __name__ == '__main__':
    uvicorn.run(app)