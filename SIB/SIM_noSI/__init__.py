import random

from otree.api import *

c = Currency

doc = """
SIM_noSI
"""


class Constants(BaseConstants):
    name_in_url = 'SIM_noSI'
    players_per_group = None
    num_rounds = 1
    use_timeout = True
    guess_time = 120
    labelled_time = 240

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    artist1 = models.StringField(
        choices=['Paul Klee', 'Wassily Kandinsky'],
        widget=widgets.RadioSelectHorizontal,
        label="",
    )
    artist2 = models.StringField(
        choices=['Paul Klee', 'Wassily Kandinsky'],
        widget=widgets.RadioSelectHorizontal,
        label="",
    )
    artist3 = models.StringField(
        choices=['Paul Klee', 'Wassily Kandinsky'],
        widget=widgets.RadioSelectHorizontal,
        label="",
    )
    artist4 = models.StringField(
        choices=['Paul Klee', 'Wassily Kandinsky'],
        widget=widgets.RadioSelectHorizontal,
        label="",
    )
    artist_points = models.IntegerField(initial=0)

# PAGES
class Instructions(Page):
    pass


class MyWaitPage(WaitPage):
    wait_for_all_groups = True
    after_all_players_arrive = 'payout_calc'

# Function to determine which individual has won the SIM
# Winner is determined by amount of solved paintings (or at random if amount of solved paintings is equal)

def payout_calc(subsession: Subsession):
    players = subsession.get_players()
    for p in players:
        if p.artist1 == "Paul Klee":
            p.artist_points += 1
        if p.artist2 == "Wassily Kandinsky":
            p.artist_points += 1
        if p.artist3 == "Wassily Kandinsky":
            p.artist_points += 1
        if p.artist4 == "Wassily Kandinsky":
            p.artist_points += 1
    for p in players:
        participant = p.participant
        others = [g.artist_points for g in players if g != p]
        competitor = random.choice(others)
        if p.artist_points > competitor:
            p.payoff = subsession.session.config['SIM_payoff']
            participant.SIM_payoff = p.payoff
        if p.artist_points < competitor:
            p.payoff = 0
            participant.SIM_payoff = p.payoff
        if p.artist_points == competitor:
            p.payoff = random.choice([subsession.session.config['SIM_payoff'], 0])
            participant.SIM_payoff = p.payoff


class Paintings_labelled(Page):
    if Constants.use_timeout:
        timeout_seconds = Constants.labelled_time


class Paintings_guess(Page):
    if Constants.use_timeout:
        timeout_seconds = Constants.guess_time
    form_model = 'player'
    form_fields = ['artist1', 'artist2', 'artist3', 'artist4']


page_sequence = [Instructions, Paintings_labelled, Paintings_guess, MyWaitPage]
