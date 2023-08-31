# Questioner, enter an word in line 25
stage = [
    '===============================',
    '|_________',
    '|         ',
    '|         ',
    '|         ',
    '|         ',
    '|         ',
    '==============================='
]

hangman_diagram = [
    '|_________',
    '|    |    ',
    '|    O    ',
    '|    |    ',
    '|   /|    ',
    '|   /|\   ',
    '|   /     ',
    '|   / \   '
]

# the answer
answer = 'apple'

# word is to check the answer, apple => ['a', 'p', 'p', 'l', 'e']
word = list(answer)

# To show the blank of the answer, apple => _ _ _ _ _
def answer_blank_space(word):
    blank_space = []
    for i in range(len(word)):
        blank_space.append('_')
    return blank_space

# hangman, when answer is wrong
def hangman(wrong_check):
    if wrong_check == 0:
        return stage
    elif wrong_check == 1:
        stage[2] = hangman_diagram[1]
        return stage
    elif wrong_check == 2:
        stage[3] = hangman_diagram[2]
        return stage
    elif wrong_check == 3:
        stage[4] = hangman_diagram[3]
        return stage
    elif wrong_check == 4:
        stage[4] = hangman_diagram[4]
        return stage
    elif wrong_check == 5:
        stage[4] = hangman_diagram[5]
        return stage
    elif wrong_check == 6:
        stage[5] = hangman_diagram[6]
        return stage
    elif wrong_check == 7:
        stage[5] = hangman_diagram[7]
        return stage

def drawing_hangman(blank_space, wrong_letter = []):
    for i in range(len(stage)):
        if i == 1:
            print(stage[i] + '     Guess a letter')
        elif i == 2:
            if len(wrong_letter) == 0:
                print(stage[i])
            else:
                print(stage[i] + '     wrong letter: {}'.format(', '.join(wrong_letter)))  # 10 spaces
        elif i == 4:
            print(stage[i] + '     {}'.format(' '.join(blank_space)))
        else:
            print(stage[i])

# Game start
wrong_check = 0
check = 0
blank_space = answer_blank_space(word)
drawing_hangman(blank_space)
wrong_letter = []
while wrong_check < 7:  # 7 means the hangman is drawn completely, the answerer loses.
    answer_character = input()
    if answer_character in word:
        # replace the letter of answer
        index = word.index(answer_character)
        # To prevent the answer has same letter, like apple
        word[index] = '@' 
        blank_space[index] = answer_character
        drawing_hangman(blank_space, wrong_letter)
        check += 1
    else: 
        wrong_check += 1
        wrong_letter.append(answer_character)
        hangman(wrong_check)  # return stage
        drawing_hangman(blank_space, wrong_letter)
    if check == len(word):
        print('Awesome, You win!\n')
        break
    if wrong_check == 7:
        print('Sorry, you lose.\nThe answer is "{}".\n'.format(answer))
        break