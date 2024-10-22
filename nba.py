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

"""


def get_career_stats(name):
    player_id = [player['id'] for player in players.get_players() if player['full_name'] == name][0]
    career_stats = playercareerstats.PlayerCareerStats(player_id=player_id)
    return career_stats.get_data_frames()[0]

def get_player_stats(name):
    player_id = [player['id'] for player in players.get_players() if player['full_name'] == name][0]
    season_stats = PlayerDashboardByGeneralSplits(player_id=player_id, season='2022-23')
    return season_stats.get_data_frames()[0]

def get_player_bio(name):
    player_id = [player['id'] for player in players.get_players() if player['full_name'] == name][0]
    player_bio = commonplayerinfo.CommonPlayerInfo(player_id=player_id)
    return player_bio.get_data_frames()[0]

def main():
    """
    Main function for the NBA stats program.
    """
    name = input("Enter player name: ")
    print(get_career_stats(name))
    print(get_player_stats(name))
    print(get_player_bio(name))

    
if __name__ == "__main__":
    main()