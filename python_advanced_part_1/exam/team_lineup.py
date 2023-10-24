def team_lineup(*args):
    data = {}
    for player, country in args:
        if country not in data:
            data[country] = [player]
        else:
            data[country].append(player)

    # Sort the countries by the number of players (descending) and then by country name (ascending)
    sorted_data = sorted(data.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))

    res = ''
    for country, players in sorted_data:
        res += f'{country}:' + '\n'
        for p in players:
            res += f'  -{p}' + '\n'

    return res

print(team_lineup(
   ("Lionel Messi", "Argentina"),
   ("Neymar", "Brazil"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Harry Kane", "England"),
   ("Kylian Mbappe", "France"),
   ("Raheem Sterling", "England")))



