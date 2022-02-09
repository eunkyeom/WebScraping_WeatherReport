# 네이버 오늘의 날씨 정보 스크래핑

import requests
from bs4 import BeautifulSoup
import re


def scrape_weather():
    print("[오늘의 날씨]")
    url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8"
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "html.parser")
    
    # 오늘 날씨 : ex) 어제보다 1° 높아요  맑음
    summary = soup.find("p", attrs={"class":"summary"}).get_text()
    print(summary)
    print("")

    # 현재 온도 (최저 온도 / 최고 온도)
    curr_temp = soup.find("div", attrs={"class":"temperature_text"}).get_text().replace(" 현재 온도", "") # 4°
    print(f"현재 온도 : {curr_temp}")

    min_temp = soup.find("span", attrs={"class":"lowest"}).get_text().replace("최저기온", "") # -4°
    print(f"최저 온도 : {min_temp}")

    max_temp = soup.find("span", attrs={"class":"highest"}).get_text().replace("최고기온", "") # 6°
    print(f"최고 온도 : {max_temp}")

    # 오전 강수확률 OO%, 오후 강수확률 OO%
    rainfall = soup.find_all("span", attrs={"class":"weather_left"})
    for idx, rainfall_idx in enumerate(rainfall):
        if idx == 0:
            rainfall_morning = rainfall_idx
            print("")
            print("강수 확률 :", rainfall_morning.get_text())
        elif idx == 1:
            rainfall_afternoon = rainfall_idx
            print("강수 확률 :", rainfall_afternoon.get_text())
    
    # 미세먼지
    dusts = soup.find("li", attrs={"class":"item_today level1"})
    # print(dusts[0].find("li", attrs={"class":"item_today level1"}))
    dusts = dusts.get_text()[2:]
    print("")
    print(dusts)
    

if __name__ == "__main__":
    scrape_weather() # 오늘의 날씨정보 가져오기, 직접 실행할 때만 동작하도록 함수 정의, 다른 파일에 의해서 호출될 때는 실행이 되지 않도록

