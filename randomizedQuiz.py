#! python3

#This is the randomized geography quiz script
#This creates 35 quizzes with 50 questions: 1 correct and 3 wrong answers each.
#The order of questions as well as the answers are randomized.
#There should be 35 quiz text files and 35 answer key text files.

import random

capitols = {'Alabama': 'Montgomary', 'Alaska': 'Juneau', 'Arizona': 'Pheonix',
           'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
           'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
           'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise',
           'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines',
           'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge',
           'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston',
           'Michigan': 'Lansing', 'Minnisota': 'Saint Paul', 'Mississippi': 'Jackson',
           'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln',
           'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
           'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
           'North Dakota': 'Bismark', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
           'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
           'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennesse': 'Nashville',
           'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Monteplier',
           'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston',
           'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}


for quizNum in range(35):
    quizFile = open(f'./quizzes/capitalquiz{quizNum + 1}.txt', 'w')
    answerFile = open(f'./answers/capitalquizAnswers{quizNum + 1}.txt', 'w')

    quizFile.write('Name: \nDate: \nPeriod:\n\n')
    quizFile.write((' '*20 )+f'State Capital Quiz (Form {quizNum + 1})')
    quizFile.write('\n\n\n')

    states = list(capitols.keys())
    random.shuffle(states)

    for i in range(50):
        answers = []
        answers.append(capitols[states[i]])

        while True:
            random_answer = random.randint(0,49)
            if capitols[states[random_answer]] not in answers:
                answers.append(capitols[states[random_answer]])

            if len(answers)==4: break

        random.shuffle(answers)

        if answers[0]==capitols[states[i]]:
            answerFile.write(f'Q{i+1}: A\n')
        elif answers[1]==capitols[states[i]]:
            answerFile.write(f'Q{i+1}: B\n')
        elif answers[2]==capitols[states[i]]:
            answerFile.write(f'Q{i+1}: C\n')
        elif answers[3]==capitols[states[i]]:
            answerFile.write(f'Q{i+1}: D\n')

        quizFile.write(f'Question #{i+1}: ')
        quizFile.write(f'What is the capitol of {states[i]}? \n')
        quizFile.write(f'A: {answers[0]}\n')
        quizFile.write(f'B: {answers[1]}\n')
        quizFile.write(f'C: {answers[2]}\n')
        quizFile.write(f'D: {answers[3]}\n')
        quizFile.write(f'\n\n')

    answerFile.close()
    quizFile.close()
