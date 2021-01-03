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


# Tests: reward_function
# ---------------------------------------
def test_reward_function_should_return_correct_reward1():
    params = {
        "progress": 20,
        "steps": (TARGET_STEPS * 0.19)
    }
    # TEST: Expect threshold 1 to return max reward
    expected_reward = (REWARD_MIN + (REWARD_LARGE * WEIGHTING_PROGRESS_TO_STEPS_REWARD))

    assert reward_function(params) == expected_reward

def test_reward_function_should_return_correct_reward2():
    params = {
        "progress": 20,
        "steps": ((TARGET_STEPS / 100) * 20) * 1.25
    }
    # TEST: Expect outside of thresholds to return on reward
    expected_reward = REWARD_MIN

    assert reward_function(params) == expected_reward


