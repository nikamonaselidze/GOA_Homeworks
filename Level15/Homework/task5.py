#5)შექმენით ცვლადი სადაც შეინახავთ ორიგინალ აქაუნთის პაროლს, და while ციკლის მეშვეობით მომხმარებელს შეეკითხეთ აქაუნთის პაროლი იქამდე სანამ სწორედ არ გამოიცნობს.
password="nikanika"
guess=input("Enter Your Password: ")
while guess != password:
    guess = input()
print("Correct!")