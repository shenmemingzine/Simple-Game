# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 16:07:15 2017

@author: yu
"""

from Main import *

def playGame(wordList):
    command = input('Press any key to start/e to end the game: ')
    score = 0
    correct = 0
    incorrect_attempt = []
    while command != 'e':
        word = getWord(wordList)
        answer = word[0]
        meaning = word[1]
        test = deleteLetters(answer)
        print(meaning)
        attempt = input('Enter your answer: ')
        if isMatch(answer, attempt):
            score += 10
            correct += 1
            print('This is correct! Total number of correct words:', correct)
            print('Your score is', score)
            wordList.pop(answer, None)
            if len(wordList) == 0:
                print('You got all words!')
                command = 'e'
        elif not isMatch(answer, attempt):
            score -= 1
            print('This is incorrect! The correct answer is', answer)
            print('Your score is', score)
            incorrect_attempt.append(answer)
        command = input('Press any key to continue/e to end the game: ')
     
    print('Want to review?')
    re_command = input('y for review section; otherwise, stop: ')
    if re_command == 'y':
        print('Starting review section...')
        while len(incorrect_attempt) != 0:
            re_section = review(incorrect_attempt, wordList)
            incorrect_attempt = re_section
        print('Finish!')
    else:
        print('Game Over!')
        
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)