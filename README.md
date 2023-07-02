# Slot-Machine
This is a simple implementation of a slot machine game in Python. The program allows the user to play the slot machine by spinning the reels and matching symbols to win Money

## How to Play
- Run the script using a Python interpreter.
- Enter the amount you want to deposit when prompted. The amount should be greater than 0.
- Choose the number of lines you want to bet on. Enter a number between 1 and the maximum number of lines specified.
- Enter the bet amount. The bet should be within the specified minimum and maximum bet limits.
- The slot machine will spin and display the symbols on the reels.
- Check if you have any winning combinations on the lines you bet on.
- Your winnings will be calculated based on the matching symbols and the bet amount.
- The game will deduct the total bet amount from your balance and update it accordingly.
- You can continue playing by pressing ENTER to spin the reels again or press Q to quit the game.
- The game will end when you choose to quit or if your balance becomes zero.

## Features

- Three reels with various symbols.
- Random generation of symbols for each reel spin.
- Betting on multiple lines and adjusting the bet amount.
- Calculation of winnings based on matching symbols and bet amount.
- User-friendly interface with clear instructions and prompts.
- Balance tracking and updating after each game.

## Customization

- `MAX_LINE`: The maximum number of lines available for betting.
- `MIN_BET` and `MAX_BET`: The minimum and maximum bet amounts allowed.
- `rows` and `cols`: The number of rows and columns on the slot machine.
- `symbol_count`: A dictionary defining the count of each symbol available on the reels.
- `symbol_values`: A dictionary assigning point values to each symbol.
