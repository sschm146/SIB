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
    use_timeout = False
    guess_time = 600
    labelled_time = 300
    artist_payoff = 3

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    artist1 = models.StringField(
        choices=['Klee', 'Kandinsky'],
        widget=widgets.RadioSelectHorizontal,
        label="",
    )
    artist2 = models.StringField(
        choices=['Klee', 'Kandinsky'],
        widget=widgets.RadioSelectHorizontal,
        label="",
    )
    artist_points = models.IntegerField(initial=0)

# PAGES
class Instructions(Page):
    pass


class MyWaitPage(WaitPage):
    wait_for_all_groups = True
    after_all_players_arrive = 'artist_winner'

# Function to determine which individual has won the SIM
# Winner is determined by amount of solved paintings (or at random if amount of solved paintings is equal)
def artist_winner(subsession: Subsession):
    players = subsession.get_players()
    winner_list = []
    for p in players:
        if p.artist1 == "Kandinsky":
            p.artist_points += 1
        if p.artist2 == "Klee":
            p.artist_points += 1
    for p in players:
        others = [g.artist_points for g in players if g != p]
        if p.artist_points > max(others):
            p.payoff += Constants.artist_payoff
        if p.artist_points == max(others):
            winner_list.append(p.id_in_group)
    if winner_list:
        winner = random.choice(winner_list)
        for p in players:
            if p.id_in_group == winner:
                p.payoff += Constants.artist_payoff


class Paintings_labelled(Page):
    if Constants.use_timeout:
        timeout_seconds = Constants.labelled_time


class Paintings_guess(Page):
    if Constants.use_timeout:
        timeout_seconds = Constants.guess_time
    form_model = 'player'
    form_fields = ['artist1', 'artist2']


page_sequence = [Instructions, Paintings_labelled, Paintings_guess, MyWaitPage]
