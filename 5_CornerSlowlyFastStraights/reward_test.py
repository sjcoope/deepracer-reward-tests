from reward import *

# Tests: corner_slowly_fast_straights_reward
# ---------------------------------------
def test_corner_slowly_fast_straights_reward_should_return_correct_reward1():
    reward = 0
    steering_angle = 0
    speed = MAX_SPEED
    expected_reward = (REWARD_LARGE * WEIGHTING_CORNER_SLOW_FAST_STRAIGHTS)

    # TEST: Check max speed on straight returns max reward.
    assert corner_slowly_fast_straights_reward(reward, steering_angle, speed) == expected_reward

def test_corner_slowly_fast_straights_reward_should_return_correct_reward2():
    reward = 0
    steering_angle = 0
    speed = MAX_SPEED - 1
    expected_reward = (REWARD_MED * WEIGHTING_CORNER_SLOW_FAST_STRAIGHTS)

    # TEST: Check med speed on straight returns med reward.
    assert corner_slowly_fast_straights_reward(reward, steering_angle, speed) == expected_reward

def test_corner_slowly_fast_straights_reward_should_return_correct_reward3():
    reward = 0
    steering_angle = 0
    speed = MIN_SPEED
    expected_reward = (REWARD_SMALL * WEIGHTING_CORNER_SLOW_FAST_STRAIGHTS)

    # TEST: Check slow speed on straight returns small reward.
    assert corner_slowly_fast_straights_reward(reward, steering_angle, speed) == expected_reward

def test_corner_slowly_fast_straights_reward_should_return_correct_reward4():
    reward = 0
    steering_angle = -15
    speed = MAX_SPEED
    expected_reward = (REWARD_SMALL * WEIGHTING_CORNER_SLOW_FAST_STRAIGHTS)

    # TEST: Check max speed on turn returns small reward.
    assert corner_slowly_fast_straights_reward(reward, steering_angle, speed) == expected_reward

def test_corner_slowly_fast_straights_reward_should_return_correct_reward5():
    reward = 0
    steering_angle = -15
    speed = MAX_SPEED - 1
    expected_reward = (REWARD_MED * WEIGHTING_CORNER_SLOW_FAST_STRAIGHTS)

    # TEST: Check med speed on turn returns med reward.
    assert corner_slowly_fast_straights_reward(reward, steering_angle, speed) == expected_reward

def test_corner_slowly_fast_straights_reward_should_return_correct_reward6():
    reward = 0
    steering_angle = -15
    speed = MIN_SPEED
    expected_reward = (REWARD_LARGE * WEIGHTING_CORNER_SLOW_FAST_STRAIGHTS)

    # TEST: Check slow speed on turn returns max reward.
    assert corner_slowly_fast_straights_reward(reward, steering_angle, speed) == expected_reward

# Tests: reward_function
# ---------------------------------------
def test_reward_function_should_return_correct_reward1():
    params = {
        "steering_angle": 0,
        "speed": 3.0
    }
    # TEST: Expect max speed on straight returns max reward
    expected_reward = REWARD_MIN + (REWARD_LARGE * WEIGHTING_CORNER_SLOW_FAST_STRAIGHTS)

    assert reward_function(params) == expected_reward

def test_reward_function_should_return_correct_reward2():
    params = {
        "steering_angle": -30,
        "speed": 3.0
    }
    # TEST: Expect max speed on corner returns small reward
    expected_reward = REWARD_MIN + (REWARD_SMALL * WEIGHTING_CORNER_SLOW_FAST_STRAIGHTS)

    assert reward_function(params) == expected_reward
