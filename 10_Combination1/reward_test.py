from reward import *

# Tests: completed_lap_reward
# ---------------------------------------
def test_completed_lap_within_step_target_reward_should_return_correct_reward1():
    # Within target steps (threshold 1)

    reward = 1
    progress = 20
    steps = (TARGET_STEPS * 0.19)

    assert completed_lap_within_step_target_reward(reward, progress, steps) == (reward + (REWARD_LARGE * WEIGHTING_PROGRESS_TO_STEPS_REWARD))

def test_completed_lap_within_step_target_reward_should_return_correct_reward2():
    # Within threshold 2 of target steps

    reward = 1
    progress = 20
    steps = ((TARGET_STEPS / 100) * progress) * 1.09

    assert completed_lap_within_step_target_reward(reward, progress, steps) == (reward + (REWARD_MED * WEIGHTING_PROGRESS_TO_STEPS_REWARD))

def test_completed_lap_within_step_target_reward_should_return_correct_reward3():
    # Within threshold 3 of target steps

    reward = 1
    progress = 20
    steps = ((TARGET_STEPS / 100) * progress) * 1.19

    assert completed_lap_within_step_target_reward(reward, progress, steps) == (reward + (REWARD_SMALL * WEIGHTING_PROGRESS_TO_STEPS_REWARD))

def test_completed_lap_within_step_target_reward_should_return_correct_reward4():
    # Outside of thresholds

    reward = 1
    progress = 20
    steps = ((TARGET_STEPS / 100) * progress) * 1.25

    assert completed_lap_within_step_target_reward(reward, progress, steps) == reward

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
def test_reward_function_should_return_correct_reward1():
    params = {
        "progress": 20,
        "steps": (TARGET_STEPS * 0.19),
        "track_width": 76,
        "distance_from_center": 7.1,
        "steering_angle": 0,
        "speed": 3.5
    }

    # TEST: Expect threshold 1 to return max reward
    expected_reward = (REWARD_LARGE * WEIGHTING_DIST_FROM_CENTER)
    expected_reward += (REWARD_LARGE * WEIGHTING_STRAIGHT_LINE_SPEED_REWARD)
    expected_reward += (REWARD_MIN + (REWARD_LARGE * WEIGHTING_PROGRESS_TO_STEPS_REWARD))

    assert reward_function(params) == expected_reward


