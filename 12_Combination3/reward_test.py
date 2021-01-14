from reward import *

# Tests: always_within_track_borders_reward
# ---------------------------------------
def test_always_within_track_borders_reward_should_return_correct_reward1():
    reward = 1
    all_wheels_on_track = True
    track_width = 76
    distance_from_center = 20
    expected_reward = (reward + (REWARD_LARGE * WEIGHTING_WITHIN_TRACK_BORDERS))

    # Reward should decrease because all wheels aren't on the track.
    assert always_within_track_borders_reward(reward, all_wheels_on_track, track_width, distance_from_center) == expected_reward

def test_always_within_track_borders_reward_should_return_correct_reward2():
    reward = 1
    all_wheels_on_track = True
    track_width = 76
    distance_from_center = 37
    expected_reward = (reward + (REWARD_LARGE * WEIGHTING_WITHIN_TRACK_BORDERS))

    # Reward should decrease because all wheels aren't on the track.
    assert always_within_track_borders_reward(reward, all_wheels_on_track, track_width, distance_from_center) == expected_reward

def test_always_within_track_borders_reward_should_return_correct_reward3():
    reward = 1
    all_wheels_on_track = False
    track_width = 76
    distance_from_center = 40
    expected_reward = (reward * REWARD_SMALL)

    # Reward shouldn't change because all wheels aren't on the track.
    assert always_within_track_borders_reward(reward, all_wheels_on_track, track_width, distance_from_center) == expected_reward

# Tests: steps_to_progress_reward
# --------------------------------
def test_steps_to_progress_reward_should_return_correct_reward1():
    reward = 1
    steps = 5
    progress = 1.5
    expected_reward = (reward + ((progress / steps) * WEIGHTING_PROGRESS_TO_STEPS_REWARD))

    assert steps_to_progress_reward(reward, progress, steps) == expected_reward

# Tests: steps_to_progress_reward
# --------------------------------
def test_steps_to_progress_reward_should_return_correct_reward2():
    reward = 1
    steps = 144
    progress = 100
    expected_reward = (reward + ((progress / steps) * WEIGHTING_PROGRESS_TO_STEPS_REWARD))

    assert steps_to_progress_reward(reward, progress, steps) == expected_reward

# Tests: reward_function
# ---------------------------------------
def test_reward_function_should_return_correct_reward1():
    steps = 25
    progress = 15.67

    params = {
        "all_wheels_on_track": True,
        "track_width": 76,
        "distance_from_center": 37,
        "steps": steps,
        "progress": progress
    }

    expected_reward = REWARD_MIN
    expected_reward += (REWARD_LARGE * WEIGHTING_WITHIN_TRACK_BORDERS)
    expected_reward += ((progress / steps) * WEIGHTING_PROGRESS_TO_STEPS_REWARD)

    assert reward_function(params) == expected_reward
