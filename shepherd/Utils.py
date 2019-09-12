# pylint: disable=invalid-name
class SHEPHERD_HEADER():
    START_NEXT_STAGE = "start_next_stage"
        # START_NEXT_STAGE{}: starts the next stage

    RESET_CURRENT_STAGE = "reset_current_stage"
        # RESET_CURRENT_STAGE{}: resets the current stage

    RESET_MATCH = "reset_match"
        # RESET_MATCH{}: resets the current match

    GET_MATCH_INFO = "get_match_info"
        # GET_MATCH_INFO{match_number}: gets match info for given match number

    SETUP_MATCH = "setup_match"
        # SETUP_MATCH{b1name, b1#, b2name, b2#, g1name, g1#, g2name, g2#, match#}:
        # sets up the match given the corresponding info about the teams and match number
        # also has {g1_custom_ip, g2_custom_ip, b1_custom_ip, b2_custom_ip}

    GET_CONNECTION_STATUS = "get_connection_status"
        # GET_CONNECTION_STATUS{}: requested from the Staff UI to check robot
        # connection statuses

    GET_SCORES = "get_scores"
        # GET_SCORES{}: gets scores of the match

    SCORE_ADJUST = "score_adjust"
        # SCORE_ADJUST{blue_score, gold_score}: adjusts the current scores to the input scores

    STAGE_TIMER_END = "stage_timer_end"
        # STAGE_TIMER_END{}: ends the stage's timer

    ROBOT_OFF = "robot_off"
        # ROBOT_OFF{team_number}: takes in team number and disables their robot

    END_EXTENDED_TELEOP = "end_extended_teleop"
        # END_EXTENDED_TELEOP{}: ends the extended teloperated period

    LAUNCH_BUTTON_TRIGGERED = "launch_button_triggered"
        # LAUNCH_BUTTON_TRIGGERED{alliance, button}: takes in an alliance color and button number
        # and activates the corresponding launch button timer

    CODE_RETRIEVAL = "code_retrieval"
        # CODE_RETRIEVAL{alliance, result}: retrieves code (from sensors.py)

    CODE_APPLICATION = "code_application"
        # CODE_APPLICATION{alliance, result}: applies code (from sensors.py)

    APPLY_PERKS = "apply_perks"
        # APPLY_PERKS{alliance, perk_1, perk_2, perk_3}: applies the chosen perks
        # to the given alliance

    MASTER_ROBOT = "master_robot"

    FINAL_SCORE = "final_score"
    ASSIGN_TEAMS = "assign_teams"
        # ASSIGN_TEAMS{g1num, g2num, b1num, b2num}
    TEAM_RETRIEVAL = "team_retrieval"
        # TEAM_RETRIEVAL{}
    TRIGGER_OVERDRIVE = "trigger_overdrive"
        #TRIGGER_OVERDRIVE{size}

    ROBOT_CONNECTION_STATUS = "robot_connection_status"
        #ROBOT_CONNECTION_STATUS{team_number, connection[True/False]}

    REQUEST_CONNECTIONS = "request_connections"
        #REQUEST_CONNECTIONS{}

# pylint: disable=invalid-name
class SENSORS_HEADER():
    FAILED_POWERUP = "failed_powerup"

# pylint: disable=invalid-name
class DAWN_HEADER():
    CODES = "codes"
    DECODE = "decode"
    SPECIFIC_ROBOT_STATE = "srt"
    MASTER = "master"
    IP_ADDRESS = "ip_address"
    ROBOT_STATE = "rs"
    HEARTBEAT = "heartbeat"
    RESET = "reset"
    #TODO this^

class RUNTIME_HEADER():
    SPECIFIC_ROBOT_STATE = "specific_robot_state"
        # SPECIFIC_ROBOT_STATE{team_number, autonomous, enabled}
        # robot ip is 192.168.128.teamnumber
    DECODE = "decode"
        # DECODE{team_number, seed}

# pylint: disable=invalid-name
class UI_HEADER():
    TEAMS_INFO = "teams_info"
    SCORES = "scores"
    CONNECTIONS = "connections"
    #CONNECTIONS{g_1_connection[True/False], g_2_connection[True/False],
    # b_1_connection[True/False], b_2_connection[True/False]}

