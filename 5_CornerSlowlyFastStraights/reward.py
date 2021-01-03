# Weightings
# -------------
WEIGHTING_CORNER_SLOW_FAST_STRAIGHTS = 1.25

# Reward Levels
# -------------
REWARD_LARGE = 1.25
REWARD_MED = 1.0
REWARD_SMALL = 0.75
REWARD_MIN = 1e-3

# Config
# -------
MAX_SPEED = 3
MIN_SPEED = 1
MIN_STEER = 0

def reward_function(params):
    # Input parameters
    speed = params['speed']
    steering_angle = params['steering_angle']

    # Execute rewards
    reward = REWARD_MIN
    reward = corner_slowly_fast_straights_reward(reward, steering_angle, speed)

    return float(reward)

# Cornering Slowly & Fast Straights Reward Function
# --------------------------------
def corner_slowly_fast_straights_reward(reward, steering_angle, speed):
    if(steering_angle == MIN_STEER):
        # Car is going straight or nearly straight - reward high speed
        if(speed == MAX_SPEED):
            reward += (REWARD_LARGE * WEIGHTING_CORNER_SLOW_FAST_STRAIGHTS)
        elif(speed < MAX_SPEED and speed > MIN_SPEED):
            reward += (REWARD_MED * WEIGHTING_CORNER_SLOW_FAST_STRAIGHTS)
        elif(speed == MIN_SPEED):
            reward += (REWARD_SMALL * WEIGHTING_CORNER_SLOW_FAST_STRAIGHTS)
    else:
        #Car is cornering - reward low speed
        if(speed == MAX_SPEED):
            reward += (REWARD_SMALL * WEIGHTING_CORNER_SLOW_FAST_STRAIGHTS)
        elif(speed < MAX_SPEED and speed > MIN_SPEED):
            reward += (REWARD_MED * WEIGHTING_CORNER_SLOW_FAST_STRAIGHTS)
        elif(speed == MIN_SPEED):
            reward += (REWARD_LARGE * WEIGHTING_CORNER_SLOW_FAST_STRAIGHTS)
    return reward
