import pandas as pd
from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.endpoints import PlayerDashboardByGeneralSplits
from nba_api.stats.endpoints import commonplayerinfo

"""
https://pypi.org/project/nba-api/
https://github.com/datasets/nba/blob/main/docs/nba_api.md

# with pd.option_context('display.max_columns', None):
#     print(player_bio.get_data_frames()[0])

import pybaseball
import nfl_data_py
import pyfootball
"""

def get_player_name(name):
    player_id = [player['id'] for player in players.get_players() if player['full_name'] == name][0]
    return player_id
def get_career_stats(player_id):
    career_stats = playercareerstats.PlayerCareerStats(player_id=player_id)
    with pd.option_context('display.max_columns', None):
        print(career_stats.get_data_frames()[0])
    return career_stats.get_data_frames()[0]

def get_current_stats(player_id):
    season_stats = PlayerDashboardByGeneralSplits(player_id=player_id, season='2022-23')
    with pd.option_context('display.max_columns', None):
        print(season_stats.get_data_frames()[0])
    return season_stats.get_data_frames()[0]

def get_player_bio(player_id):
    player_bio = commonplayerinfo.CommonPlayerInfo(player_id=player_id)
    with pd.option_context('display.max_columns', None):
        print(player_bio.get_data_frames()[0])
    return player_bio.get_data_frames()[0]

def favorite_player():
    q = print("Would you like to add this as one of your favorite players?")
    if q == "y" or q == "Y" or q == "yes" or q == "Yes":
        print("Adding to your favorite players")
    #SQLDB

def main():
    """
    Main function for the NBA stats program.
    """
    name = input("Enter player name: ")
    pid=get_player_name(name)
    # cs = get_career_stats(pid)
    # print(cs)
    # ps= get_current_stats(pid)
    # print(ps)
    # pb= get_player_bio(pid)
    # print(pb)
    stats = get_career_stats(pid)
    print(stats.columns)
    stats1= get_current_stats(pid)
    print(stats1.columns)
    stats2= get_player_bio(pid)
    print(stats2.columns)


if __name__ == "__main__":
    main()