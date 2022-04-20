from otree.api import *

c = Currency

doc = """
Final Questionnaire
"""


class Constants(BaseConstants):
    name_in_url = 'Final_Questionnaire_SI'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    all_clear = models.LongStringField(blank=True, label= '')
    comments = models.LongStringField(blank=True, label= '')
    sisi= models.IntegerField(
        choices=[
            [1, ''],
            [2, ''],
            [3, ''],
            [4, ''],
            [5, ''],
            [6, ''],
            [7, ''],

        ],
        widget=widgets.RadioSelectHorizontal,
        label="",)



# PAGES
class Final_SI(Page):

    @staticmethod
    def vars_for_template(player: Player):
        participant = player.participant
        identity = participant.identity
        return dict(
            group_name=identity,
        )

    form_model = 'player'
    form_fields = ["sisi", "all_clear", "comments"]


page_sequence = [Final_SI]
