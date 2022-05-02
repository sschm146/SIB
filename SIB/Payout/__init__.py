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
class Payout_calc(WaitPage):
    wait_for_all_groups = True
    after_all_players_arrive = 'payout_calc'

def payout_calc(subsession: Subsession):
    for p in subsession.get_players():
        participant = p.participant
        SIM_payoff = participant.SIM_payoff
        GuessingTask_payoff = participant.GuessingTask_payoff
        if participant.Role == 'receiver':
            Trust_payoff = participant.Trust_payoff
            participant.payoff = random.choice([SIM_payoff, GuessingTask_payoff, Trust_payoff]) + p.session.config[
            'participation_fee']
        if participant.Role == 'sender':
            participant.payoff = random.choice([SIM_payoff, GuessingTask_payoff]) + p.session.config[
                'participation_fee']
        p.payoff = participant.payoff

class Payout(Page):
    @staticmethod
    def vars_for_template(player: Player):
        participant = player.participant
        SIM_payoff = participant.SIM_payoff
        return dict(
            part_fee=player.session.config['participation_fee'],
            SIM_payoff=SIM_payoff,
            total_payoff=participant.payoff,
        )



page_sequence = [Payout_calc, Payout]
