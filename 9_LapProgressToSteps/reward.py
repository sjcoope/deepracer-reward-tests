# Weightings
# -------------
WEIGHTING_PROGRESS_TO_STEPS_REWARD = 1.25

# Reward Levels
# -------------
REWARD_LARGE = 1.25
REWARD_MED = 1.0
REWARD_SMALL = 0.75
REWARD_MIN = 1e-3

# Config
# -------
TARGET_STEPS = 160

def reward_function(params):
    # Input parameters
    progress = params['progress']
    steps = params['steps']

    # Execute rewards
    reward = REWARD_MIN
    reward = completed_lap_within_step_target_reward(reward, progress, steps)

    return float(reward)

# Lap progress to steps completed reward
# -----------------------------
# Reward progress of the track against the expected amount of steps
def completed_lap_within_step_target_reward(reward, progress, steps):

    expected_steps = (TARGET_STEPS / 100) * progress

    threshold_1 = expected_steps
    threshold_2 = (expected_steps * 1.1)
    threshold_3 = (expected_steps * 1.2)

    if(steps <= threshold_1):
        reward += (REWARD_LARGE * WEIGHTING_PROGRESS_TO_STEPS_REWARD)
    elif(steps <= threshold_2):
        reward += (REWARD_MED * WEIGHTING_PROGRESS_TO_STEPS_REWARD)
    elif(steps <= threshold_3):
        reward += (REWARD_SMALL * WEIGHTING_PROGRESS_TO_STEPS_REWARD)

    return reward
