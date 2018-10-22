# Complete the function below.
def differentTeams(skills):
    if not skills or len(skills) < 5 :
        return 0
    teamDict = {'p':0,'c':0,'m':0,'b':0,'z':0}
    for i in range(len(skills)):
        teamDict[skills[i]] += 1
    return min(teamDict.values())

# print(differentTeams('pcmpcmbbbzz')) -> 2

