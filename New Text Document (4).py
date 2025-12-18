import random
import time

# Define all 22 programming challenges
CHALLENGES = {
    1: {
        "name": "Print 'Hello World'",
        "task": "Write a program to print 'Hello World'",
        "solution": 'print("Hello World")'
    },
    2: {
        "name": "Print 'Welcome to MRIST'",
        "task": "Write a program to print 'Welcome to MRIST'",
        "solution": 'print("Welcome to MRIST")'
    },
    3: {
        "name": "Input and Display Name",
        "task": "Write a program to take a name as input and display it",
        "solution": 'name = input("Enter your name: ")\nprint(name)'
    },
    4: {
        "name": "Name with MRIST",
        "task": "Write a program to take a name as input and display it along with 'MRIST'",
        "solution": 'name = input("Enter your name: ")\nprint(name + " - MRIST")'
    },
    5: {
        "name": "Even or Odd",
        "task": "Write a program to check whether a given number is even or odd",
        "solution": 'num = int(input("Enter a number: "))\nif num % 2 == 0:\n    print(f"{num} is even")\nelse:\n    print(f"{num} is odd")'
    },
    6: {
        "name": "Positive or Negative",
        "task": "Write a program to check whether a given number is positive or negative",
        "solution": 'num = int(input("Enter a number: "))\nif num > 0:\n    print(f"{num} is positive")\nelif num < 0:\n    print(f"{num} is negative")\nelse:\n    print(f"{num} is zero")'
    },
    7: {
        "name": "Vowel or Consonant",
        "task": "Write a program to check whether a given character is a vowel or consonant",
        "solution": 'char = input("Enter a character: ")\nif char.lower() in ["a", "e", "i", "o", "u"]:\n    print(f"{char} is a vowel")\nelse:\n    print(f"{char} is a consonant")'
    },
    8: {
        "name": "Leap Year Check",
        "task": "Write a program to check whether a given year is a leap year",
        "solution": 'year = int(input("Enter a year: "))\nif (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):\n    print(f"{year} is a leap year")\nelse:\n    print(f"{year} is not a leap year")'
    },
    9: {
        "name": "Area of Circle",
        "task": "Write a program to calculate the area of a circle",
        "solution": 'import math\nradius = float(input("Enter the radius of circle: "))\narea = math.pi * radius * radius\nprint(f"Area of circle: {area:.2f}")'
    },
    10: {
        "name": "Area of Triangle",
        "task": "Write a program to calculate the area of a triangle",
        "solution": 'base = float(input("Enter the base of triangle: "))\nheight = float(input("Enter the height of triangle: "))\narea = (base * height) / 2\nprint(f"Area of triangle: {area:.2f}")'
    },
    11: {
        "name": "Area of Rectangle",
        "task": "Write a program to calculate the area of a rectangle",
        "solution": 'length = float(input("Enter the length of rectangle: "))\nwidth = float(input("Enter the width of rectangle: "))\narea = length * width\nprint(f"Area of rectangle: {area:.2f}")'
    },
    12: {
        "name": "Area of Square",
        "task": "Write a program to calculate the area of a square",
        "solution": 'side = float(input("Enter the side of square: "))\narea = side * side\nprint(f"Area of square: {area:.2f}")'
    },
    13: {
        "name": "Numbers 1 to 100",
        "task": "Write a program to display numbers from 1 to 100 using a loop",
        "solution": 'for i in range(1, 101):\n    print(i, end=" ")'
    },
    14: {
        "name": "Even Numbers 10-100",
        "task": "Write a program to display even numbers from 10 to 100",
        "solution": 'for i in range(10, 101):\n    if i % 2 == 0:\n        print(i, end=" ")'
    },
    15: {
        "name": "Odd Numbers 10-100",
        "task": "Write a program to display odd numbers from 10 to 100",
        "solution": 'for i in range(10, 101):\n    if i % 2 != 0:\n        print(i, end=" ")'
    },
    16: {
        "name": "Sum 1+2+...+n",
        "task": "Write a program to find the sum of series 1 + 2 + 3 + 4 + ... + n",
        "solution": 'n = int(input("Enter n: "))\nsum_val = 0\nfor i in range(1, n + 1):\n    sum_val += i\nprint(f"Sum of series: {sum_val}")'
    },
    17: {
        "name": "Sum 2+4+6+...+n",
        "task": "Write a program to find the sum of series 2 + 4 + 6 + ... + n",
        "solution": 'n = int(input("Enter n: "))\nsum_val = 0\nfor i in range(2, n + 1, 2):\n    sum_val += i\nprint(f"Sum of even series: {sum_val}")'
    },
    18: {
        "name": "Product (Factorial)",
        "task": "Write a program to calculate the product of series 1 × 2 × 3 × 4 × ... × n",
        "solution": 'n = int(input("Enter n: "))\nproduct = 1\nfor i in range(1, n + 1):\n    product *= i\nprint(f"Product (Factorial): {product}")'
    },
    19: {
        "name": "Star Pattern",
        "task": "Write a program to print the star pattern:\n*\n**\n***\n****",
        "solution": 'n = int(input("Enter number of rows: "))\nfor i in range(1, n + 1):\n    for j in range(i):\n        print("*", end="")\n    print()'
    },
    20: {
        "name": "Multiplication Table",
        "task": "Write a program to generate the multiplication table of a given number",
        "solution": 'num = int(input("Enter a number: "))\nfor i in range(1, 11):\n    print(f"{num} x {i} = {num * i}")'
    },
    21: {
        "name": "Function: Even or Odd",
        "task": "Write a program using a function to check whether a number is even or odd",
        "solution": 'def check_even_odd(num):\n    if num % 2 == 0:\n        return f"{num} is even"\n    else:\n        return f"{num} is odd"\n\nnumber = int(input("Enter a number: "))\nprint(check_even_odd(number))'
    },
    22: {
        "name": "Function: Leap Year",
        "task": "Write a program using a function to check whether a year is a leap year",
        "solution": 'def is_leap_year(year):\n    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):\n        return f"{year} is a leap year"\n    else:\n        return f"{year} is not a leap year"\n\nyear = int(input("Enter a year: "))\nprint(is_leap_year(year))'
    }
}

