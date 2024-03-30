#Taking a month to have 30 days on average, this function returns a value of total cards you have studied using Anki, using the following rule: 1st month: 180 cards; 2nd month: 180+60; 3rd month: 180+120; ...
def  anki_sum(n):
    amount_per_month = []
    for n in range(-1,n):
        formula = (180*(n+1) +60*((n*(n+1))/2))
    amount_per_month.append(formula)
    language = input('Choose your language: ')
    print(f'After {n} months of studying {language} using Anki, you will have approximately {int(formula)} cards on total.')
    print(f'Number of daily Anki cards up to this point: {6 + n*2}')
anki_sum(int(input('n: ')))