def calculate_kd(kills, deaths):
    if deaths == 0:
        if kills == 0:
            return 0.00
        else:
            return float('inf')
    return kills / deaths

while True:
    try:
        player_kills = int(input("Enter the number of kills: "))
        player_deaths = int(input("Enter the number of deaths: "))

        kd_ratio = calculate_kd(player_kills, player_deaths)
        if kd_ratio == float('inf'):
            print("Player KD: Infinity")
        else:
            print("Player KD: {:.2f}".format(kd_ratio))
        break

    except ValueError:
        print("Invalid input. Please enter integer values for kills and deaths.")
