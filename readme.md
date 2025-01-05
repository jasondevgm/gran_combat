# Gran Combate

Gran Combate is a text-based fighting game implemented in Python. The game allows players to create fighters with different attributes and schools, and then engage in a combat simulation.

![Gran Combate!](gran_combate.gif "Gran Combate")

## Requirements

- Python 3.x
- `rich` library for console output
- `inquirer` library for interactive prompts

## Installation

1. Install the required libraries using pip:
    ```sh
    pip install rich inquirer
    ```

2. Clone the repository or download the script.

## Usage

Run the script using Python:
```sh
python granCombat.py
```

## Game Overview

### Classes

- **Phrases**: Contains various phrases used during the fight for attacks, dodges, hits, fails, finishing moves, and winning announcements.
- **Fighter**: Represents a fighter with attributes such as power, physique, size, skill, personality, and school. It also calculates derived statistics like resistance points, damage points, attack probability, and dodge probability.

### Functions

- **firstPlayerCreation(nPlayer)**: Initializes the first player by selecting a character and school.
- **secondPlayerCreation(nPlayer)**: Initializes the second player by selecting a character and school.
- **inputValidator(ability)**: Validates the input for fighter abilities.
- **createFighter(fname, *args)**: Creates a Fighter instance.
- **fighterFunction72(fighterName, fighterSchool, nPlayer)**: Helper function to set up fighter statistics.
- **functionStatsForFighter(fight3r, pwer, physiq, siz, skll, personalty, fschool, nPlayer)**: Sets up and validates fighter statistics.
- **fightInit(p1, p2)**: Simulates a fight round between two fighters.
- **combatField()**: Manages the combat field and determines the winner.
- **_main_()**: Main function to start the game.

## Game Flow

1. The game starts by creating two players.
2. Each player selects a character and a school.
3. Players distribute points among their fighter's abilities.
4. The combat begins, and fighters take turns attacking and dodging.
5. The game announces the winner based on the remaining resistance points.

## License

This project is licensed under the MIT License.