# Weightings
# -------------
WEIGHTING_WITHIN_TRACK_BORDERS = 1.25
WEIGHTING_PROGRESS_TO_STEPS_REWARD = 1.75

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

    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    all_wheels_on_track = params['all_wheels_on_track']

    progress = params['progress']
    steps = params['steps']

    # Execute rewards
    reward = REWARD_MIN
    reward = always_within_track_borders_reward(reward, all_wheels_on_track, track_width, distance_from_center)
    reward = steps_to_progress_reward(reward, progress, steps)

    return float(reward)

# Always within track borders
# ------------------------------------
# Give a reward if no wheels go off of the track and the car is somewhere between the track borders
def always_within_track_borders_reward(reward, all_wheels_on_track, track_width, distance_from_center):

    if all_wheels_on_track and (0.5*track_width - distance_from_center) >= 0.05:
        reward += (REWARD_LARGE * WEIGHTING_WITHIN_TRACK_BORDERS)

    return reward

# Lap progress to steps completed reward
# -----------------------------
# Reward progress of the track against the amount of steps taken
def steps_to_progress_reward(reward, progress, steps):
    return reward + ((progress / steps) * WEIGHTING_PROGRESS_TO_STEPS_REWARD)
