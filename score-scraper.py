from dataclasses import dataclass, field
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import datetime, sys, json


@dataclass
class Results:
    round_scores: list[int] = field(default_factory=list)
    round_distances: list[int] = field(default_factory=list)
    round_times: list[str] = field(default_factory=list)
    total_time : str = ""
    total_score: int = 0
    total_distance: str = ""
    game_title: str = ""

def results_to_json(results: Results) -> str:
    """Convert the Results dataclass to a dictionary"""
    results_dict = {
        "RoundScores": results.round_scores,
        "RoundDistances": results.round_distances,
        "RoundTimes": results.round_times,
        "TotalTime": results.total_time,
        "TotalScore": results.total_score,
        "TotalDistance": results.total_distance,
        "GameTitle": results.game_title
    }

    # Convert the dictionary to a JSON string
    results_json = json.dumps(results_dict)

    return results_json

def get_score_from_url(url):
    """ Scrapes info from geoguessr using selenium. """
    options = Options()
    driver=webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get(url)
    scores=[]
    # Find elements by class on the webpage
    driver.implicitly_wait(1)
    scores = driver.find_elements(By.CSS_SELECTOR, "[class*=results_score__]")
    details = driver.find_elements(By.CSS_SELECTOR, "[class*=results_scoreDetails__]")
    game_title = driver.find_element(By.CSS_SELECTOR, "[class*=info-card_title__]").text
    
    
    # Parse Text
    score_list = []
    dist_list = []
    time_list = []
    for score in scores:
        text = score.text
        text = text.replace(" pts", "")
        text = text.replace(",", "")
        score_list.append(int(text))

    for detail in details:
        dist, time = detail.text.split(" - ")
        time = time.replace(" min, ", ":")
        time = time.replace(" sec", "")
        try:
            if len(time.split(":")[1]) == 1:
                time = time.split(":")[0] + ":0" + time.split(":")[1]
        except IndexError:
            pass
        dist_list.append(dist)
        time_list.append(time)

    total_score = score_list.pop()
    total_dist = dist_list.pop()
    total_time = time_list.pop()

    return ((total_score, total_dist, total_time)), score_list, dist_list, time_list, game_title

def main(url):
    results = Results()
    totals, scores, dists, times, game_title = get_score_from_url(url)
    results.total_score = totals[0]
    results.total_distance = totals[1]
    results.total_time = totals[2]
    results.round_scores = scores
    results.round_distances = dists
    results.round_times = times
    results.game_title = game_title
    return results_to_json(results)

if __name__ == "__main__":
    print(main(sys.argv[1]))
