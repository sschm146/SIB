from otree.api import *


class Constants(BaseConstants):
    name_in_url = 'All_Sliders_in_one_Page'
    players_per_group = None
    num_rounds = 1
    endowment = 100

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    question1_a = models.IntegerField(
        min=0, max=Constants.endowment
    )

    question1_b = models.IntegerField(
        min=0, max=Constants.endowment
    )

    question2_a = models.IntegerField(
        min=0, max=Constants.endowment
    )

    question2_b = models.IntegerField(
        min=0, max=Constants.endowment
    )
    question3_a = models.IntegerField(
        min=0, max=Constants.endowment
    )

    question3_b = models.IntegerField(
        min=0, max=Constants.endowment
    )


# PAGES
class All_one(Page):
    form_model = 'player'
    form_fields = ['question1_a', 'question1_b', 'question2_a', 'question2_b', 'question3_a', 'question3_b']


page_sequence = [All_one]
