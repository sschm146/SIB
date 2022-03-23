from otree.api import *

c = Currency

doc = """
Welcome & Instructions
"""


class Constants(BaseConstants):
    name_in_url = 'Intro_SI_all'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    identity = models.StringField()


#FUNCTIONS
def creating_session(subsession: Subsession):
    import itertools
    identity = itertools.cycle(["Blue", "Yellow"])
    for player in subsession.get_players():
        participant = player.participant
        participant.identity = next(identity)
        player.identity = participant.identity


# PAGES
class Instructions_all(Page):
    pass


page_sequence = [Instructions_all]
