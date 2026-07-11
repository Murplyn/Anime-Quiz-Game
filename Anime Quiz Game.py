#Anime Quiz Game
# Think you're a true anime fan?

#Then test your knowledge with this anime game,
#There are 10 questions covering
#popular anime series and characters. Type your
# answers and see how many you get right!
# 
# At the end of the game, you'll receive a rank
# based on your score:
# 
# 0–5  you are a  Anime Newbie
# 6–8  you are a Average Anime Watcher
# 9–10 you are a → Elite Anime Watcher
# 
# Good luck, and have fun!

user = input(" TIME TO PLAY THE ANIME GAME type start to BEGIN :) ")
user_start = 'start'
game_station = {'\n Which anime is based on the Law of Equivalent Exchange?': 'Fullmetal Alchemist',
                '\nWhich anime won Anime of the Year in 2026?': 'My Hero Academia',
                '\n Who was the first member to join Luffy\'s crew?': 'Zoro',
                '\n Which anime teaches the power of friendship?': 'Fairy Tail',
                '\n In Attack on Titan, what do Titans feed on?': 'Humans',
                '\n What is the name of Naruto\'s signature move?': 'Shadow Clone Jutsu',
                '\n What color is Yona\'s hair in Yona of the Dawn?': 'Red',
                '\n What is Lord\'s Death Number from Soul Eater': '42-42-564',
                '\n What did Light Yagami called himself after acquring the Death note?': 'Kira',
                '\n Which member of Frieren\'s party is a First-Class Mage?': 'Fern'}
 

while user.lower() != user_start.lower():
    user = input(" TIME TO PLAY THE ANIME GAME type 'start' to BEGIN :) ")
 
count = 0
for user_key in game_station:
    correct_value = game_station[user_key]
    user_input = input(user_key + " ")
    if user_input.lower() == correct_value.lower():
        print(f"✅ {correct_value} is correct")
        count+=1

    else:
        print(f"❌ Sorry it's {correct_value}")

if count <= 5:
    print(f' \n Welcome to the club newbie!')
    print(f" Final Score: {count}/10")

elif count <=8:
    print(f' \n You are an average anime watcher!')
    print(f" Final Score: {count}/10")

else:
    print(f' \n You are an elite anime watcher!')
    print(f" Final Score: {count}/10")
    


print("\nThanks for playing the Anime Quiz Game!")

  