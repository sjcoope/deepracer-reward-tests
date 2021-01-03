# Weightings
# -------------
WEIGHTING_OVERALL_PROGRESS = 1.25

# Reward Levels
# -------------
REWARD_LARGE = 1.25
REWARD_MED = 1.0
REWARD_SMALL = 0.75
REWARD_MIN = 1e-3

def reward_function(params):
    # Input parameters
    progress = params['progress']

    # Execute rewards
    reward = REWARD_MIN
    reward = progress_reward(reward, progress)

    return float(reward)

# Progress Reward Per Quarter Completed
# -------------------------------------
def progress_reward(reward, progress):
    if(progress <= 25):
        reward += (REWARD_MIN * WEIGHTING_OVERALL_PROGRESS)
    elif(progress <= 50):
        reward += (REWARD_SMALL * WEIGHTING_OVERALL_PROGRESS)
    elif(progress <= 75):
        reward += (REWARD_MED * WEIGHTING_OVERALL_PROGRESS)
    else:
        reward += (REWARD_LARGE * WEIGHTING_OVERALL_PROGRESS)

    return reward
