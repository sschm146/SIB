import random

from otree.api import *

c = Currency

doc = """
Payout
"""


class Constants(BaseConstants):
    name_in_url = 'Payout'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
   pass


# PAGES
class Payout(Page):
    @staticmethod
    def vars_for_template(player: Player):
        part_fee = player.session.config['participation_fee']
        participant = player.participant
        SIM_payoff = participant.SIM_payoff
        GuessingTask_payoff = participant.GuessingTask_payoff
        participant.payoff = participant.SIM_payoff + participant.GuessingTask_payoff
        total_payoff = participant.payoff_plus_participation_fee()
        return dict(
            part_fee=part_fee,
            SIM_payoff=SIM_payoff,
            GuessingTask_payoff=GuessingTask_payoff,
            total_payoff=total_payoff,
        )



page_sequence = [Payout]
