from bs4 import BeautifulSoup
import requests

URL = "https://www.billboard.com/charts/hot-100/"

# -- GET HTML FILE 
response = requests.get("https://www.billboard.com/charts/hot-100/")
response = response.text

soup = BeautifulSoup(response, "html.parser")

# --FIND TOP 100 SONGS HIT
songs = soup.find_all(
    name= "h3", 
    class_= "c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only"
    )

first_song = soup.find(
    name= "h3",
    class_= "c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 u-font-size-23@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-245 u-max-width-230@tablet-only u-letter-spacing-0028@tablet" 
)

songs.insert(0, first_song)

songs = [song.getText().replace("\n", "") for song in songs]

# --GET SINGERS 
singers = soup.find_all(
    name= "span", 
    class_= "c-label a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only"
    )

first_singer = soup.find(
    name= "span", 
    class_= "c-label a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only u-font-size-20@tablet"
    )

singers.insert(0, first_singer)

singers = [singer.getText().replace("\n", "") for singer in singers]

# --GET POSITION, PEAK POSITION, WEEKS ON CHART

lastweek_pos = soup.find_all(
    name= "span", 
    class_= "c-label a-font-primary-m lrv-u-padding-tb-050@mobile-max"
    )

first_lastweek_pos = soup.find_all(
    name= "span", 
    class_= "c-label a-font-primary-bold-l a-font-primary-m@mobile-max u-font-weight-normal@mobile-max lrv-u-padding-tb-050@mobile-max u-font-size-32@tablet"
    )

lastweek_pos = first_lastweek_pos + lastweek_pos

lastweek_pos = [place.getText().replace("\n", "") for place in lastweek_pos]

current_pos = []
peak_pos = []
weeks_on_chart = []
for i in range(0, len(lastweek_pos), 6):
    current_pos.append(lastweek_pos[i])
    peak_pos.append(lastweek_pos[i + 1])
    weeks_on_chart.append(lastweek_pos[i + 2])
    

