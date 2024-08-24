import os
import random
os.environ['TERM'] = 'xterm'

decks = input("Введите количество колод: ")

# умножаем список карт одной масти на 4 и на количество колод decks
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] * (int(decks) * 4)

# initialize scores
wins = 0
losses = 0


def deal(deck_func):
    hand = []
    for i in range(2):
        random.shuffle(deck_func)
        card = deck_func.pop()
        if card == 11:
            card = "J"
        if card == 12:
            card = "Q"
        if card == 13:
            card = "K"
        if card == 14:
            card = "A"
        hand.append(card)
    return hand


def play_again():
    again = input("Хотите сыграть снова? (Да/Нет) : ").lower()
    if again == "да":
        dealer_hand = []
        player_hand = []
        deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] * 4
        game()
    else:
        print("Казино всегда выигрывает!")
        exit()


def total(hand):
    points = 0
    for card in hand:
        if card == "J" or card == "Q" or card == "K":
            points += 10
        elif card == "A":
            if points >= 11:
                points += 1
            else:
                points += 11
        else:
            points += card
    return points


def hit(hand):
    card = deck.pop()
    if card == 11:
        card = "J"
    if card == 12:
        card = "Q"
    if card == 13:
        card = "K"
    if card == 14:
        card = "A"
    hand.append(card)
    return hand


# очишаем экран в консоли
def clear():
    if os.name == 'nt':
        os.system('CLS')
    if os.name == 'posix':
        os.system('clear')


def print_results(dealer_hand, player_hand):
    clear()

    print("\n    Итоги\n")
    print("-" * 30 + "\n")
    print("    \033[1;32;40mПОБЕДЫ:  \033[1;37;40m%s   \033[1;31;40mПОРАЖЕНИЯ:  \033[1;37;40m%s\n" % (wins, losses))
    print("-" * 30 + "\n")
    print("У раздающего на руке: " + str(dealer_hand) + ", в сумме: " + str(total(dealer_hand)))
    print("У вас на руке: " + str(player_hand) + ", в сумме: " + str(total(player_hand)))


def blackjack(dealer_hand, player_hand):
    global wins
    global losses
    if total(player_hand) == 21:
        print_results(dealer_hand, player_hand)
        print("Поздравляю! У вас 21, вы выиграли!\n")
        wins += 1
        play_again()
    elif total(dealer_hand) == 21:
        print_results(dealer_hand, player_hand)
        print("Простите, вы проиграли. У раздающего 21.\n")
        losses += 1
        play_again()


def score(dealer_hand, player_hand):
    # score function now updates to global win/loss variables
    global wins
    global losses
    if total(player_hand) == 21:
        print_results(dealer_hand, player_hand)
        print("score Поздравляю! У вас 21, вы выиграли!\n")
        wins += 1
    elif total(dealer_hand) == 21:
        print_results(dealer_hand, player_hand)
        print("score Простите, вы проиграли. У раздающего 21.\n")
        losses += 1
    elif total(player_hand) > 21:
        print_results(dealer_hand, player_hand)
        print("score У вас перебор. Вы проиграли.\n")
        losses += 1
    elif total(dealer_hand) > 21:
        print_results(dealer_hand, player_hand)
        print("score У раздающего перебор. Вы выиграли!\n")
        wins += 1
    elif total(player_hand) < total(dealer_hand):
        print_results(dealer_hand, player_hand)
        print("score У раздающего больше очков, чем у вас. Вы проиграли.\n")
        losses += 1
    elif total(player_hand) > total(dealer_hand):
        print_results(dealer_hand, player_hand)
        print("score Поздравляю, у вас больше очков, чем у раздающего. Вы выиграли!\n")
        wins += 1


def game():
    global wins
    global losses
    choice = 0
    clear()
    print("\n    Новая игра!\n")
    print("-" * 30 + "\n")
    print("    \033[1;32;40mПОБЕДЫ:  \033[1;37;40m%s   \033[1;31;40mПОРАЖЕНИЯ:  \033[1;37;40m%s\n" % (wins, losses))
    print("-" * 30 + "\n")
    dealer_hand = deal(deck)
    player_hand = deal(deck)
    print("Раздающий показывает " + str(dealer_hand[0]))
    print("У вас на руке:" + str(player_hand) + ", в сумме количество очков равно " + str(total(player_hand)))
    blackjack(dealer_hand, player_hand)
    quit = False
    while not quit:
        choice = input("Вы хотите [д]обрать карту, [о]становиться или [в]ыйти из игры? ").lower()
        if choice == 'д':
            hit(player_hand)
            print(player_hand)
            print("Сумма ваших очков: " + str(total(player_hand)))
            if total(player_hand) > 21:
                print('У вас перебор')
                losses += 1
                play_again()
        elif choice == 'о':
            while total(dealer_hand) < 17:
                hit(dealer_hand)
                print(dealer_hand)
                if total(dealer_hand) > 21:
                    print('У раздающего перебор, вы выиграли!')
                    wins += 1
                    play_again()
            score(dealer_hand, player_hand)
            play_again()
        elif choice == "в":
            print("Казино всегда выигрывает!")
            quit = True
            exit()


game()
