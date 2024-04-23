planstability = 0
rewardscale = 0
correctcount = 0
basereward = 0
esccount = 0

print("AP Statistics 2023: Katherina Pinto & Michelle Ordonez\n")
print("Let's Pull Off a Heist!!!\n\n\n")

print("After three years of working at a gas station, Silas Giordanni has had enough.")
print("His gas station has been robbed more than 50 times during his time as a night-shift worker,")
print("and 23-year-old college dropout Silas is ready to move on to greater things in life.")
print("With experience (from being a burglary victim),")
print("a pack of Redbull (stolen from the gas station), and a whole lot of spite,")
print("Silas is determined to turn the tables and pull off a heist on the biggest bank in the city!\n")

print("Welcome to our Stats Activity! In this activity, you will be playing as Silas, our down-on-his-luck protagonist.")
print("There are three stages to the activity: ")
print("Planning, Heisting, and Escaping!")
print("Answer the statistics questions correctly for a better chance of succeeding in your heist!")
print("If you answer too many questions wrong, Silas will fail in his heist, and he will be carted off to jail. :(")

print("\nGood luck, and let the Heisting commence!")

userStart = input("\n\n\nEnter anything to begin: ")

print("\n\n\nPart I. Planning")

print("\n\n\nAs anyone with some common sense should know, a good heist always begins with good planning.")
print("Help Silas come up with a semi-decent plan, recruit allies, and pave the way to success!")

print("\nFirst off, Silas decides to examine how long bank heists usually take.")
print("From the data, Silas concludes that the average bank heist takes around 67 minutes, with a standard deviation of 3 minutes.")
answer = input("What percentage of bank heists have a finishing time of less than 62 minutes, to the nearest tenth?\n ___% of bank heists \n")
if (answer == "4.8" or answer == "4.8%"):
    planstability = planstability + 20
    print("\nThat sounds right! 4.8% of bank heists finish in less than 62 minutes. Your plan stability is at " + str(planstability) + "%")
else:
    print("\nThat doesn't seem accurate. I think it's closer to 4.8%")

userStart = input("\n\n\nEnter anything to move on to the next question: ")

print("The amount of time it takes to get from Best Bank to Silas’s secret base location is normally distributed with a mean of 26 minutes and a standard deviation of 3 minutes.")
print("Out of the 242 times that Silas has made the journey back and forth (he wants to make sure his plan will work),")
answer = input("how many times has his commute been between 21 and 27 minutes, to the nearest whole number?\n ___ times \n")
if (answer == "141"):
    planstability = planstability + 20
    print("\nThat sounds right! His commute is between 21 and 27 minutes 141 times out of 242. Your plan stability is at " + str(planstability) + "%")
else:
    print("\nThat doesn't seem accurate. I think it's closer to 141 times.")

userStart = input("\n\n\nEnter anything to move on to the next question: ")

print("In order to successfully pull off his heist, Silas needs to get into the mind of his enemies.")
print("He needs to have a higher IQ than the majority of the bank workers.")
print("The IQ scores of the bank workers are normally distributed with a mean of 100 and a standard deviation of 15.")
answer = input("Out of a randomly selected 450 people from the bank worker population, how many of them would have an IQ higher than 122, to the nearest whole number?\n ___ bank workers\n")
if (answer == "32"):
    planstability = planstability + 20
    print("\nThat sounds right! 32 out of 450 bank workers have an IQ higher than 122. Your plan stability is at " + str(planstability) + "%")
else:
    print("\nThat doesn't seem accurate. I think it's closer to 32 bank workers.")
    
userStart = input("\n\n\nEnter anything to move on to the next question: ")

print("Since funds are limited, Silas’s weapon of choice is a Fightsaber.")
print("The amount of time a HaulMart™ MoonWars V.2.0 Fightsaber lasts is normally distributed")
print("with a mean of 1200 hours and a standard deviation of 50 hours.")
print("Out of the 775 Fightsabers currently in stock in Silas’s closest HaulMart,")
answer = input("how many would be expected to last less than 1080 hours, to the nearest whole number?\n___ Fightsabers\n")
if (answer == "6"):
    planstability = planstability + 20
    print("\nThat sounds right! 6 out of 775 Fightsabers would last less than 1080 hours. Your plan stability is at " + str(planstability) + "%")
else:
    print("\nThat doesn't seem accurate. I think it's closer to 6 Fightsabers.")
    
userStart = input("\n\n\nEnter anything to move on to the next question: ")

