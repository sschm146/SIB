import random

from otree.api import *
import time
c = Currency

doc = """
Final Questionnaire
"""


class Constants(BaseConstants):
    name_in_url = 'Final_Questionnaire'
    players_per_group = None
    num_rounds = 8  # Short version with 8 imtes and 4 minutes
    solution = [4, 4, 7, 1, 6, 3, 2, 5]  # Short version with 8 items and 4 minutes
    IQ_time = 240
    use_timeout = True

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    identity = models.StringField()
    input_field = models.IntegerField(label="Welches Puzzlestück passt?", min=1)
    time_started = models.FloatField()
    time_needed = models.FloatField()
    sisi_in = models.IntegerField(
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
        label="")
    sisi_out = models.IntegerField(
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
        label="")
    Abitur = models.IntegerField(
        choices=[
            [8, "3,5-4,0"],
            [7, "3,0-3,4"],
            [6, "2,5-2,9"],
            [5, "2,0-2,4"],
            [4, "1,5-1,9"],
            [3, "1,0-1,5"],
            [2, "Weiß ich nicht mehr."],
            [1, "Ich habe kein Abitur."]],
        label="", )




# PAGES
class SiSi(Page):
    @staticmethod
    def vars_for_template(player: Player):
        if "SI" in player.session.config['name']:
            participant = player.participant
            player.identity = participant.identity
            return dict(
                SI=True,
                identity=player.identity,
                random=random.randint(0, 1)
            )
        else:
            return dict(
                SI=False
            )
    @staticmethod
    def js_vars(player: Player):
        return dict(
            SI="SI" in player.session.config['name']
        )
    @staticmethod
    def is_displayed(player):
        return player.round_number == 1

    form_model = 'player'
    form_fields = ["sisi_in", "sisi_out"]


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
        if player.round_number < 3:
            return 6
        else:
            return 8

    @staticmethod
    def get_timeout_seconds(player):
        import time
        if player.round_number == 1:
            player.time_started = time.time()
        if player.round_number > 0:
            participant = player.participant
            return participant.expiry - time.time()

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        first_round_player = player.in_round(1)
        if player.round_number == 1:
            player.time_needed = time.time() - player.time_started
        if player.round_number > 1:
            time_deduct = 0
            for i in list(range(1, player.round_number, 1)):
                prev_player = player.in_round(i)
                time_deduct += prev_player.time_needed
            player.time_needed = time.time() - first_round_player.time_started - time_deduct

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
        return player.round_number == 8

    form_model = 'player'
    form_fields = ["Abitur"]

page_sequence = [SiSi, IQ_Instructions, Task, Abitur]
