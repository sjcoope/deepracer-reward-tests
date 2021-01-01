# Weightings
# -------------
WEIGHTING_DIST_FROM_CENTER = 1.25

# Reward Levels
# -------------
REWARD_LARGE = 1.25
REWARD_MED = 1.0
REWARD_SMALL = 0.75
REWARD_MIN = 1e-3

def reward_function(params):
    # Input parameters
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']

    # Execute rewards
    reward = REWARD_MIN
    reward = distance_from_center_reward(reward, track_width, distance_from_center)

    return float(reward)

# Distance From Center Reward Function
# ------------------------------------
# Make reward close for all zones to allow for better cornering
def distance_from_center_reward(reward, track_width, distance_from_center):
    # Calculate 3 markers that are at varying distances away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width

    # Give higher reward if the car is closer to center line and vice versa
    if distance_from_center <= marker_1:
        reward += (REWARD_LARGE * WEIGHTING_DIST_FROM_CENTER)
    elif distance_from_center <= marker_2:
        reward += (REWARD_MED * WEIGHTING_DIST_FROM_CENTER)
    elif distance_from_center <= marker_3:
        reward += (REWARD_SMALL * WEIGHTING_DIST_FROM_CENTER)
    else:
        reward += REWARD_MIN  # likely crashed/ close to off track

    return reward
