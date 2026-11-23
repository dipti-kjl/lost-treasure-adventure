"""
The Lost Treasure Adventure
===========================
A colorful "Choose Your Own Adventure" game for the terminal.

How the game works (big picture):
    1. main() shows a welcome screen and asks for your name.
    2. play_adventure() runs ONE round of the story.
    3. The story splits into small functions (cave_path, bridge_path).
       Each one returns True if you WIN and False if you LOSE.
    4. main() keeps looping until the player says they don't want to play again.

Only beginner-friendly Python is used: variables, input(), print(),
if/elif/else, while loops, string methods and functions.
The only outside library is colorama (for colored text).
"""

from colorama import Fore, Style, init

# init() makes colors work on Windows too.
# autoreset=True means the color turns off after every print,
# so we never have to remember to "turn off" a color.
init(autoreset=True)

# How wide (in characters) our decorative boxes are.
WIDTH = 58


# ---------------------------------------------------------------------------
# Helper functions: small tools used again and again by the story
# ---------------------------------------------------------------------------

def print_box(lines, color):
    """Print a list of text lines inside a decorative box in the given color."""
    print(color + Style.BRIGHT + "╔" + "═" * WIDTH + "╗")
    for line in lines:
        # .center() puts the text in the middle of the box.
        print(color + Style.BRIGHT + "║" + line.center(WIDTH) + "║")
    print(color + Style.BRIGHT + "╚" + "═" * WIDTH + "╝")


def say(text):
    """Print one line of story text in white."""
    print(Fore.WHITE + text)


def ask_choice(prompt, options):
    """
    Ask a question and KEEP asking until the player types a valid answer.

    prompt  -> the question to show, e.g. "Left or right? "
    options -> list of allowed answers, e.g. ["left", "right"]

    Returns the cleaned-up answer (lowercase, no extra spaces).
    """
    while True:
        # .strip() removes accidental spaces, .lower() ignores CAPITAL letters.
        answer = input(Fore.YELLOW + Style.BRIGHT + prompt).strip().lower()
        if answer in options:
            return answer
        # Wrong answer: explain what is allowed, then the loop asks again.
        print(Fore.RED + "❌ Oops! Please type one of: " + " / ".join(options))


def ask_yes_no(prompt):
    """Ask a yes/no question. Returns True for yes and False for no."""
    answer = ask_choice(prompt, ["yes", "y", "no", "n"])
    return answer in ("yes", "y")


def ask_name():
    """Ask for the player's name. An empty name is not allowed."""
    while True:
        name = input(Fore.YELLOW + Style.BRIGHT + "🧑 Hey explorer, what is your name? ").strip()
        if name != "":
            return name
        print(Fore.RED + "❌ Please type a name so I know who you are!")


# ---------------------------------------------------------------------------
# Screens: the big colorful messages
# ---------------------------------------------------------------------------

def show_welcome():
    """Show the title screen when the game starts."""
    print()
    print(Fore.GREEN + "🌲 ✨ 🌲 ✨ 🌲 ✨ 🌲 ✨ 🌲 ✨ 🌲 ✨ 🌲".center(WIDTH + 2))
    print_box(
        [
            "",
            "THE LOST TREASURE",
            "A D V E N T U R E",
            "",
            "~ A Choose Your Own Adventure ~",
            "",
        ],
        Fore.CYAN,
    )
    print(Fore.GREEN + "🌲 ✨ 🌲 ✨ 🌲 ✨ 🌲 ✨ 🌲 ✨ 🌲 ✨ 🌲".center(WIDTH + 2))
    print()


def show_win(name):
    """Show the winning message."""
    # Emojis are 2 characters wide, so we keep them OUTSIDE the box
    # (inside, they would push the right border out of line).
    print()
    print(Fore.GREEN + "🏆 🏆 🏆 🏆 🏆 🏆 🏆 🏆 🏆 🏆".center(WIDTH + 2))
    print_box(["", "YOU WIN!", f"Amazing job, {name}!", "The treasure is yours!", ""], Fore.GREEN)
    print(Fore.GREEN + "💰 💎 👑 💰 💎 👑 💰 💎 👑 💰 💎 👑".center(WIDTH + 2))
    print()


def show_game_over(name):
    """Show the game over message."""
    print()
    print(Fore.RED + "💀 💀 💀 💀 💀 💀 💀 💀 💀 💀".center(WIDTH + 2))
    print_box(["", "GAME OVER", f"Oh no, {name}...", ""], Fore.RED)
    print()


def show_try_again():
    """Show an encouraging message after a loss."""
    print(Fore.MAGENTA + Style.BRIGHT + "🔄 TRY AGAIN! Every great explorer fails a few times first.")
    print()


