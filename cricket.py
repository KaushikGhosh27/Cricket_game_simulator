import random

batsmen_list = ["Sehwag","Sachin","Ganguly","Gambhir","Yuvi","MSD","Jadeja","Kapil","Amarnath","Khan"]
bowler_list = ["Warne","Steyn","Boult","Lee","Johnson","Tikolo","Starc","Cummins","Henry","Ferguson","Marshall"]


individual_score = 0
individual_wickets = 0

total_score = 0
total_wickets = 0
boundaries = 0

b_runs = {}
b_wickets = {}
balls_played = {}

batsman_index = 0
batsman = batsmen_list[batsman_index]

bowler_index = 0
bowler = bowler_list[bowler_index]

balls_faced  =0

for overs in range(0,10):
    print("---------------------------------------------------------------------------")
    print("Over:{}".format(overs))
    start = batsman
    for balls in range(1,7):
        ball = random.randint(1,7)
        if ball == 5:
            if (batsman_index) <= 9:
                print("{}:OUT  Over:{}.{}".format(batsman,overs,balls))
                b_runs[batsman] = individual_score
                balls_played[batsman] = balls_faced
                individual_score = 0
                balls_faced = 0
                batsman_index += 1
                if batsman_index <= 9:
                    batsman = batsmen_list[batsman_index]
                individual_wickets += 1
                total_wickets += 1


        elif ball == 4 or ball == 6:
            boundaries +=1
            individual_score += ball
            total_score += ball
            balls_faced += 1
        else:
            individual_score += ball
            total_score += ball
            balls_faced += 1



    if bowler_index < 9:
        b_wickets[bowler] = individual_wickets
        individual_wickets = 0
        bowler_index += 1
        bowler = bowler_list[bowler_index]



        if (batsman_index == 10):
            print("\nBatsman [ Start of Over: {},End of Over: {} ] Bowler:{}\n".format(start, batsman, bowler))
            print("Score: {}/{}    Boundaries: {}".format(total_score, total_wickets, boundaries))
            print("----------------------------------------------------------------------------")
            print("\nScore: {} All OUT   Boundaries: {}\n".format(total_score, boundaries))
            print("----------------------------------------------------------------------------")
            Name = "\u0332".join("Name ")
            Runs = "\u0332".join("Runs ")
            print("{}    {}".format(Name,Runs))
            for name,runs in b_runs.items():
                print("{:<10s} {}".format(name,runs))
            #print("\nName    Wickets")
            Name = "\u0332".join("Name ")
            Wickets = "\u0332".join("Wickets ")
            print("{}    {}".format(Name,Wickets))
            for name,wickets in b_wickets.items():
                print("{:<10s}  {}".format(name,wickets))
            break
        else:
            print("\nBatsman [ Start of Over: {},End of Over: {} ] Bowler:{}\n".format(start, batsman, bowler))
            print("Score: {}/{}    Boundaries: {}".format(total_score, total_wickets, boundaries))
            continue
        break

    else:
        print("\nBatsman [ Start of Over: {},End of Over: {} ] Bowler:{}\n".format(start,batsman,bowler))
        print("Score: {}/{}    Boundaries: {}".format(total_score,total_wickets,boundaries))
        continue
    break

else:
    b_runs[batsman] = individual_score
    b_wickets[bowler]= individual_wickets
    print("----------------------------------------------------------------------------")
    print("\nEND OF INNINGS Score: {}/{}  Overs:10    Boundaries: {}\n".format(total_score, total_wickets, boundaries))
    #print("Name       Runs")
    Name = "\u0332".join("Name ")
    Runs = "\u0332".join("Runs ")
    print("{}    {}".format(Name, Runs))
    for name, runs in b_runs.items():
        print("{:<10s} {}".format(name, runs))
    #print("\nName    Wickets")
    Name = "\u0332".join("Name ")
    Wickets = "\u0332".join("Wickets ")
    print("{}    {}".format(Name, Wickets))
    for name, wickets in b_wickets.items():
        print("{:<10s}  {}".format(name, wickets))







