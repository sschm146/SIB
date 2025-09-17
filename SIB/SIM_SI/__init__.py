from otree.api import *
import random
c = Currency

doc = """
SIM_SI
"""


class Constants(BaseConstants):
    name_in_url = 'SIM_SI'
    players_per_group = None
    num_rounds = 1
    use_timeout = True
    guess_time = 120
    labelled_time = 240


class Subsession(BaseSubsession):
    tie_breaker = models.StringField()


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    identity = models.StringField()
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

def creating_session(subsession: Subsession):
    players = subsession.get_players()
    for p in players:  # Senders (in rounds 1-10) see a randomly drawn signal from a normal distribution with given mean and sd
        participant = p.participant
        p.identity = participant.identity
# PAGES
class Instructions(Page):

    @staticmethod
    def vars_for_template(player: Player):
        participant = player.participant
        identity = participant.identity
        return dict(
            identity=identity,
            SIM_payoff=player.session.config['SIM_payoff'],
            SIM_labelled_time=int(player.session.config['SIM_labelled_time'] / 60)
        )


class MyWaitPage(WaitPage):
    wait_for_all_groups = True
    after_all_players_arrive = 'payout_calc'

    # Function to determine which individual has won the SIM
    # Winner is determined by amount of solved paintings (or at random if amount of solved paintings is equal)

def payout_calc(subsession: Subsession):
    subsession.tie_breaker = random.choice(["Gelb", "Blau"])
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
    correct_yellow = sum([a.artist_points for a in players if a.identity == 'Gelb'])
    correct_blue = sum([a.artist_points for a in players if a.identity == 'Blau'])
    for p in players:
        participant = p.participant
        if p.identity != "neutral":
            if correct_yellow > correct_blue and p.identity == "Gelb":
                participant.SIM_payoff = subsession.session.config['SIM_payoff']
            elif correct_yellow < correct_blue and p.identity == "Blau":
                participant.SIM_payoff = subsession.session.config['SIM_payoff']
            elif correct_yellow == correct_blue and p.identity == subsession.tie_breaker:
                participant.SIM_payoff = subsession.session.config['SIM_payoff']
            else:
                participant.SIM_payoff = 0
        if p.identity == "neutral":
            others_points = [g.artist_points for g in players if g != p]
            others_ids = [g.id_in_group for g in players if g != p]
            temp = random.choice(others_ids) - 1
            competitor = others_points[temp]
            if p.artist_points > competitor:
                participant.SIM_payoff = subsession.session.config['SIM_payoff']
            elif p.artist_points == competitor:
                participant.SIM_payoff = random.choice([subsession.session.config['SIM_payoff'], 0])
            else:
                participant.SIM_payoff = 0



class Paintings_labelled(Page):

    @staticmethod
    def get_timeout_seconds(player: Player):
        return player.session.config['SIM_labelled_time']

    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            SIM_payoff=player.session.config['SIM_payoff'],
            SIM_labelled_time=int(player.session.config['SIM_labelled_time'] / 60)
        )


class Paintings_guess(Page):

    @staticmethod
    def get_timeout_seconds(player: Player):
        return player.session.config['SIM_guess_time']

    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            SIM_guess_time=int(player.session.config['SIM_guess_time'] / 60),
            SIM_payoff=player.session.config['SIM_payoff']
        )
    form_model = 'player'
    form_fields = ['artist1', 'artist2', 'artist3', 'artist4']


page_sequence = [Instructions, Paintings_labelled, Paintings_guess, MyWaitPage]
