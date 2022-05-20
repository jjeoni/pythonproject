import func_basic1 as fb1

word = ['cat', 'dog', 'fox', 'monkey', 'mouse', 'panda', 'frog', 'snake', 'wolf']
rank = {'aaa':10.123}

word = fb1.load_save_data('word.json', 'r')
rank = fb1.load_save_data('rank.json', 'r')

while True:
    menu = input('''
    ---------------------------------------------
    1. 문제추가 2.타자게임 3.등수리스트 4.종료하기
    ---------------------------------------------
    번호 입력 : ''')
    
    if menu == '1':
        fb1.quiz_input(word)
        fb1.load_save_data('word.json', 'w', word)
        
    elif menu == '2':
        fb1.game(word, rank)
        
    elif menu == '3':
        fb1.rank_list(rank)

    elif menu == '4':
        print('종료하기')
        fb1.load_save_data('rank.json', 'w', rank)
        break
        
    else:
        print('잘못 입력하였습니다.')
    