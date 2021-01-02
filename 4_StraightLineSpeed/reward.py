# Weightings
# -------------
WEIGHTING_STRAIGHT_LINE_SPEED_REWARD = 1.25

# Reward Levels
# -------------
REWARD_LARGE = 1.25
REWARD_MED = 1.0
REWARD_SMALL = 0.75
REWARD_MIN = 1e-3

def reward_function(params):
    # Input parameters
    speed = params['speed']
    steering_angle = params['steering_angle']

    # Execute rewards
    reward = REWARD_MIN
    reward = straight_line_speed_reward(reward, steering_angle, speed)

    return float(reward)

# Straight Line Speed Reward Function
# -----------------------------------
def straight_line_speed_reward(reward, steering_angle, speed):
    if(steering_angle == 0 and speed >= 2):
        reward += (REWARD_LARGE * WEIGHTING_STRAIGHT_LINE_SPEED_REWARD)

    return reward
