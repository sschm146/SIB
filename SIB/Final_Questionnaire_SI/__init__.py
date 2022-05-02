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
    identity = models.StringField()
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


def creating_session(subsession: Subsession):
    players = subsession.get_players()
    for p in players:
        participant = p.participant
        p.identity = participant.identity
# PAGES
class Final_SI(Page):

    @staticmethod
    def is_displayed(player):
        return player.identity != "neutral"

    @staticmethod
    def vars_for_template(player: Player):

        return dict(
            group_name=player.identity,
        )

    form_model = 'player'
    form_fields = ["sisi", "all_clear", "comments"]


page_sequence = [Final_SI]
