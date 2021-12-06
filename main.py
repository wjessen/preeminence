__author__ = "Wayne M Jessen"
__email__ = "jessenwm@gmail.com"

import logging
import os
import warnings
from pathlib import Path

import pytest
from dotenv import load_dotenv

from yfpy import Data
from yfpy.logger import get_logger
from yfpy.models import Game, StatCategories, User, Scoreboard, Settings, Standings, League, Player, Team, \
    TeamPoints, TeamStandings, Roster
from yfpy.query import YahooFantasySportsQuery
from yfpy.utils import prettify_data

logger = get_logger(__name__)

# Suppress YahooFantasySportsQuery debug logging
logging.getLogger("yfpy.query").setLevel(level=logging.INFO)

# Ignore resource warnings from unittest module
warnings.simplefilter("ignore", ResourceWarning)

# load python-dotenv to parse environment variables
env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)

# Turn on/off example code stdout logging output
log_output = False

# Turn on/off automatic opening of browser window for OAuth
browser_callback = True

# Put private.json (see README.md) in test/ directory
auth_dir = Path(".")

# Example code will output data here
# data_dir = Path(__file__).parent / "test_output"
data_dir = Path(__name__).parent / "test_output"


season = "2021"
league_player_limit = 101
game_key = "406"  # NFL - 2021
game_code = "nfl"
league_id = "718110"  # NFL - 2021

team_id = 4
# team_name = "Legion"
player_id = "7200"  # NFL: Aaron Rodgers - 2020/2021

player_key = game_key + ".p." + player_id

# Instantiate yfpy objects
yahoo_data = Data(data_dir)
yahoo_query = YahooFantasySportsQuery(
    auth_dir,
    league_id,
    game_id=game_key,
    game_code=game_code,
    offline=False,
    all_output_as_json=False,
    consumer_key=os.environ["YFPY_CONSUMER_KEY"],
    consumer_secret=os.environ["YFPY_CONSUMER_SECRET"],
    browser_callback=browser_callback
)

league_data = yahoo_query.get_league_data()


if (__name__ == "__main__"):
    yfq = YahooFantasySportsQuery(

    )
    yfq.login()