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
    Questionnaire_payoff=4,
    True_state=[369, 860, 624, 492, 528, 257, 137, 649, 486, 491, 162],
    Signals=[[327, 861, 607, 456, 568, 345, 230, 680, 453, 592, 99], # Signals for Sender A
             [293, 813, 572, 473, 617, 267, 168, 743, 570, 451, 216], # Signals for Sender B
             [371, 782, 551, 398, 533, 317, 133, 664, 425, 427, 173], # Signals for Sender C
             [489, 973, 745, 596, 431, 148, 40, 552, 481, 491, 163], # Signals for Sender D
             [337, 891, 657, 530, 519, 236, 128, 630, 542, 424, 93], # Signals for Sender E
             [401, 843, 617, 488, 497, 224, 126, 634, 419, 562, 225], # Signals for Sender F
             [325, 820, 581, 446, 576, 314, 178, 701, 484, 489, 163]], # Signals for Sender 1 (CB-treatment)
    signal_order_1=[0, 1, 8, 2, 3, 10, 5, 4, 9, 6, 7],
    signal_order_2=[6, 7, 9, 3, 2, 10, 4, 5, 8, 1, 0],
    signal_order_3=[3, 2, 10, 5, 4, 9, 1, 7, 8, 0, 6],
    timeout_guess=240,
    entry_warning_border=10,
    QSR_cutoff=5000
)


SESSION_CONFIGS = [
    dict(
        name="version_131224",
        display_name="version_131224",
        num_demo_participants=1,
        app_sequence=["Intro_noSI_all"],
        prior_sender=False
    ),
    dict(
        name="testing",
        display_name="testing",
        num_demo_participants=10,
        app_sequence=["Intro_noSI_all"],
        prior_sender=False
    ),
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

PARTICIPANT_FIELDS = ["Role", "identity", "SIM_payoff", "GuessingTask_payoff", "Trust_payoff", "chosen_payoff", "total_payoff", "signals_all_rounds",
                      "estimates_all_rounds", "task_rounds", "expiry"]
SESSION_FIELDS = []

ROOMS = [
    dict(
        name="lab",
        display_name="lab",
        participant_label_file='_rooms/lab.txt',
    ),
dict(
        name="CLER",
        display_name="CLER",
        participant_label_file='_rooms/lab_cler.txt',
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
