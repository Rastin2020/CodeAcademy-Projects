import random;

money = 100;

# Write your game of chance functions here:
def flipCoin(call, moneybet):
  global money;
  
  if (moneybet > money):
    print("Insufficient Funds.");
  elif (moneybet <= 0):
    print("Please bet something legitimate.");
  else:
    num = random.randint(1, 2);
    result = "";

    if (num == 1):
      result += "Heads";
    else:
      result += "Tails";
      
    print("You called {}. Coin is flipped and lands on {}!".format(call, result))
    
    if (call.lower() == "Heads".lower()):
      if (result.lower() == "Heads".lower()):
        print("You win {}!".format(moneybet));
        money += moneybet;
      else: 
        print("You lose {}...".format(moneybet));
        money -= moneybet;
    elif (call.lower() == "Tails".lower()):
      if (result.lower() == "Tails".lower()):
        print("You win {}!".format(moneybet));
        money += moneybet;
      else: 
        print("You lose {}...".format(moneybet));
        money -= moneybet;
  
  print("You now have {}".format(money));
# -------------------------------------------------
def choHan(guess, moneybet):
  global money;
  
  if (moneybet > money):
    print("Insufficient Funds.");
  elif (moneybet <= 0):
    print("Please bet something legitimate.");
  else:
    num1 = random.randint(1, 6);
    num2 = random.randint(1, 6);
    _sum = num1 + num2;
    if (_sum % 2 == 0):
      answer = "Even";
    else:
      answer = "Odd";

    print("The sum of both dices is {}. You guessed {}".format(_sum, guess));

    if(guess.lower() == answer.lower()):
      print("You win {}!".format(moneybet));
      money += moneybet;
    else:
      print("You lose {}...".format(moneybet));
      money -= moneybet;

  print("You now have {}".format(money));
# -------------------------------------------------
def pickCard(moneybet):
  global money;
  
  if (moneybet > money):
    print("Insufficient Funds.");
  elif (moneybet <= 0):
    print("Please bet something legitimate.");
  else:
    deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13];
    playerPick = deck.pop(random.randint(1, len(deck))-1);
    computerPick = deck.pop(random.randint(1, len(deck))-1);

    print("You got {}. Computer got {}.".format(playerPick, computerPick));

    if (playerPick > computerPick):
      print("You win {}!".format(moneybet));
      money += moneybet;
    elif (computerPick > playerPick):
      print("You lose {}...".format(moneybet));
      money -= moneybet;
    else:
      print("It's a draw.");
      
  print("You now have {}".format(money));
  
# Call your game of chance functions here:
flipCoin("Heads", 25);
flipCoin("Tails", 25);
flipCoin("heads", 25);
flipCoin("tails", 25);
print("---------------------------------------------");
choHan("Odd", 25);
choHan("Even", 25);
choHan("odd", 25);
choHan("even", 25);
print("---------------------------------------------");
pickCard(5);
