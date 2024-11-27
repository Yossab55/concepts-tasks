import random

def word_scramble_game() :
  my_words = ["skills", "programming", "software", "python", "javascript"]

  original_word = random.choice(my_words)

  scrambled_word = ''.join(random.sample(original_word, len(original_word)))

  attempts = 5
  print("welcome to scramble game")
  print(f"you have five attempts and the scrambled word is {scrambled_word}")
  
  while attempts > 0 :
    guess = input("enter your guess : ").strip().lower()

    if not guess :
      print("invalid input. please enter correct guess.")
      continue

    if guess == original_word:
      print(f"bravo: you've guessed correctly and it's {original_word} in {5 - attempts} times")
      break
    else: 
      attempts -= 1
      if attempts == 0 :
        print("you ran out of attempts")
        break
      else:
        print(f"wrong answer you still have {attempts} times more")

word_scramble_game()