# pylint: disable=invalid-name
class SCOREBOARD_HEADER():
    SCORE = "score"
    TEAMS = "teams"
    STAGE = "stage"
    STAGE_TIMER_START = "stage_timer_start"
    RESET_TIMERS = "reset_timers"
    ALL_INFO = "all_info"

    LAUNCH_BUTTON_TIMER_START = "launch_button_timer_start"
        # LAUNCH_BUTTON_TIMER_START{alliance, button}
    PERKS_SELECTED = "perks_selected"
        # PERKS_SELECTED{alliance, perk_1, perk_2, perk_3}
    APPLIED_EFFECT = "applied_effect"
        # APPLIED_EFFECT{alliance, effect}
    OVERDRIVE_START = "overdrive_start"
        # OVERDRIVE_START{}

class TABLET_HEADER():
    TEAMS = "teams"
    #{b1num, b2num, g1num, g2num}
    CODE = "code"
    #{alliance, code}
    COLLECT_PERKS = "collect_perks"
    #{}
    COLLECT_CODES = "collect_codes"
    #{}
    RESET = "reset"
    #{}

# pylint: disable=invalid-name
class CONSTANTS():
    PERK_SELECTION_TIME = 30 # actually supposed to be 30
    AUTO_TIME = 30 # 30
    TELEOP_TIME = 180 # 180
    OVERDRIVE_TIME = 30
    SPREADSHEET_ID = "1vurNOrlIIeCHEtK5aJVDfHrRM1AC2qWvIbtWqUgnmLk"
    CSV_FILE_NAME = "Sheets/fc2019.csv"
    TAFFY_TIME = 15
    TWIST_CHANCE = .3 #a value 0<x<1
    COOLDOWN = 30
    STUDENT_DECODE_TIME = 1
    CRATE_SIZES = ["fun", "full", "king"]

# pylint: disable=invalid-name
class ALLIANCE_COLOR():
    GOLD = "gold"
    BLUE = "blue"

# pylint: disable=invalid-name
class LCM_TARGETS():
    SHEPHERD = "lcm_target_shepherd"
    SCOREBOARD = "lcm_target_scoreboard"
    SENSORS = "lcm_target_sensors"
    UI = "lcm_target_ui"
    DAWN = "lcm_target_dawn"
    RUNTIME = "lcm_target_runtime"
    TABLET = "tablet"

# pylint: disable=invalid-name
class TIMER_TYPES():
    MATCH = {"TYPE":"match", "NEEDS_FUNCTION": True,
             "FUNCTION":SHEPHERD_HEADER.STAGE_TIMER_END}
    EXTENDED_TELEOP = {"TYPE":"extended_teleop", "NEEDS_FUNCTION": True,
                       "FUNCTION":SHEPHERD_HEADER.END_EXTENDED_TELEOP}
    OVERDRIVE_DELAY = {"TYPE":"overdrive_delay", "NEEDS_FUNCTION": True,
                       "FUNCTION":SHEPHERD_HEADER.TRIGGER_OVERDRIVE}
    STUDENT_DECODE = {"TYPE":"student_decode", "NEEDS_FUNCTION": True,
                      "FUNCTION":SHEPHERD_HEADER.CODE_RETRIEVAL}
    LAUNCH_BUTTON = {"TYPE":"extended_teleop", "NEEDS_FUNCTION": False}

# pylint: disable=invalid-name
class STATE():
    SETUP = "setup"
    PERK_SELCTION = "perk_selection"
    AUTO_WAIT = "auto_wait"
    AUTO = "auto"
    WAIT = "wait"
    TELEOP = "teleop"
    END = "end"

class EFFECTS():
    TWIST = "twist"
    SPOILED_CANDY = "spoiled_candy"

class PERKS():
    EMPTY = "empty"
    BUBBLEGUM = "bubblegum"
    DIET = "diet"
    SWEET_SPOT = "sweet_spot"
    TAFFY = "taffy"
    CHOCOLATE_COVERED_ESPRESSO_BEANS = "chocolate_covered_espresso_beans"
    MINTY_FRESH_START = "minty_fresh_start"
    RASPBERRY_COTTON_CANDY = "raspberry_cotton_candy"
    ARTIFICIAL_SWEETENER = "artificial"
    JAWBREAKER = "jawbreaker"
    SOUR_GUMMY_WORMS = "sour_gummy_worms"
    # To be continued TODO
