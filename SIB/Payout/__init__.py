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
    all_clear = models.LongStringField(blank=True, label='')
    comments = models.LongStringField(blank=True, label='')
    payoff_urn = models.StringField()
    payoff_ball = models.IntegerField()



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
            payoff_urn = [SIM_payoff, GuessingTask_payoff, Trust_payoff]
            p.payoff_urn = str(payoff_urn)
            p.payoff_ball = random.choice([0, 1, 2])
            p.payoff = payoff_urn[p.payoff_ball] + p.session.config['participation_fee']
            participant.payoff = payoff_urn[p.payoff_ball]
        if participant.Role == 'sender' or participant.Role == 'prior_sender':
            payoff_urn = [SIM_payoff, GuessingTask_payoff]
            p.payoff_urn = str(payoff_urn)
            p.payoff_ball = random.choice([0, 1])
            p.payoff = payoff_urn[p.payoff_ball] + p.session.config['participation_fee']
            participant.payoff = payoff_urn[p.payoff_ball]



class Final_Q(Page):

    form_model = 'player'
    form_fields = ["all_clear", "comments"]

class Payout(Page):
    @staticmethod
    def vars_for_template(player: Player):
        participant = player.participant

        SIM_payoff = participant.SIM_payoff
        GuessingTask_payoff = participant.GuessingTask_payoff

        if participant.Role == 'sender' or participant.Role == 'prior_sender':
            return dict(
                part_fee=player.session.config['participation_fee'],
                SIM_payoff=SIM_payoff,
                GuessingTask_payoff=GuessingTask_payoff,
                total_payoff=player.payoff,
                payoff_ball=player.payoff_ball,
                role = participant.Role
            )
        if participant.Role == 'receiver':
            Trust_payoff = participant.Trust_payoff
            return dict(
                part_fee=player.session.config['participation_fee'],
                SIM_payoff=SIM_payoff,
                GuessingTask_payoff=GuessingTask_payoff,
                Trust_payoff=Trust_payoff,
                total_payoff=player.payoff,
                payoff_ball=player.payoff_ball,
                role=participant.Role
            )




page_sequence = [Payout_calc, Final_Q, Payout]
