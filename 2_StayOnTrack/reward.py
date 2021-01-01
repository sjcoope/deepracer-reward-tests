# Weightings
# -------------
WEIGHTING_ON_TRACK = 1.25

# Reward Levels
# -------------
REWARD_LARGE = 1.25
REWARD_MED = 1.0
REWARD_SMALL = 0.75
REWARD_MIN = 1e-3

def reward_function(params):
    # Input parameters
    on_track = params['all_wheels_on_track']

    # Execute rewards
    reward = REWARD_MIN
    reward = stay_on_track_reward(reward, on_track)

    return float(reward)

# Stay on Track Reward Function
# ------------------------------------
def stay_on_track_reward(reward, on_track):
    if(on_track):
        reward += (REWARD_LARGE * WEIGHTING_ON_TRACK)
    else:
        reward *= REWARD_SMALL

    return reward
