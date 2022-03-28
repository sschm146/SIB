from os import environ


# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']


SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=4.00, doc=""
)


SESSION_CONFIGS = [
    dict(
        name="control",
        display_name="SIB_control",
        num_demo_participants=10,
        app_sequence=["Intro_noSI_all", "SIM_noSI", "GuessingTask_noSI", "Payout"],
    ),
    dict(
        name="SI",
        display_name="SIB_SI",
        num_demo_participants=10,
        app_sequence=["Intro_SI_all", "SIM_SI", "GuessingTask_SI", "Payout"],
    ),
    dict(
        name="control_confirmation",
        display_name="SIB_control_CB",
        num_demo_participants=10,
        app_sequence=["Intro_noSI_all", "SIM_noSI", "GuessingTask_noSI_CB", "Payout"],
    ),
]

PARTICIPANT_FIELDS = ["identity", "SIM_payoff", "GuessingTask_payoff"]
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

SECRET_KEY = "2646253538807"
