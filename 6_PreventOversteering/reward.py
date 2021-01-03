# Weightings
# -------------
WEIGHTING_PREVENT_OVERSTEER = 1

# Reward Levels
# -------------
REWARD_LARGE = 1.25
REWARD_MED = 1.0
REWARD_SMALL = 0.75
REWARD_MIN = 1e-3

# Config
# -------
MAX_ABS_STEERING_THRESHOLD = 15
MIN_ABS_STEERING_THRESHOLD = -15

def reward_function(params):
    # Input parameters
    steering_angle = params['steering_angle']

    # Execute rewards
    reward = REWARD_MIN
    reward = prevent_oversteering_reward(reward, steering_angle)

    return float(reward)

# Prevent Oversteering Reward Function
# ------------------------------------
# Reduce the current reward if the car is oversteering - should encourage better cornering (i.e. taking corners wider)
def prevent_oversteering_reward(reward, steering_angle):

    # Reduce the current reward if the agent is steering too much.
    if steering_angle < MIN_ABS_STEERING_THRESHOLD or steering_angle > MAX_ABS_STEERING_THRESHOLD:
        reward *= (REWARD_SMALL * WEIGHTING_PREVENT_OVERSTEER)

    return reward
