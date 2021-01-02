from reward import *

# Tests: straight_line_speed_reward
# ---------------------------------------
def test_straight_line_speed_reward_should_return_correct_reward1():
    reward = 0
    steering_angle = 0
    speed = 3.5
    expected_reward = (REWARD_LARGE * WEIGHTING_STRAIGHT_LINE_SPEED_REWARD)

    # Reward should decrease because all wheels aren't on the track.
    assert straight_line_speed_reward(reward, steering_angle, speed) == expected_reward

def test_straight_line_speed_reward_should_return_correct_reward2():
    reward = 0
    steering_angle = 15
    speed = 3.5

    # Reward should decrease because all wheels aren't on the track.
    assert straight_line_speed_reward(reward, steering_angle, speed) == reward

# Tests: reward_function
# ---------------------------------------
def test_reward_function_should_return_correct_reward():
    reward = 0
    params = {
        "steering_angle": -15,
        "speed": 3.0
    }
    expected_reward = 1e-3

    assert reward_function(params) == expected_reward
