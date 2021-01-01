from reward import *

# Tests: stay_on_track_reward
# ---------------------------------------
def test_stay_on_track_reward_should_return_correct_reward1():
  reward = 0
  params = {
      "all_wheels_on_track": True
  }
  assert stay_on_track_reward(reward, params['all_wheels_on_track']) == (REWARD_LARGE * WEIGHTING_ON_TRACK)

def test_stay_on_track_reward_should_return_correct_reward2():
  reward = 1
  params = {
      "all_wheels_on_track": False
  }
  assert stay_on_track_reward(reward, params['all_wheels_on_track']) == 0.75

# Tests: reward_function
# ---------------------------------------
def test_reward_function_should_return_correct_reward():
    reward = 0
    params = {
        "all_wheels_on_track": True
    }
    expected_reward = 1e-3
    expected_reward += (REWARD_LARGE * WEIGHTING_ON_TRACK)

    assert reward_function(params) == expected_reward