class MRISTLotteryGame:
    def __init__(self):
        self.players = {}
        self.game_history = []
        
    def register_players(self):
        """Register players for the lottery"""
        print("\n" + "="*60)
        print("🎰 WELCOME TO MRIST LOTTERY GAME 🎰".center(60))
        print("="*60)
        print("\nRegister players for the lottery game")
        print("-"*60)
        
        num_players = int(input("Enter number of players: "))
        
        for i in range(1, num_players + 1):
            player_name = input(f"Enter player {i} name: ")
            player_code = f"MRIST-{i:03d}"
            self.players[player_code] = {
                "name": player_name,
                "code": player_code,
                "tasks_completed": 0,
                "challenges": []
            }
            print(f"✓ Player {player_name} registered with code: {player_code}")
        
        print("\n" + "="*60)
        print(f"Total players registered: {len(self.players)}")
        print("="*60)
    
    def display_codes(self):
        """Display all registered player codes"""
        print("\n📋 REGISTERED PLAYER CODES:")
        print("-"*60)
        for code, player in self.players.items():
            print(f"{code} --> {player['name']}")
        print("-"*60)
    
    def draw_lottery(self):
        """Draw a random player code"""
        print("\n🎲 DRAWING LOTTERY...".center(60))
        print("-"*60)
        
        # Simulate lottery draw animation
        codes = list(self.players.keys())
        for _ in range(20):
            print(f"🎰 {random.choice(codes)} 🎰", end="\r")
            time.sleep(0.1)
        
        drawn_code = random.choice(codes)
        print(f"\n✅ LOTTERY WINNER: {drawn_code} --> {self.players[drawn_code]['name']}")
        print("-"*60)
        
        return drawn_code
    
    def assign_challenge(self, player_code):
        """Assign a random challenge to the player"""
        challenge_num = random.randint(1, 22)
        challenge = CHALLENGES[challenge_num]
        
        self.players[player_code]["challenges"].append(challenge_num)
        
        print("\n📝 CHALLENGE ASSIGNED:")
        print("="*60)
        print(f"Player: {self.players[player_code]['name']}")
        print(f"Code: {player_code}")
        print(f"Challenge #{challenge_num}: {challenge['name']}")
        print("-"*60)
        print(f"TASK: {challenge['task']}")
        print("-"*60)
        print(f"SOLUTION HINT:\n{challenge['solution']}")
        print("="*60)
        
        return challenge_num
    
    def play_round(self):
        """Play one complete round of lottery"""
        if not self.players:
            print("No players registered!")
            return
        
        # Draw lottery
        drawn_code = self.draw_lottery()
        
        # Assign challenge
        challenge_num = self.assign_challenge(drawn_code)
        
        # Record in history
        self.game_history.append({
            "code": drawn_code,
            "player": self.players[drawn_code]["name"],
            "challenge": challenge_num
        })
        
        self.players[drawn_code]["tasks_completed"] += 1
        
        # Ask to play again
        print("\n" + "="*60)
        play_again = input("Play another round? (yes/no): ").lower()
        return play_again == 'yes' or play_again == 'y'
    
    def show_statistics(self):
        """Display game statistics"""
        print("\n" + "="*60)
        print("📊 GAME STATISTICS".center(60))
        print("="*60)
        print(f"Total Rounds Played: {len(self.game_history)}")
        print("\nPlayer Performance:")
        print("-"*60)
        
        for code, player in self.players.items():
            print(f"{player['name']:20} ({code}): {player['tasks_completed']} tasks completed")
        
        print("-"*60)
        print("\nChallenge History:")
        print("-"*60)
        for i, record in enumerate(self.game_history, 1):
            print(f"{i}. {record['player']:20} - Challenge #{record['challenge']:2} ({CHALLENGES[record['challenge']]['name']})")
        print("="*60)
    
    def run_game(self):
        """Main game loop"""
        try:
            # Register players
            self.register_players()
            
            # Display all codes
            self.display_codes()
            
            # Play rounds
            while True:
                if not self.play_round():
                    break
            
            # Show statistics
            self.show_statistics()
            
            print("\n🎊 THANKS FOR PLAYING MRIST LOTTERY GAME! 🎊".center(60))
            
        except KeyboardInterrupt:
            print("\n\n⚠️  Game interrupted by user!")
            self.show_statistics()
        except Exception as e:
            print(f"\n❌ Error: {e}")

# Run the game
if __name__ == "__main__":
    game = MRISTLotteryGame()
    game.run_game()
