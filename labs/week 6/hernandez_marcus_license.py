# Name: Marcus Hernandez
# Assignment: Week 6 Lab (Sequences) PART 1
#
# Grades the 20-question written driver's license exam.
# The correct answers are stored in one list and the student's answers
# go in a second list. The program then compares them and shows the
# number right, the number wrong, pass/fail (15 correct needed to pass),
# and which questions were missed!

def main():
    # answer key, question 1 is at index 0
    correct_answers = ['A', 'C', 'A', 'A', 'D', 'B', 'C', 'A', 'C', 'B',
                       'A', 'D', 'C', 'A', 'D', 'C', 'B', 'B', 'D', 'A']

    # ask for all 20 answers and add each one to the student's list
    # (.upper() so a lowercase "a" still counts as A)
    student_answers = []
    for number in range(1, 21):
        answer = input('Enter your answer for question ' + str(number) + ': ')
        student_answers = student_answers + [answer.upper()]

    # question numbers where the two lists don't match
    # (index + 1 since the questions start at 1, not 0)
    missed = [i + 1 for i in range(20) if student_answers[i] != correct_answers[i]]

    num_incorrect = len(missed)
    num_correct = 20 - num_incorrect

    print('Number of correct answers:', num_correct)
    print('Number of incorrect answers:', num_incorrect)

    if num_correct >= 15:
        print('You passed the test.')
    else:
        print('You did not pass the test.')

    # turn each number into a string so they can be joined with commas
    print('Questions answered incorrectly:', ', '.join([str(q) for q in missed]))

main()