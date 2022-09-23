from os import environ


# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']


SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=7, doc="",
    SIM_payoff=16, #Payoff for winning the Klee/Kandinsky contest in SIM
    SIM_labelled_time=240, #Time for Paintings_labelled
    SIM_guess_time=120, #Time for Paintings_guess
    GT_sender_payoff=13, #Payoff for precision of sent signal (QSR)
    GT_receiver_payoff=13, #Payoff for precision of submitted estimate (QSR)
    GT_guess_time=240, #Time to submit a guess on the Signals page
    Trust_in_Senders_payoff=14, #Payoff for receivers based on precision TiS
    Confidence_payoff=2, #Fixed Payoff for receivers based on Confidence_3_new
    True_state=[135, 343, 675, 328, 684, 267, 544, 452, 511, 303],
    Signals=[[211, 382, 703, 374, 610, 220, 515, 411, 474, 342], # Signals for Sender A
             [187, 432, 713, 405, 589, 188, 468, 367, 492, 292], # Signals for Sender B
             [236, 357, 771, 433, 593, 198, 454, 389, 519, 301], # Signals for Sender C
             [59, 249, 583, 258, 765, 372, 650, 557, 503, 308], # Signals for Sender D
             [169, 351, 683, 360, 651, 254, 548, 437, 495, 312], # Signals for Sender E
             [151, 361, 697, 378, 665, 268, 548, 441, 471, 306], # Signals for Sender F
             [207, 388, 728, 408, 602, 191, 478, 388, 524, 311]], # Signals for Sender 1 (CB-treatment)
    signal_order_1=[0,1,8,2,3,5,4,9,6,7],
    signal_order_2=[6,7,9,4,2,4,5,1,8,0],
    signal_order_3=[3,2,5,9,4,1,8,7,0,6],
    timeout_guess=240,
    entry_warning_border=10,
    QSR_cutoff=5000
)



SESSION_CONFIGS = [
    dict(
        name="control",
        display_name="SIB_control",
        num_demo_participants=10,
        app_sequence=["Intro_noSI_all", "SIM_noSI", "GuessingTask_noSI", "BigFive", "Trust", "Final_Questionnaire", "MU", "Payout"],
        prior_sender=False,
    ),
    dict(
        name="SI",
        display_name="SIB_SI",
        num_demo_participants=10,
        app_sequence=["Intro_SI_all", "SIM_SI", "GuessingTask_SI", "BigFive", "Trust", "Final_Questionnaire", "MU",  "Payout"],
        prior_sender=False,
    ),
    dict(
        name="control_confirmation",
        display_name="SIB_control_CB",
        num_demo_participants=10,
        app_sequence=["Intro_noSI_all", "SIM_noSI", "GuessingTask_noSI_CB", "BigFive", "Trust",  "Final_Questionnaire", "MU", "Payout"],
        prior_sender=True,
    ),
    dict(
        name="SI_confirmation",
        display_name="SIB_SI_CB",
        num_demo_participants=10,
        app_sequence=["Intro_SI_all", "SIM_SI", "GuessingTask_SI_CB", "BigFive", "Trust", "Final_Questionnaire", "MU", "Payout"],
        prior_sender=True,
    ),
    dict(
        name="control_selection",
        display_name="SIB_control_SB",
        num_demo_participants=10,
        app_sequence=["Intro_noSI_all", "SIM_noSI", "GuessingTask_noSI_SB", "BigFive", "Trust", "Final_Questionnaire", "MU", "Payout"],
        prior_sender=False,
    ),
    dict(
        name="SI_selection",
        display_name="SIB_SI_SB",
        num_demo_participants=10,
        app_sequence=["Intro_SI_all", "SIM_SI", "GuessingTask_SI_SB", "BigFive", "Trust", "Final_Questionnaire", "MU", "Payout"],
        prior_sender=False,
    ),
    dict(
        name="control_correlation",
        display_name="SIB_control_CN",
        num_demo_participants=10,
        app_sequence=["Intro_noSI_all", "SIM_noSI", "GuessingTask_noSI_CN", "BigFive", "Trust", "Final_Questionnaire", "MU", "Payout"],
        prior_sender=False,
    ),
    dict(
        name="SI_correlation",
        display_name="SIB_SI_CN",
        num_demo_participants=10,
        app_sequence=["Intro_SI_all", "SIM_SI", "GuessingTask_SI_CN", "BigFive", "Trust", "Final_Questionnaire", "MU", "Payout"],
        prior_sender=False,
    ),
]

PARTICIPANT_FIELDS = ["Role", "identity", "SIM_payoff", "GuessingTask_payoff", "Trust_payoff", "signals_all_rounds",
                      "estimates_all_rounds", "task_rounds", "expiry"]
SESSION_FIELDS = []

ROOMS = [
    dict(
        name="lab",
        display_name="Lab Experiment",
        participant_label_file='_rooms/lab.txt',
    ),
]
# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = "de"

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = "EUR"
USE_POINTS = False

ADMIN_USERNAME = "admin"
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get("OTREE_ADMIN_PASSWORD")

DEMO_PAGE_INTRO_HTML = """ """
#sk
SECRET_KEY = "2646253538807"
