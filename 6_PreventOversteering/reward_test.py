from reward import *

# Tests: prevent_oversteering_reward
# ---------------------------------------
def test_prevent_oversteering_reward_should_return_correct_reward1():
    reward = 1
    steering_angle = 30
    expected_reward = reward * (REWARD_SMALL * WEIGHTING_PREVENT_OVERSTEER)

    # TEST: Test reward reduced for max steer.
    assert prevent_oversteering_reward(reward, steering_angle) == expected_reward

# Tests: prevent_oversteering_reward
# ---------------------------------------
def test_prevent_oversteering_reward_should_return_correct_reward2():
    reward = 1
    steering_angle = -15
    expected_reward = reward

    # TEST: Test reward not reduced for medium steer
    assert prevent_oversteering_reward(reward, steering_angle) == expected_reward

# Tests: prevent_oversteering_reward
# ---------------------------------------
def test_prevent_oversteering_reward_should_return_correct_reward3():
    reward = 1
    steering_angle = 0
    expected_reward = reward

    # TEST: Test reward not reduced for no steer
    assert prevent_oversteering_reward(reward, steering_angle) == expected_reward

# Tests: reward_function
# ---------------------------------------
def test_reward_function_should_return_correct_reward1():
    params = {
        "steering_angle": -30
    }
    # TEST: Expect max steer to reduce reward
    expected_reward = REWARD_MIN * (REWARD_SMALL * WEIGHTING_PREVENT_OVERSTEER)

    assert reward_function(params) == expected_reward

def test_reward_function_should_return_correct_reward2():
    params = {
        "steering_angle": 0
    }
    # TEST: Expect no steer to maintain reward
    expected_reward = REWARD_MIN

    assert reward_function(params) == expected_reward
