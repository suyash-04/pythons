import random
def play():
   user = input("Whats you choice?? 'r' for rock, 's' for scissors and 'p' for paper:\n")
   computer = random.choice(['r','s','p'])
   


   if is_win(user,computer):
      return print('YOU WON!!!')   
   return print('YOU LOST!!')
   
   if user == computer:
      print("It\'s a tie")
   
def is_win(player, oppnent):
   
   if (player == 'r' and oppnent =='s') or (player == 's' and oppnent == 'p') or (player =='p' and oppnent == 'r'):
      return True

play()
