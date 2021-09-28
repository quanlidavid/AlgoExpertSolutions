# Tournament Winner
# There's an algorithms tournament taking place in which teams of programmers compete against each other to solve algorithmic problems as fast as possible. Teams compete in a round robin, where each team faces off against all other teams. Only two teams compete against each other at a time, and for each competition, one team is designated the home team, while the other team is the away team. In each competition there's always one winner and one loser; there are no ties. A team receives 3 points if it wins and 0 points if it loses. The winner of the tournament is the team that receives the most amount of points.
#
# Given an array of pairs representing the teams that have competed against each other and an array containing the results of each competition, write a function that returns the winner of the tournament. The input arrays are named competitions and results, respectively. The competitions array has elements in the form of [homeTeam, awayTeam], where each team is a string of at most 30 characters representing the name of the team. The results array contains information about the winner of each corresponding competition in the competitions array. Specifically, results[i] denotes the winner of competitions[i], where a 1 in the results array means that the home team in the corresponding competition won and a 0 means that the away team won.
#
# It's guaranteed that exactly one team will win the tournament and that each team will compete against all other teams exactly once. It's also guaranteed that the tournament will always have at least two teams.
#
# Sample Input
# competitions = [
#   ["HTML", "C#"],
#   ["C#", "Python"],
#   ["Python", "HTML"],
# ]
# results = [0, 0, 1]
# Sample Output
# "Python"
# // C# beats HTML, Python Beats C#, and Python Beats HTML.
# // HTML - 0 points
# // C# -  3 points
# // Python -  6 points


def tournamentWinner(competitions, results):
    dic = {}
    for index in range(len(results)):
        if results[index] == 1:
            if competitions[index][0] in dic.keys():
                dic[competitions[index][0]] += 3
            else:
                dic[competitions[index][0]] = 3
            if competitions[index][1] not in dic.keys():
                dic[competitions[index][1]] = 0
        else:
            if competitions[index][1] in dic.keys():
                dic[competitions[index][1]] += 3
            else:
                dic[competitions[index][1]] = 3
            if competitions[index][0] not in dic.keys():
                dic[competitions[index][0]] = 0
    mostCourse = competitions[0][0]
    mostPoint = dic[competitions[0][0]]
    for k, v in dic.items():
        if int(v) > mostPoint:
            mostPoint = v
            mostCourse = k
    print(mostCourse)
    return mostCourse


# 遍历一遍结果, 把胜的名字加到key里并且加3分, 第一次出现就创建key, value
# O(n) time n是competitions的数量| O(k) space k是参加比赛的队伍的数量
def tournamentWinnerSecond(competitions, results):
    dic = {}
    bestPoint = 0
    winner = ""
    for index in range(len(results)):
        if results[index] == 1:
            if competitions[index][0] in dic.keys():
                dic[competitions[index][0]] += 3
                if dic[competitions[index][0]] > bestPoint:
                    bestPoint = dic[competitions[index][0]]
                    winner = competitions[index][0]
            else:
                dic[competitions[index][0]] = 3
                if dic[competitions[index][0]] > bestPoint:
                    bestPoint = dic[competitions[index][0]]
                    winner = competitions[index][0]
            if competitions[index][1] not in dic.keys():
                dic[competitions[index][1]] = 0
        else:
            if competitions[index][1] in dic.keys():
                dic[competitions[index][1]] += 3
                if dic[competitions[index][1]] > bestPoint:
                    bestPoint = dic[competitions[index][1]]
                    winner = competitions[index][1]
            else:
                dic[competitions[index][1]] = 3
                if dic[competitions[index][1]] > bestPoint:
                    bestPoint = dic[competitions[index][1]]
                    winner = competitions[index][1]
            if competitions[index][0] not in dic.keys():
                dic[competitions[index][0]] = 0

    print(winner)
    return winner


# 遍历一遍结果, 把胜的名字加到key里并且加3分, 第一次出现就创建key, value
# O(n) time n是competitions的数量| O(k) space k是参加比赛的队伍的数量
def updateWinnerTeamPoint(winnerTeam, point, dic):
    if winnerTeam not in dic:
        dic[winnerTeam] = 0
    dic[winnerTeam] += point


def tournamentWinnerThird(competitions, results):
    dic = {}
    winner = ""
    mostPoint = 0
    for index, competition in enumerate(competitions):
        winnerTeam = competition[0] if results[index] == 1 else competition[1]
        updateWinnerTeamPoint(winnerTeam, 3, dic)
        if dic[winnerTeam] > mostPoint:
            mostPoint = dic[winnerTeam]
            winner = winnerTeam
    print(winner)
    return winner


competitions = [
    ["HTML", "Java"],
    ["Java", "Python"],
    ["Python", "HTML"]
]
results = [0, 1, 1]

tournamentWinnerThird(competitions, results)
