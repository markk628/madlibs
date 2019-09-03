#got the madlib from here -> https://www.woojr.com/mad-libs-worksheets/back-to-school-mad-libs/
def madlibs():
    adj1 = input("Enter an adjective: ")
    noun1 = input("Enter a noun: ")
    noun2 = input("Enter another noun: ")
    verb1 = input("Enter a verb: ")
    noun3 = input("Enter another noun:" )
    verb2 = input("Enter another verb: ")
    noun4 = input("Enter another noun: ")
    noun5 = input("Enter a noun (plural): ")
    noun6 = input("Enter a noun (plural): ")
    noun7 = input("Enter another noun: ")
    noun8 = input("Enter another noun: ")
    adj2 = input("Enter another adjective: ")
    noun9 = input("Enter another noun: ")
    noun10 = input("Enter another noun: ")
    emotion = input("Enter an emotion: ")
    number1 = input("Enter a number: ")
    number2 = input("Enter a larger number: ")
    adverb = input("Enter an adverb: ")
    verb3 = input("Enter a past tense verb (-ed): ")
    adj3 = input("Enter another adjective: ")
    pronoun1 = input("Enter a pronoun: ")
    noun11 = input("Enter another noun: ")
    pronoun2 = input("Enter another pronoun: ")

    print(f''' "\033[1;34;40m Lunchtime in our cafeteria is always {adj1}. They serve hot
    {noun1} and {noun2}, but some students {verb1} their own {noun3} to eat.
    Some kids quietly {verb2} their {noun4}, while others throw {noun5} or
    {noun6} when the teachers aren't looking. One time, a bunch of kids mixed
    all of their unfinished {noun7} and {noun8} toghether to make a {adj2}
    mountain of {noun9} on a {noun10}. The teachers were {emotion}. {number1}
    of the {number2} teachers got {adverb} drenched, but the rest were {verb3}.
    Things got so {adj3} that the principal showed up. {pronoun1} stated that
    there will be no recess for a week, and the students replied by throwing a
    load of {noun11} at {pronoun2}.''')

madlibs()