print("Regarding the most important part of Silas’s whole heist, he now has to focus on how much money he can earn!")
print("Since the people in Silas’s city are kind of broke, the amount of money in a bank account is normally distributed with a mean of $1100 and a standard deviation of $70.")
print("Out of the 260 bank accounts open in Best Bank,")
answer = input("how many would be expected to hold an amount of money between $1130 and $1280, to the nearest whole number?\n___ bank accounts\n")
if (answer == "86"):
    planstability = planstability + 20
    print("\nThat sounds right! 86 out of 260 bank accounts should hold between $1130 and $1280. Your plan stability is at " + str(planstability) + "%")
else:
    print("\nThat doesn't seem accurate. I think it's closer to 86 bank accounts.")
    
print("\n\nAfter long and tedious planning, your final plan stability is at " + str(planstability) + "%")

userStart = input("\n\n\nEnter anything to move on to the next part: ")

print("\n\n\nPart II. Heisting: The Target")

print("\n\n\nThe time has come for Silas to pull off his master plan! There is only one more aspect he must decide on: how much he is going to take in his heist.")

print("\nChoose your question difficulty! Choosing a harder difficulty will give you a harder question but rewards get better based on harder difficulty.")
print("You only get one question on this part, and if you fail, Silas won’t be able to get ANY rewards from his heist, so choose wisely!")
qpass = False
diffic = input("\nPlease enter \"easy\", \"medium\", or \"hard\": ")

while qpass == False:
    if (diffic == "easy"):
        rvault = "the most discrete"
        print("When considering a vault full of diamonds, a vault with 16 diamonds falls three standard deviations below the mean, while a vault with 24 diamonds falls one standard deviation above the mean.")
        answer = input("Determine the mean of the diamonds in a vault.\n___ diamonds\n")
        if (answer == "22"):
            print("\nThat sounds right! The mean number of diamonds in a vault is 22. Silas goes for the most discrete vault in Best Bank.")
            rewardscale = 1
            rvault = "the most discrete"
        else:
            print("\nThat doesn't seem accurate. I think it's closer to 22 diamonds. Silas fails to get to any vault.")
        qpass = True
    elif (diffic == "medium"):
        rvault = "a pretty average"
        print("Silas managed to acquire $700 dollars from a group of vaults with a mean of $750 and a standard deviation of $100.")
        print("He is about to move on to a group of vaults with a mean of $500 and a standard deviation of $40.")
        print("How much money must Silas acquire from the second group of vaults in order to do equivalently well to how he did on the first set?")
        answer = input("Assume that the amount of money in each group of vaults is normally distributed.\n$___\n")
        if (answer == "480"):
            print("\nThat sounds right! Silas has to get $480 from the second group to do as well as he did in the first group. Silas goes for a pretty average vault in Best Bank.")
            rewardscale = 2
            rvault = "a pretty average"
        else:
            print("\nThat doesn't seem accurate. I think it's closer to $480. Silas fails to get to any vault.")
        qpass = True
    elif (diffic == "hard"):
        rvault = "the most extravagent"
        print("While looking for more information on what the bank vaults held, Silas stumbled on a recent survey held online determining how much money people were keeping at Best Bank.")
        print("Out of a random sample of 400 people, 216 said that they kept over $2000 in their bank accounts.")
        answer = input("At the 95% confidence level, what is the margin of error for this survey expressed as a proportion to the nearest thousandth?\n")
        if (answer == "0.050" or answer == "0.05" or answer == ".05" or answer == ".050"):
            print("\nThat sounds right! The margin of error for the survey is 0.050. Silas goes for the most extravagent vault in Best Bank.")
            rewardscale = 3
            rvault = "the most extravagent"
        else:
            print("\nThat doesn't seem accurate. I think it's closer to 0.050. Silas fails to get to any vault.")
        qpass = True
    else:
        diffic = input("\nPlease enter \"easy\", \"medium\", or \"hard\": ")

if rewardscale != 0:
    print("\nSilas has chosen his target: " + rvault + " vault in Best Bank!")
else:
    print("\nSilas failed to get to his initial target, but now he's moving on to others.")
    
userStart = input("\n\n\nEnter anything to move on to the next section: ")

print("\n\n\nPart II. Heisting: The Execution")

print("\n\n\nSilas’s plan is set. His target has been chosen. He has consumed more Redbull than any human should be able to survive.")
print("He feels like he could run 10 miles in 2 minutes. He is ready.")
print("Silas is in the bank, holding a duffel bag with the rewards from the initial vault he stole from, and now he is ready to hit some more vaults.")


