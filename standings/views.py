from debate.models import Team, TeamScore, Speaker, SpeakerScore, Round
from motions.models import Motion
from django.views.decorators.cache import cache_page
from django.conf import settings
from django.contrib.auth.decorators import login_required

from utils import *

def get_speaker_standings(rounds, round, results_override=False, only_novices=False, for_replies=False):
    last_substantive_position = round.tournament.LAST_SUBSTANTIVE_POSITION
    reply_position = round.tournament.REPLY_POSITION
    total_prelim_rounds = Round.objects.filter(stage=Round.STAGE_PRELIMINARY, tournament=round.tournament).count()
    missable_debates = round.tournament.config.get('standings_missed_debates')
    minimum_debates_needed = total_prelim_rounds - missable_debates

    if for_replies:
        speaker_scores = SpeakerScore.objects.select_related(
            'speaker','ballot_submission', 'debate_team__debate__round'
            ).filter(ballot_submission__confirmed=True, position=reply_position)
    else:
        speaker_scores = SpeakerScore.objects.select_related(
            'speaker','ballot_submission', 'debate_team__debate__round'
            ).filter(ballot_submission__confirmed=True, position__lte=last_substantive_position)

    if only_novices is True:
        speakers = list(Speaker.objects.filter(team__tournament=round.tournament, novice=True).select_related(
            'team', 'team__institution', 'team__tournament'))
    else:
        speakers = list(Speaker.objects.filter(team__tournament=round.tournament).select_related(
            'team', 'team__institution', 'team__tournament'))

    def get_scores(speaker, this_speakers_scores):
        speaker_scores = [None] * len(rounds)
        for r in rounds:
            finding_score = next((x for x in this_speakers_scores if x.debate_team.debate.round == r), None)
            if finding_score:
                speaker_scores[r.seq - 1] = finding_score.score

        return speaker_scores

    for speaker in speakers:
        this_speakers_scores = [score for score in speaker_scores if score.speaker == speaker]
        speaker.scores = get_scores(speaker, this_speakers_scores)
        speaker.results_in = speaker.scores[-1] is not None or round.stage != Round.STAGE_PRELIMINARY or results_override

        if round.seq < total_prelim_rounds or len(filter(None, speaker.scores)) >= minimum_debates_needed:
            speaker.total = sum(filter(None, speaker.scores))
            try:
                speaker.average = sum(filter(None, speaker.scores)) / len(filter(None, speaker.scores))
            except ZeroDivisionError:
                speaker.average = None
        else:
            speaker.total = None
            speaker.average = None

        if for_replies:
            speaker.replies_given = len(filter(None, speaker.scores))

    if for_replies:
        speakers = [s for s in speakers if s.replies_given > 0]

    prev_total = None
    current_rank = 0

    if for_replies or round.tournament.config.get('standings_method') is False:
        method = False
        speakers.sort(key=lambda x: x.average, reverse=True)
    else:
        method = True
        speakers.sort(key=lambda x: x.total, reverse=True)

    for i, speaker in enumerate(speakers, start=1):
        if method:
            comparison = speaker.total
        else:
            comparison = speaker.average

        if comparison != prev_total:
            current_rank = i
            prev_total = comparison
        speaker.rank = current_rank

    return speakers

def get_round_result(team, team_scores, r):
    ts = next((x for x in team_scores if x.debate_team.team == team and x.debate_team.debate.round == r), None)
    try:
        ts.opposition = ts.debate_team.opposition.team # TODO: this slows down the page generation considerably
    except AttributeError:
        pass
    except Exception as e:
        print "Unexpected exception in view.teams.get_round_result"
        print e
    return ts

@admin_required
@round_view
def team_standings(request, round):
    teams = Team.objects.ranked_standings(round)
    rounds = round.tournament.prelim_rounds(until=round).order_by('seq')
    team_scores = list(TeamScore.objects.select_related('debate_team__team', 'debate_team__debate__round').filter(ballot_submission__confirmed=True))

    for team in teams:
        team.results_in = round.stage != Round.STAGE_PRELIMINARY or get_round_result(team, team_scores, round) is not None
        team.round_results = [get_round_result(team, team_scores, r) for r in rounds]
        team.wins = [ts.win for ts in team.round_results if ts].count(True)
        team.points = sum([ts.points for ts in team.round_results if ts])
        if round.tournament.config.get('show_avg_margin'):
            try:
                margins = []
                for ts in team.round_results:
                    if ts:
                        if ts.get_margin is not None:
                            margins.append(ts.get_margin)

                team.avg_margin = sum(margins) / float(len(margins))
            except ZeroDivisionError:
                team.avg_margin = None

    show_draw_strength = decide_show_draw_strength(round.tournament)

    return r2r(request, 'teams.html', dict(teams=teams, rounds=rounds,
        show_ballots=False, show_draw_strength=show_draw_strength))


