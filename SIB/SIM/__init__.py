from otree.api import *

c = Currency

doc = """
SIM
"""


class Constants(BaseConstants):
    name_in_url = 'SIM'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

class Player(BasePlayer):
    choice1 = models.StringField(
        choices=[['Alpha1', 'Alpha1'], ['Beta1', 'Beta1']],
        widget=widgets.RadioSelect,
        label="Choose who you think draw this painting:",

    )
    choice2 = models.StringField(
        choices=[['Alpha2', 'Alpha2'], ['Beta2', 'Beta2']],
        widget=widgets.RadioSelect,
        label="Choose who you think draw this painting:",
    )


# PAGES
class Instructions(Page):
    pass


class Paintings_labelled(Page):
    form_model = 'player'


class Paintings_guess(Page):
    form_model = 'player'
    form_fields = ['choice1', 'choice2']


page_sequence = [Instructions, Paintings_labelled, Paintings_guess]
