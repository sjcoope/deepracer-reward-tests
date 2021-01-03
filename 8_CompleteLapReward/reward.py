# Weightings
# -------------
WEIGHTING_COMPLETED_LAP = 1.25

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
    reward = completed_lap_reward(reward, progress)

    return float(reward)

# Completed Lap Reward Function
# -----------------------------
# Reward only 100% completion of a lap (as opposed to continual progress reward)
def completed_lap_reward(reward, progress):
    if(progress == 100):
        reward += (REWARD_LARGE * WEIGHTING_COMPLETED_LAP)

    return reward