print("\nYour chances of success depend on the number of questions you got right during the planning phase!")
print("For every question you got right, your plan stability increased by 20%.")
print("In this section, you will be given three questions. If your: ")

print("\nPlan stability is 20%, you will need 3/3 questions right for success")
print("\nPlan stability is between 20-80%, you will need 2/3 questions right")
print("\nPlan stability is greater than 80%, you will need 1/3 questions right")

print("\n Good Luck!")

userStart = input("\n\n\nEnter anything to begin: ")

print("Silas watches as a security guard paces back and forth between the hall.")
print("The amount of time his pacing takes has a mean of 10 minutes and a standard deviation of 3 minutes.")
answer = input("What is the probability that a randomly selected round of pacing will take between 5 and 14 minutes, to the nearest thousandth?\n")
if answer == "0.861" or answer == ".861":
    print("\nThat sounds right! There is a 0.861 probability that a round of pacing will take between 5 and 14 minutes.")
    correctcount = correctcount + 1
else:
    print("\nThat doesn't seem accurate. I think it's closer to 0.861.")

userStart = input("\nEnter anything to move on: ")


print("Our determined protagonist reaches an area of smaller vaults that don’t seem to have as much money.")
print("The amount of money he has gained from each vault has a mean of $105 and a standard deviation of $10.")
answer = input("Out of the 60 vaults in this area, how many would be expected to hold more than $118, to the nearest whole number?\n___ vaults\n")

if answer == "6":
    print("\nThat sounds accurate! 6 vaults out of 60 vaults can be expected to hold more than $118.")
    correctcount = correctcount + 1
else:
    print("\nThat doesn't seem accurate. I think it's closer to 6 vaults.")
    
userStart = input("\nEnter anything to move on: ")

print("After considering the amount of money Silas has been earning from the vaults on another floor")
print("(he decided raiding all the smaller vaults wasn’t worth the risk),")
print("he tries to determine the mean amount of money he has been earning from his current vaults.")
print("His findings indicate a confidence interval for the mean amount of money to be between $465 and $499.")
answer = input("What is the margin of error on Silas’s findings?\n$___\n")

if answer == "17":
    print("\nThat sounds right! Silas's findings have a $17 margin of error.")
    correctcount = correctcount + 1
else:
    print("\nThat doesn't sound accurate. I think the margin of error is closer to $17.")

print("\nAfter trying his best at securing his profits, Silas thinks its time to move on before things take a turn for the worse.")
print("His first--and most important--target was " + rvault + " vault.")
if rewardscale == 0:
    print("Unfortunately, he was not able to break into this vault before moving on.")
else:
    print("With your help, he was able to secure his reward!")
print("\nNext, Silas moved onto the rest of the bank.")
if correctcount == 3:
    print("Thankfully, with your elite planning and execution skills, Silas was able to get the most out of the heist!")
    basereward = 1
elif correctcount == 2 and planstability >= 20:
    print("Thankfully, with your elite planning and execution skills, Silas was able to get the most out of the heist!")
    basereward = 1
elif correctcount == 1 and planstability > 80:
    print("Thankfully, with your elite planning and execution skills, Silas was able to get the most out of the heist!")
    basereward = 1
else:
    print("Unfortunately, Silas's plan was unsuccessful and he was unable to break into any vault.")
print("\nNow it's time to move on!")

userStart = input("Enter anything to move on to the next part: ")

print("\n\n\nPart III. Escaping")

print("\n\n\nSilas has his money.")
print("He’s slightly shaking, and his heart is racing.")
print("It could be nerves, or it could be the 6 Redbulls he downed before heisting finally wearing off. Regardless of the reason,")
print("Silas is ready to successfully escape and go enjoy his rewards.")
print("Perhaps he’ll move to Mexico, and live out a life of heists like in the shows he watches on cable.")
print("Or maybe he’ll just pay his rent for this month and treat himself to a donut.")

print("\nIt’s time to escape!")
print("Answer the following questions correctly in order to pull off the last step of your heist by leaving the bank with your profits.")
print("Answering too many questions incorrectly will get Silas caught by the police, so make sure to answer carefully!")

userStart = input("\nEnter anything to start: ")

