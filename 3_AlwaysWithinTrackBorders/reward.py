# Weightings
# -------------
WEIGHTING_WITHIN_TRACK_BORDERS = 1.25

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
    all_wheels_on_track = params['all_wheels_on_track']


    # Execute rewards
    reward = REWARD_MIN
    reward = always_within_track_borders_reward(reward, all_wheels_on_track, track_width, distance_from_center)

    return float(reward)

# Always within track borders
# ------------------------------------
# Give a reward if no wheels go off of the track and the car is somewhere between the track borders
def always_within_track_borders_reward(reward, all_wheels_on_track, track_width, distance_from_center):

    if all_wheels_on_track and (0.5*track_width - distance_from_center) >= 0.05:
        reward += (REWARD_LARGE * WEIGHTING_WITHIN_TRACK_BORDERS)
    else:
        reward *= REWARD_SMALL

    return reward
