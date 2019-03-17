from phrases import *
from STATIC_VARIABLES import *
from random import randint, shuffle


def main():
    reboot = True
    while reboot:
        counter = 0

        print(GREETING + "\n")
        print(START_MENU)

        choicer = input_variant()

        if (choicer == 1):
            print(R_VARIANT)
            list_of_word = input_part_of_speach()
            amount_of_words = input_amount_of_words()
            if (list_of_word != ERROR and amount_of_words != aOFw):
                for i in range(amount_of_words):
                    word = create_made_a_guess_word_ENG(list_of_word)
                    answer_list = []
                    answer_list.append(word[RUSSIAN])
                    create_answer_list_RUS(answer_list, list_of_word)
                    print_answer_list(answer_list)
                    print(ANSWER_VARIANT)
                    text_answer = answer_list[input_variant() - 1]
                    counter = show_your_choice_RUS(counter, word, text_answer)
                print(counter, " - right answers.\n")
            else:
                print(WRONG)

        elif (choicer == 2):
            print(E_VARIANT)
            list_of_word = input_part_of_speach()
            amount_of_words = input_amount_of_words()
            if (list_of_word != ERROR and amount_of_words != aOFw):
                for i in range(amount_of_words):
                    word = create_made_a_guess_word_RUS(list_of_word)
                    answer_list = []
                    answer_list.append(word[ENGLISH])
                    create_answer_list_ENG(answer_list, list_of_word)
                    print_answer_list(answer_list)
                    print(ANSWER_VARIANT)
                    text_answer = answer_list[input_variant() - 1]
                    counter = show_your_choice_ENG(counter, word, text_answer)
                print(counter, " - right answers.\n")
            else:
                print(WRONG)

        else:
            print(WRONG)

        print(START_OR_STOP)
        reboot = choice_reboot()


def choice_reboot():
    while True:
        reboot = input().lower()
        if reboot == "yes":
            return YES_OR_NO[reboot]
        elif reboot == "no":
            print(PARTING)
            return YES_OR_NO[reboot]
        else:
            print(WRONG)


def print_answer_list(answer_list):
    for j in range(AMOUNT_OF_ANSWER):
        print(str(j + 1) + ") " + answer_list[j])


def create_made_a_guess_word_RUS(list_of_word):
    word = list_of_word[randint(0, len(list_of_word) - 1)]
    print("What does " + word[RUSSIAN].upper() + " mean?")
    return word


def create_made_a_guess_word_ENG(list_of_word):
    word = list_of_word[randint(0, len(list_of_word) - 1)]
    print("What does " + word[ENGLISH].upper() + " mean?")
    return word


def create_answer_list_ENG(answer_list, list_of_word):
    for k in range(AMOUNT_OF_ANSWER - 1):
        answer_list.append(list_of_word[randint(0, len(list_of_word) - 1)][ENGLISH])
    shuffle(answer_list)
    return answer_list


def create_answer_list_RUS(answer_list, list_of_word):
    for k in range(AMOUNT_OF_ANSWER - 1):
        answer_list.append(list_of_word[randint(0, len(list_of_word) - 1)][RUSSIAN])
    shuffle(answer_list)
    return answer_list


def show_your_choice_ENG(counter, word, text_answer):
    if text_answer == word[ENGLISH]:
        print(CONGRATULATION + "\n")
        counter += 1
    else:
        print(LOSS + "\n")
    return counter


def show_your_choice_RUS(counter, word, text_answer):
    if text_answer == word[RUSSIAN]:
        print(CONGRATULATION + "\n")
        counter += 1
    else:
        print(LOSS + "\n")
    return counter


def input_variant():
    while True:
        try:
            variant = int(input())
        except:
            print(WRONG)
        else:
            return variant


def input_amount_of_words():
    print(AMOUNT_MENU)
    choice = input_variant()
    if (choice == 1):
        print(AM_VARIANT1)
        return aOFw[1]
    elif (choice == 2):
        print(AM_VARIANT2)
        return aOFw[2]
    elif (choice == 3):
        print(AM_VARIANT3)
        return aOFw[3]
    else:
        print(WRONG)
        return aOFw[0]


def input_part_of_speach():
    print(SP_MENU)
    choicer = input_variant()
    if (choicer == 1):
        print(SP_VARIAN1)
        return NOUN
    elif (choicer == 2):
        print(SP_VARIAN2)
        return VERB
    elif (choicer == 3):
        print(SP_VARIAN3)
        return OTHER
    else:
        print(WRONG)
        return ERROR


if __name__ == '__main__':
    main()
