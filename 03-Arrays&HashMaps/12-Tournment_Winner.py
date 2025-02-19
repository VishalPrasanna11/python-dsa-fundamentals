# Write a function that returns the winner of a competition based on the results of the competitions.

HOME_TEAM_WON = 1

def tournamentWinner(competitions, results):
    # Write your code here.
    currentBestTeam = ""
    scores = {currentBestTeam:0}

    for idx, comp in enumerate(competitions):
        result = results[idx]
        homeTeam,awayTeam = comp

        winningTeam  = homeTeam if result == HOME_TEAM_WON else awayTeam

        updateScores(winningTeam,3, scores)

        if scores[winningTeam] > scores[currentBestTeam]:
            currentBestTeam = winningTeam

    return currentBestTeam

def updateScores(team,points,scores):
    if team not in scores:
        scores[team]=0

    scores[team]+= points


