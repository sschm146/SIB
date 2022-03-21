from otree.api import *

c = Currency

doc = """
Introduction & Instructions
"""


class Constants(BaseConstants):
    name_in_url = 'Intro_all'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    treatment = models.StringField()



#FUNCTIONS
def creating_session(subsession: Subsession):
    import itertools
    if subsession.round_number == 1:
        treat = itertools.cycle(["Blue", "Yellow"])
        for player in subsession.get_players():
            #player.treatment = next(treat)
            participant = player.participant
            participant.treatment = next(treat)
            player.treatment = participant.treatment
            print(participant.treatment)



# PAGES
class Instructions_all(Page):
    pass


class Instructions_sender(Page):
    pass


class Instructions_receiver(Page):
    pass


page_sequence = [Instructions_all, Instructions_sender, Instructions_receiver]
