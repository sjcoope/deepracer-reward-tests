# Weightings
# -------------
WEIGHTING_DIST_FROM_CENTER = 1.25
WEIGHTING_PROGRESS_TO_STEPS_REWARD = 1.5

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
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']

    # Execute rewards
    reward = REWARD_MIN
    reward = distance_from_center_reward(reward, track_width, distance_from_center)
    reward = completed_lap_within_step_target_reward(reward, progress, steps)

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