print("During his planning,")
print("Silas sent out a survey to 200 people asking whether he should walk out the front entrance or leave via a window when heisting.")
print("Of those surveyed, 144 people said that he should leave out a window.")
answer = input("At the 95% confidence level, what is the margin of error for this survey expressed as a proportion to the nearest thousandth?\n")
if answer == "0.063" or answer == ".063":
    print("\nThat sounds right! The margin of error for the survey is 0.063.")
    esccount = esccount + 1
else:
    print("\nThat doesn't sound accurate. I think the margin of error is closer to 0.063.")
    
userStart = input("\nEnter anything to move on: ")

print("After considering several possible escape windows,")
print("Silas has realized that the heights of the windows are normally distributed with a mean of 70 inches and a standard deviation of 4.5 inches.")
answer = input("Out of the 300 windows at Best Bank, how many would be expected to be taller than 74 inches tall, to the nearest whole number?\n___windows\n")
if answer == "56":
    print("\nThat sounds right! 56 out of the 300 windows should be taller than 74 inches.")
    esccount = esccount + 1
else:
    print("\nThat doesn't sound accurate. I think it's closer to 56 out of the 300 windows.")
    
userStart = input("\nEnter anything to move on: ")

print("Silas has factored into account how long it takes the average person to get through each hallway in Best Bank, and knows he has to be faster.")
print("Silas takes 35 seconds to get through a hallway that has a mean of 45 seconds and a standard deviation of 10 seconds.")
print("He is about to go through a long corridor with a mean of 550 seconds and a standard deviation of 25 seconds.")
print("How much time can Silas take to get through the hallway while still doing equivalently well to his other travel time?")
answer = input("Assume that the times to get through each hallway are normally distributed.\n___ seconds\n")

if answer == "525":
    print("\nThat sounds right! Silas should take 525 if he wants to do just as well as before.")
    esccount = esccount + 1
else:
    print("\nThat doesn't sound accurate. I think it's closer to 525 seconds.")
    
userStart = input("\nEnter anything to move on: ")

print("The police have arrived at the bank!")
print("This is quite tragic for Silas,who intended to sneak out quietly.")
print("The police check through each vault as they look for Silas,")
print("and the times they take per vault are normally distributed with a mean of 64 seconds and a standard deviation of 3 seconds.")
answer = input("Using the empirical rule, what percentage of check times will take between 58 and 70 seconds?\n___%\n")

if answer == "95":
    print("\nThat sounds right! 95% of check times fall between 58 and 70 seconds.")
    esccount = esccount + 1
else:
    print("\nThat doesn't sound accurate. I think it's closer to 95%.")
    
userStart = input("\nEnter anything to move on: ")    

print("Since, like every other fed-up college drop-out, he seeks validation,")
print("Silas sent out a question to all of his friends asking whether or not he would be justified in carrying out a heist on Best Bank.")
print("The percentage of Silas’s friends who said he would be justified was 54%.")
print("The margin of error for his question’s responses was 5%.")
print("What is the confidence interval for the actual percentage of Silas’s friends who support his heist?")
answer = input("Use the format \"(XX%, XX%)\" for your answer.\n")
if answer == "(49%, 59%)":
    print("\nThat sounds right! The percentage of Silas's friends that support him should fall between 49% and 59%.")
    esccount = esccount + 1
else:
    print("\nThat doesn't sound accurate. I think it's closer to 49% to 59%.")
    
userStart = input("\n\n\nEnter anything to see your final results: ")

print("\n\n\nPart IV. Finale\n\n\n")

if esccount >= 3:
    escFT = "succeeded"
    print("Congratulations!!!")
    print("Silas has managed to escape the bank with his heist rewards, and hopefully has enough money to move to Mexico.")
    print("Considering the economy though, it is considerably more likely that he now has enough money to at least pay off his monthly rent and buy a donut.")
    print("Good job on answering the questions correctly!")
else:
    escFT = "failed"
    print("Tragically, Silas was caught by the police before he could leave with his heist rewards.")
    print("He will not be able to move to Mexico, or pay his rent, or even buy a donut and another pack of Redbull.")
    print("Even worse, Silas now has to find a way to pay bail and hire a lawyer!")
    print("Things aren’t looking very bright for our protagonist, but hopefully he’ll find a way to pull through.")

print("\nYour answers and choices led you to: ")
print("Plan Stability: " + str(planstability) + "%")
print("Heist Difficulty: " + diffic)
print("Execution: " + str(correctcount))
print("Escape: " + escFT)
totalr = (basereward * 3) + (rewardscale * 2)
print("Total Reward: $" + str(totalr) + "00,000")


