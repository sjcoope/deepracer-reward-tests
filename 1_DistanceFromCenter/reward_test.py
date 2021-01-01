from reward import *

# Tests: distance_from_center_reward
# ---------------------------------------
def test_when_within_zone_1_distance_from_center_reward_should_return_correct_reward():
    reward = 0
    params = {
        "track_width": 76,
        "distance_from_center": 7.1
    }
    assert distance_from_center_reward(reward, params['track_width'], params['distance_from_center']) == (REWARD_LARGE * WEIGHTING_DIST_FROM_CENTER)

def test_when_within_zone_2_distance_from_center_reward_should_return_correct_reward():
    reward = 0
    params = {
        "track_width": 76,
        "distance_from_center": 15
    }
    assert distance_from_center_reward(reward, params['track_width'], params['distance_from_center']) == (REWARD_MED * WEIGHTING_DIST_FROM_CENTER)

def test_when_within_zone_3_distance_from_center_reward_should_return_correct_reward():
    reward = 0
    params = {
        "track_width": 76,
        "distance_from_center": 25
    }
    assert distance_from_center_reward(reward, params['track_width'], params['distance_from_center']) == (REWARD_SMALL * WEIGHTING_DIST_FROM_CENTER)

def test_when_off_track_distance_from_center_reward_should_return_correct_reward():
    reward = 0
    params = {
        "track_width": 76,
        "distance_from_center": 40
    }
    assert distance_from_center_reward(reward, params['track_width'], params['distance_from_center']) == REWARD_MIN

# Tests: reward_function
# ---------------------------------------
def test_reward_function_should_return_correct_reward():
    reward = 0
    params = {
        "track_width": 76,
        "distance_from_center": 15
    }
    expected_reward = 1e-3
    expected_reward += (REWARD_MED * WEIGHTING_DIST_FROM_CENTER)

    assert reward_function(params) == expected_reward
