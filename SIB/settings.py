from os import environ


# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']


SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=5.00, doc="",
    SIM_payoff=2, #Payoff for winning the Klee/Kandinsky contest in SIM
    GT_sender_payoff=0.5, #Payoff for precision of sent signal (QSR)
    GT_receiver_payoff=0.5, #Payoff for precision of submitted estimate (QSR)
    Trust_payoff_1=0.5, #Payoff for receivers based on TiS
    Trust_payoff_2=0.5, #Payoff for receivers based on Confidence_2
    True_state=[531, 233, 4495, 6713, 6635, 7114, 1823, 2892, 200, 2353],
    Signals=[[538, 244, 4506, 6706, 6644, 7102, 1813, 2883, 203, 2362],
             [539, 241, 4505, 6704, 6643, 7106, 1817, 2884, 204, 2343],
             [532, 234, 4503, 6713, 6641, 7107, 1818, 2889, 188, 2342],
             [534, 235, 4490, 6712, 6639, 7126, 1821, 2890, 200, 2346],
             [524, 229, 4504, 6724, 6625, 7120, 1831, 2802, 198, 2348],
             [520, 221, 4498, 6722, 6631, 7108, 1833, 2898, 196, 2349],
             [541, 247, 4492, 6703, 6626, 7104, 1815, 2899, 193, 2351]],
    signal_order_1=[0, 1, 2, 3, 4, 9, 8, 7, 6, 5],
    signal_order_2=[0, 9, 1, 8, 2, 7, 3, 6, 4, 5],
    signal_order_3=[1, 3, 5, 7, 9, 0, 2, 4, 6, 8]
)

SESSION_CONFIGS = [
    dict(
        name="control",
        display_name="SIB_control",
        num_demo_participants=10,
        app_sequence=["Intro_noSI_all", "SIM_noSI", "GuessingTask_noSI", "BigFive", "Trust_noSI", "Final_Questionnaire_noSI", "MU", "Payout"],
        prior_sender=False,
    ),
    dict(
        name="SI",
        display_name="SIB_SI",
        num_demo_participants=10,
        app_sequence=["Intro_SI_all", "SIM_SI", "GuessingTask_SI", "BigFive", "Trust_SI", "Final_Questionnaire_SI", "MU",  "Payout"],
        prior_sender=False,
    ),
    dict(
        name="control_confirmation",
        display_name="SIB_control_CB",
        num_demo_participants=10,
        app_sequence=["Intro_noSI_all", "SIM_noSI", "GuessingTask_noSI_CB", "BigFive","Trust_noSI",  "Final_Questionnaire_noSI", "MU", "Payout"],
        prior_sender=True,
    ),
    dict(
        name="SI_confirmation",
        display_name="SIB_SI_CB",
        num_demo_participants=10,
        app_sequence=["Intro_SI_all", "SIM_SI", "GuessingTask_SI_CB", "BigFive","Trust_SI", "Final_Questionnaire_SI", "MU", "Payout"],
        prior_sender=True,
    ),
    dict(
        name="control_selection",
        display_name="SIB_control_SB",
        num_demo_participants=10,
        app_sequence=["Intro_noSI_all", "SIM_noSI", "GuessingTask_noSI_SB", "BigFive","Trust_noSI", "Final_Questionnaire_noSI", "MU", "Payout"],
        prior_sender=False,
    ),
    dict(
        name="SI_selection",
        display_name="SIB_SI_SB",
        num_demo_participants=10,
        app_sequence=["Intro_SI_all", "SIM_SI", "GuessingTask_SI_SB","BigFive", "Trust_SI", "Final_Questionnaire_SI", "MU", "Payout"],
        prior_sender=False,
    ),
    dict(
        name="control_correlation",
        display_name="SIB_control_CN",
        num_demo_participants=10,
        app_sequence=["Intro_noSI_all", "SIM_noSI", "GuessingTask_noSI_CN","BigFive", "Trust_noSI", "Final_Questionnaire_noSI", "MU", "Payout"],
        prior_sender=False,
    ),
    dict(
        name="SI_correlation",
        display_name="SIB_SI_CN",
        num_demo_participants=10,
        app_sequence=["Intro_SI_all", "SIM_SI", "GuessingTask_SI_CN", "BigFive","Trust_SI", "Final_Questionnaire_SI", "MU", "Payout"],
        prior_sender=False,
    ),
dict(
        name="MU_Test",
        display_name="MU_Test",
        num_demo_participants=2,
        app_sequence=["MU"],
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
