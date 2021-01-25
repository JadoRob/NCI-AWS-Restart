teams = [
    ['sadf', 'efs', 'sefk', 'kffsa'],
    ['geret', 'euioe', 'bbefk', 'kfhilfsa'],
    ['sasf', '1fs', 'seghk', 'jssfsa']
]


teamCounter = 1

def printTeam(team):
    for member in team:
        print(f'{member}')

for teamnum in range(3):
    print(f'Team #{teamCounter}')
    printTeam(teams(teamnum))
    teamCounter += 1