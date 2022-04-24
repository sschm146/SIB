from otree.api import *
import random


class Constants(BaseConstants):
    name_in_url = 'Each_Slider_in_separate_Page'
    players_per_group = None
    tasks = ['A', 'B', 'C']
    num_rounds = len(tasks)
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

# FUNCTIONS
def creating_session(subsession: Subsession):
    if subsession.round_number == 1:
        for p in subsession.get_players():
            round_numbers = list(range(1, Constants.num_rounds + 1))
            random.shuffle(round_numbers)
            p.participant.task_rounds = dict(zip(Constants.tasks, round_numbers))

# PAGES
class Question1(Page):
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return player.round_number == participant.task_rounds['A']

    form_model = 'player'
    form_fields = ['question1_a', 'question1_b']

class Question2(Page):
    @staticmethod
    def is_displayed(player: Player):
        participant = player.participant

        return player.round_number == participant.task_rounds['B']

    form_model = 'player'
    form_fields = ['question2_a', 'question2_b']

class Question3(Page):
    @staticmethod
    def is_displayed(player: Player):
         participant = player.participant

         return player.round_number == participant.task_rounds['C']

    form_model = 'player'
    form_fields = ['question3_a', 'question3_b']

page_sequence = [Question1, Question2, Question3]
