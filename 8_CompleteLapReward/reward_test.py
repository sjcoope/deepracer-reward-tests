from reward import *

# Tests: completed_lap_reward
# ---------------------------------------
def test_completed_lap_reward_should_return_correct_reward1():
    reward = 0
    progress = 20
    expected_reward = 0

    # TEST: Test progress less than 50% returns no reward
    assert completed_lap_reward(reward, progress) == expected_reward

def test_completed_lap_reward_should_return_correct_reward2():
    reward = 0
    progress = 99
    expected_reward = 0

    # TEST: Test progress less than 100% returns no reward
    assert completed_lap_reward(reward, progress) == expected_reward

def test_completed_lap_reward_should_return_correct_reward3():
    reward = 0
    progress = 100
    expected_reward = (REWARD_LARGE * WEIGHTING_COMPLETED_LAP)

    # TEST: Test progress of 100% returns reward
    assert completed_lap_reward(reward, progress) == expected_reward

# Tests: reward_function
# ---------------------------------------
def test_reward_function_should_return_correct_reward1():
    params = {
        "progress": 20
    }
    # TEST: Expect min progress to have no reward
    expected_reward = REWARD_MIN

    assert reward_function(params) == expected_reward

def test_reward_function_should_return_correct_reward2():
    params = {
        "progress": 100
    }
    # TEST: Expect max progress to have reward
    expected_reward = REWARD_MIN + (REWARD_LARGE * WEIGHTING_COMPLETED_LAP)

    assert reward_function(params) == expected_reward
