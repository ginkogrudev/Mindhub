def calculate_winners(snapshot, penguins): 
    # your code here
    races = snapshot.split()
    swiming_distances = []

    for race in races:
        swiming_distances.append(penguins_distances(race))
    total =  sorted(list(zip(swiming_distances,penguins)))

    return f"GOLD: {total[0][1]}, SILVER: {total[1][1]}, BRONZE: {total[2][1]}"

def penguins_distances(race):
    p_index = 0
    wave_cnt = 0
    dashes_cnt = 0
    for r in range(len(race)):
        if race[r] == "P" or race[r] == "p":
            p_index = race[r]
        if p_index != 0 and race[r] == "~":
            wave_cnt += 1
        if p_index != 0 and race[r] == "-":
            dashes_cnt += 1

    return dashes_cnt+wave_cnt*2