from reward import *

# Tests: prevent_oversteering_reward
# ---------------------------------------
def test_progress_reward_should_return_correct_reward1():
    reward = 0
    progress = 20
    expected_reward = reward + (REWARD_MIN * WEIGHTING_OVERALL_PROGRESS)

    # TEST: Test progress less than 25% gives min reward with weighting
    assert progress_reward(reward, progress) == expected_reward

def test_progress_reward_should_return_correct_reward2():
    reward = 0
    progress = 35
    expected_reward = reward + (REWARD_SMALL * WEIGHTING_OVERALL_PROGRESS)

    # TEST: Test progress less than 50% gives small reward with weighting
    assert progress_reward(reward, progress) == expected_reward

def test_progress_reward_should_return_correct_reward3():
    reward = 0
    progress = 51
    expected_reward = reward + (REWARD_MED * WEIGHTING_OVERALL_PROGRESS)

    # TEST: Test progress less than 75% gives medium reward with weighting
    assert progress_reward(reward, progress) == expected_reward

def test_progress_reward_should_return_correct_reward4():
    reward = 0
    progress = 90
    expected_reward = reward + (REWARD_LARGE * WEIGHTING_OVERALL_PROGRESS)

    # TEST: Test progress less than 100% gives large reward with weighting
    assert progress_reward(reward, progress) == expected_reward

# Tests: reward_function
# ---------------------------------------
def test_reward_function_should_return_correct_reward1():
    params = {
        "progress": 20
    }
    # TEST: Expect min progress to have min reward
    expected_reward = REWARD_MIN + (REWARD_MIN * WEIGHTING_OVERALL_PROGRESS)

    assert reward_function(params) == expected_reward

def test_reward_function_should_return_correct_reward2():
    params = {
        "progress": 100
    }
    # TEST: Expect max progress to have max reward
    expected_reward = REWARD_MIN + (REWARD_LARGE * WEIGHTING_OVERALL_PROGRESS)

    assert reward_function(params) == expected_reward