@admin_required
@round_view
def division_standings(request, round):
    # TODO: this can largely be merged/abstracted with teams
    teams = Team.objects.divisions(round)

    rounds = round.tournament.prelim_rounds(until=round).order_by('seq')
    team_scores = list(TeamScore.objects.select_related('debate_team__team', 'debate_team__debate__round').filter(ballot_submission__confirmed=True))

    for team in teams:
        team.round_results = [get_round_result(team, team_scores, r) for r in rounds]
        team.wins = [ts.win for ts in team.round_results if ts].count(True)
        team.points = sum([ts.points for ts in team.round_results if ts])
        if round.tournament.config.get('show_avg_margin'):
            try:
                margins = []
                for ts in team.round_results:
                    if ts:
                        if ts.get_margin is not None:
                            margins.append(ts.get_margin)

                team.avg_margin = sum(margins) / float(len(margins))
            except ZeroDivisionError:
                team.avg_margin = None

    return r2r(request, 'divisions.html', dict(teams=teams))


@admin_required
@round_view
def speaker_standings(request, round):
    rounds = round.tournament.prelim_rounds(until=round).order_by('seq')
    speakers = get_speaker_standings(rounds, round)
    return r2r(request, 'speakers.html', dict(speakers=speakers,
                                        rounds=rounds))


@admin_required
@round_view
def novice_standings(request, round):
    rounds = round.tournament.prelim_rounds(until=round).order_by('seq')
    speakers = get_speaker_standings(rounds, round, only_novices=True)
    return r2r(request, "novices.html", dict(speakers=speakers,
                                        rounds=rounds))


@admin_required
@round_view
def reply_standings(request, round):
    rounds = round.tournament.prelim_rounds(until=round).order_by('seq')
    speakers = get_speaker_standings(rounds, round, for_replies=True)
    return r2r(request, 'replies.html', dict(speakers=speakers,
                                        rounds=rounds))

@admin_required
@round_view
def motion_standings(request, round):
    rounds = round.tournament.prelim_rounds(until=round).order_by('seq')
    motions = list()
    motions = Motion.objects.statistics(round=round)
    return r2r(request, 'motions.html', dict(motions=motions))


@cache_page(settings.TAB_PAGES_CACHE_TIMEOUT)
@public_optional_tournament_view('tab_released')
def public_speaker_tab(request, t):
    print "Generating public speaker tab"
    round = t.current_round
    rounds = t.prelim_rounds(until=round).order_by('seq')
    speakers = get_speaker_standings(rounds, round)
    return r2r(request, 'public_speaker_tab.html', dict(speakers=speakers,
            rounds=rounds, round=round))



@cache_page(settings.TAB_PAGES_CACHE_TIMEOUT)
@public_optional_tournament_view('tab_released')
def public_novices_tab(request, t):
    round = t.current_round
    rounds = round.tournament.prelim_rounds(until=round).order_by('seq')
    speakers = get_speaker_standings(rounds, round, only_novices=True)
    return r2r(request, 'public_novices_tab.html', dict(speakers=speakers,
            rounds=rounds, round=round))


@cache_page(settings.TAB_PAGES_CACHE_TIMEOUT)
@public_optional_tournament_view('tab_released')
def public_replies_tab(request, t):
    round = t.current_round
    rounds = t.prelim_rounds(until=round).order_by('seq')
    speakers = get_speaker_standings(rounds, round, for_replies=True)
    return r2r(request, 'public_reply_tab.html', dict(speakers=speakers,
            rounds=rounds, round=round))


@cache_page(settings.TAB_PAGES_CACHE_TIMEOUT)
@public_optional_tournament_view('tab_released')
def public_team_tab(request, t):
    print "Generating public team tab"
    round = t.current_round
    teams = Team.objects.ranked_standings(round)
    rounds = t.prelim_rounds(until=round).order_by('seq')
    team_scores = list(TeamScore.objects.select_related('debate_team__team', 'debate_team__debate__round').filter(ballot_submission__confirmed=True))

    for team in teams:
        team.results_in = True # always
        team.round_results = [get_round_result(team, r) for r in rounds]
        team.wins = [ts.win for ts in team.round_results if ts].count(True)
        team.points = sum([ts.points for ts in team.round_results if ts])
        if round.tournament.config.get('show_avg_margin'):
            try:
                margins = []
                for ts in team.round_results:
                    if ts:
                        if ts.get_margin is not None:
                            margins.append(ts.get_margin)

                team.avg_margin = sum(margins) / float(len(margins))
            except ZeroDivisionError:
                team.avg_margin = None

    show_ballots = round.tournament.config.get('ballots_released')
    show_draw_strength = decide_show_draw_strength(round.tournament)

    return r2r(request, 'public_team_tab.html', dict(teams=teams,
            rounds=rounds, round=round, show_ballots=show_ballots,
            show_draw_strength=show_draw_strength))


@cache_page(settings.TAB_PAGES_CACHE_TIMEOUT)
@public_optional_tournament_view('motion_tab_released')
def public_motions_tab(request, t):
    round = t.current_round
    rounds = t.prelim_rounds(until=round).order_by('seq')
    print rounds
    motions = list()
    motions = Motion.objects.statistics(round=round)
    return r2r(request, 'public_motions_tab.html', dict(motions=motions))

