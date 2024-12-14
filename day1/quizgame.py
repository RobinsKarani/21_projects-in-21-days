print("***Welcome to my quiz game***")

playing = input("Do you want to play?(y/n): ")
playing.lower()

if playing != "y":
    quit()
print("Okay! Let's play")   
score = 0

#question1
answer = int(input("What is 3 *13? "))
if answer == (3*13):
    print("Correct!")
    score += 1
else:
    print("Incorrect!")    

#question1
answer = int(input("What is 7 *13? "))
if answer == (7*13):
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

percentageScore = score/2 * 100

print(f"Your score is {percentageScore}%")        