def show_goodbye(name, wins, losses):
    """Show the final message with the player's name and their score."""
    print()
    print_box(
        [
            "",
            f"Thanks for playing, {name}!",
            f"Treasures found: {wins}   Adventures lost: {losses}",
            "See you on the next adventure!",
            "",
        ],
        Fore.CYAN,
    )
    print(Fore.CYAN + "👋 👋 👋".center(WIDTH + 2))
    print()


# ---------------------------------------------------------------------------
# Story paths: each function plays one part of the story
# Each one returns True (the player wins) or False (the player loses).
# ---------------------------------------------------------------------------

def cave_path():
    """The LEFT path: a dark cave with two tunnels."""
    print()
    print(Fore.MAGENTA + "🕳️  You step into the dark cave. Water drips somewhere far away...")
    say("Ahead, the cave splits into two tunnels.")
    say("  • One tunnel glows with a warm golden light.   ✨")
    say("  • The other tunnel echoes with a deep growl.   🐉")
    print()

    tunnel = ask_choice("Which tunnel do you take? (glow/growl) ", ["glow", "growl"])

    if tunnel == "glow":
        # Good choice: the glowing tunnel leads straight to the treasure.
        print()
        print(Fore.YELLOW + "✨ The light leads you to a mysterious treasure chest!")
        say("You lift the heavy lid... it is FULL of gold coins and jewels!")
        return True

    # The player chose the growling tunnel.
    print()
    print(Fore.RED + "🐉 A giant cave creature blocks your way! Its eyes glow red.")
    say("It has not noticed you yet. You must decide fast!")
    print()

    action = ask_choice("Do you fight it or hide? (fight/hide) ", ["fight", "hide"])

    if action == "hide":
        # Smart choice: the creature wanders away and reveals a chest.
        print()
        print(Fore.GREEN + "🤫 You hide behind a rock. The creature sniffs around and leaves.")
        say("Behind where it was sleeping, you find a hidden treasure chest!")
        return True

    # The player chose to fight and loses.
    print()
    print(Fore.RED + "⚔️  You swing your stick at the creature... it was a bad idea.")
    say("The creature roars and chases you out of the cave. You lose the treasure hunt!")
    return False


def bridge_path():
    """The RIGHT path: an old bridge over a river."""
    print()
    print(Fore.BLUE + "🌉 You walk to an old wooden bridge above a wide, green river.")
    say("The planks creak loudly. Something moves in the water below...")
    print()

    choice = ask_choice("Do you cross the bridge or swim under it? (cross/swim) ", ["cross", "swim"])

    if choice == "swim":
        print()
        print(Fore.RED + "🐊 You jump in the water... and an alligator swims right up to you!")
        say("Chomp! The adventure ends here.")
        return False

    # The player chose to cross.
    print()
    print(Fore.GREEN + "🚶 You carefully cross the bridge to the other side.")
    say("Under a big oak tree, the ground looks freshly dug...")
    print(Fore.YELLOW + "💎 You dig and find a hidden treasure!")
    return True


def play_adventure(name):
    """
    Play ONE full round of the story.
    Returns True if the player wins, or False if the player loses.
    """
    print()
    print(Fore.CYAN + Style.BRIGHT + "📜 THE STORY BEGINS...")
    say(f"{name}, you are exploring a mysterious forest.")
    say("An old map says a hidden treasure waits deep inside.")
    say("After an hour of walking, the path splits in two:")
    print()
    print(Fore.MAGENTA + "  ⬅️  LEFT  : a dark cave 🕳️")
    print(Fore.BLUE + "  ➡️  RIGHT : an old bridge 🌉")
    print()

    direction = ask_choice("Do you go left or right? (left/right) ", ["left", "right"])

    if direction == "left":
        return cave_path()
    return bridge_path()


# ---------------------------------------------------------------------------
# The main function: connects everything together
# ---------------------------------------------------------------------------

def main():
    """Run the whole game, including the play-again loop."""
    show_welcome()

    name = ask_name()
    print(Fore.GREEN + Style.BRIGHT + f"\n👋 Hello {name}! Welcome to my game!\n")

    if not ask_yes_no("🎮 Do you want to start the adventure? (yes/no) "):
        print(Fore.YELLOW + "\nNo problem! Come back when you feel brave.")
        show_goodbye(name, 0, 0)
        return

    # Score counters. They start at 0 and go up after each round.
    wins = 0
    losses = 0

    # This loop repeats the game until the player chooses to stop.
    while True:
        won = play_adventure(name)

        if won:
            wins += 1
            show_win(name)
        else:
            losses += 1
            show_game_over(name)
            show_try_again()

        if not ask_yes_no("🔁 Do you want to play again? (yes/no) "):
            break  # leave the loop -> the game ends

    show_goodbye(name, wins, losses)


# This line means: only start the game when this file is run directly
# (python game.py). It will NOT start when the tests import this file.
if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        # The player pressed Ctrl+C (or the input ended): leave politely.
        print(Fore.YELLOW + "\n\n👋 Game closed. Thanks for playing!")
