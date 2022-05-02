from os import environ


# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']


SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=4.00, doc="",
    SIM_payoff=2, #Payoff for winning the Klee/Kandinsky contest in SIM
    GT_sender_payoff=0.5, #Payoff for precision of sent signal (QSR)
    GT_receiver_payoff=0.5, #Payoff for precision of submitted estimate (QSR)
    Trust_payoff_1=0.5, #Payoff for receivers based on TiS
    Trust_payoff_2=0.5, #Payoff for receivers based on Confidence_2
)


SESSION_CONFIGS = [
    dict(
        name="control",
        display_name="SIB_control",
        num_demo_participants=10,
        app_sequence=["Intro_noSI_all", "SIM_noSI", "GuessingTask_noSI", "Trust_noSI", "MU", "Final_Questionnaire_noSI", "Payout"],
        prior_sender=False,
    ),
    dict(
        name="SI",
        display_name="SIB_SI",
        num_demo_participants=10,
        app_sequence=["Intro_SI_all", "SIM_SI", "GuessingTask_SI", "Trust_SI", "MU", "Final_Questionnaire_SI", "Payout"],
        prior_sender=False,
    ),
    dict(
        name="control_confirmation",
        display_name="SIB_control_CB",
        num_demo_participants=10,
        app_sequence=["Intro_noSI_all", "SIM_noSI", "GuessingTask_noSI_CB", "Trust_noSI", "MU", "Final_Questionnaire_noSI", "Payout"],
        prior_sender=True,
    ),
    dict(
        name="SI_confirmation",
        display_name="SIB_SI_CB",
        num_demo_participants=10,
        app_sequence=["Intro_SI_all", "SIM_SI", "GuessingTask_SI_CB", "Trust_SI", "MU", "Final_Questionnaire_SI", "Payout"],
        prior_sender=True,
    ),
    dict(
        name="control_selection",
        display_name="SIB_control_SB",
        num_demo_participants=10,
        app_sequence=["Intro_noSI_all", "SIM_noSI", "GuessingTask_noSI_SB", "Trust_noSI", "MU", "Final_Questionnaire_noSI", "Payout"],
        prior_sender=False,
    ),
    dict(
        name="SI_selection",
        display_name="SIB_SI_SB",
        num_demo_participants=10,
        app_sequence=["Intro_SI_all", "SIM_SI", "GuessingTask_SI_SB", "Trust_SI", "MU", "Final_Questionnaire_SI",  "Payout"],
        prior_sender=False,
    ),
    dict(
        name="control_correlation",
        display_name="SIB_control_CN",
        num_demo_participants=10,
        app_sequence=["Intro_noSI_all", "SIM_noSI", "GuessingTask_noSI_CN", "Trust_noSI", "MU", "Final_Questionnaire_noSI","Payout"],
        prior_sender=False,
    ),
    dict(
        name="SI_correlation",
        display_name="SIB_SI_CN",
        num_demo_participants=10,
        app_sequence=["Intro_SI_all", "SIM_SI", "GuessingTask_SI_CN", "Trust_SI", "MU", "Final_Questionnaire_SI", "Payout"],
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
                      "estimates_all_rounds", "task_rounds"]
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = "en"

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = "EUR"
USE_POINTS = False

ADMIN_USERNAME = "admin"
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get("OTREE_ADMIN_PASSWORD")

DEMO_PAGE_INTRO_HTML = """ """
#sk
SECRET_KEY = "2646253538807"
