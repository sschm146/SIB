from otree.api import *

c = Currency

doc = """
Final Questionnaire
"""


class Constants(BaseConstants):
    name_in_url = 'Final_Questionnaire_noSI'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    all_clear = models.LongStringField(blank=True, label= '')
    comments = models.LongStringField(blank=True,label= '')



# PAGES
class Final_noSI(Page):
    pass

    form_model = 'player'
    form_fields = ["all_clear", "comments"]


page_sequence = [Final_noSI]
