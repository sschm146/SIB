from otree.api import *

c = Currency

doc = """
Final Questionnaire
"""


class Constants(BaseConstants):
    name_in_url = 'Final_Questionnaire_noSI'
    players_per_group = None
    num_rounds = 10  # Short version with 10 imtes and 5 minutes
    solution = [5, 2, 4, 4, 7, 1, 6, 3, 2, 5]  # Short version with 10 items and 5 minutes
    IQ_time = 300
    use_timeout = True

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    all_clear = models.LongStringField(blank=True, label= '')
    comments = models.LongStringField(blank=True,label= '')
    input_field = models.IntegerField(label="Welches Puzzlestück passt?", min=1)
    win = models.IntegerField()
    time_spend = models.FloatField(initial=0)
    total_points = models.IntegerField()
    sisi = models.IntegerField(
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
        label="", )
    Abitur = models.IntegerField(
        choices=[
            [7, "3,5-4,0"],
            [6, "3,0-3,4"],
            [5, "2,5-2,9"],
            [4, "2,0-2,4"],
            [3, "1,5-1,9"],
            [2, "1,0-1,5"],
            [1, "Weiß ich nicht mehr."],
            [0, "Ich habe kein Abitur."]])




# PAGES
class SiSi_noSI(Page):

    @staticmethod
    def is_displayed(player):
        return player.round_number == 1

    form_model = 'player'
    form_fields = ["sisi"]

class Final_noSI(Page):

    @staticmethod
    def is_displayed(player):
        return player.round_number == 10

    form_model = 'player'
    form_fields = ["all_clear", "comments"]

class IQ_Instructions(Page):

    @staticmethod
    def is_displayed(player):
        return player.round_number == 1

    @staticmethod
    def before_next_page(player, timeout_happened):
        participant = player.participant
        import time
        participant.expiry = time.time() + Constants.IQ_time

class Task(Page):
    if Constants.use_timeout:
        timeout_seconds = Constants.IQ_time

    @staticmethod
    def input_field_max(player):
        if player.round_number < 5:
            return 6
        else:
            return 8

    @staticmethod
    def get_timeout_seconds(player):
        if player.round_number > 1:
            participant = player.participant
            import time
            return participant.expiry - time.time()

    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            round=player.round_number
        )

    form_model = 'player'
    form_fields = ['input_field']

class Abitur(Page):

    @staticmethod
    def is_displayed(player):
        return player.round_number == 10

    form_model = 'player'
    form_fields = ["Abitur"]

page_sequence = [SiSi_noSI, IQ_Instructions, Task, Final_noSI, Abitur]
