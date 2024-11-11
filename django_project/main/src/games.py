from ..models import *

def linkSelfGame(request, id):
    self_game = Self_game.objects.get(id=id)
    baskets = linkGameSelfSpor.objects.filter(UserId=request.user, Game=id)
    if not baskets.exists():
        GL = linkGameSelfSpor(UserId=request.user, Game=Self_game)
        GL.save()
        pr = Profile.objects.get(user=request.user)
        if pr.balance - Self_game.stavka < 0:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        pr.balance -= Self_game.stavka
        pr.wins_coins -= Self_game.stavka
        pr.save()
        Self_game.People += 1
        if Self_game.win_ans != 0:
            basketPeople = linkGame.objects.filter(Game=Self_game)
            Winner = random.choice(list(basketPeople)).UserId
            Loto(Game=Self_game, Winner=Winner).save()
            gameA = Self_game
            gameA.People = 0
            gameA.save()
            Self_game.post = False
            WinnerPr = Profile.objects.get(user=Winner)
            WinnerPr.wins_coins += (Self_game.MaxPeople * Self_game.stavka)
            WinnerPr.wins_games += 1
            WinnerPr.balance += (Self_game.MaxPeople * Self_game.stavka)
            WinnerPr.save()
        GL.save()
        Self_game.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def linkGameAdd(request, id):
    game = Game.objects.get(id=id)
    baskets = linkGame.objects.filter(UserId=request.user, Game=id)
    if not baskets.exists():
        GL = linkGame(UserId=request.user, Game=game)
        GL.save()
        pr = Profile.objects.get(user=request.user)
        if pr.balance - game.stavka < 0:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        pr.balance -= game.stavka
        pr.wins_coins -= game.stavka
        pr.save()
        game.People += 1
        if game.People == game.MaxPeople:
            basketPeople = linkGame.objects.filter(Game=game)
            Winner = random.choice(list(basketPeople)).UserId
            Loto(Game=game, Winner=Winner).save()
            gameA = game
            gameA.People = 0
            gameA.save()
            game.is_published = False
            WinnerPr = Profile.objects.get(user=Winner)
            WinnerPr.wins_coins += (game.MaxPeople * game.stavka)
            WinnerPr.wins_games += 1
            WinnerPr.balance += (game.MaxPeople * game.stavka)
            WinnerPr.save()
        GL.save()
        game.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
