#PART A
#------------wins_rocks_Scissors_paper
def wins_rock_scissors_paper(player_throw, opponent_throw):
    
    player = player_throw.lower()
    opponent = opponent_throw.lower()
    
    # Determine if the player wins
    if player == 'rock' and opponent == 'scissors':
        return True
    elif player == 'paper' and opponent == 'rock':
        return True
    elif player == 'scissors' and opponent == 'paper':
        return True
    
    
    return False

#-------------FACTORIAL
def factorial(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * factorial(number - 1)  

#-------------FIBONICCA
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib = [0, 1]
        for i in range(2, n + 1):
            fib.append(fib[i - 1] + fib[i - 2])
        return fib[n]

#------------sum_to_goal
def sum_to_goal(numbers, goal):
    seen = set()
    for number in numbers:
        complement = goal - number
        if complement in seen:
            return number * complement
        seen.add(number)
    return 0

#PYTHON OBJECT 
class UpCounter:
    def __init__(self, step_size=1):
        self.step_size = step_size
        self.value = 0
    
    def count(self):
        return self.value
    
    def update(self):
        self.value += self.step_size

class DownCounter(UpCounter):
    def update(self):
        self.value -= self.step_size

# Example usage:
print(wins_rock_scissors_paper("rock", "scissors"))  
print(wins_rock_scissors_paper("ROCK", "PAPER"))     
print(wins_rock_scissors_paper("scissors", "paper")) 
print(wins_rock_scissors_paper("Scissors", "Scissors")) 
print(factorial(4))
print(fibonacci(3))
numbers = [1, 3, 7, 9]
goal = 10
result = sum_to_goal(numbers, goal)
print(result)
