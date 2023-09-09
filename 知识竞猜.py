def check_gues(guess,anwser):
    global score 
    if guess==anwser:
        print('对')
        score =score+1
    else:
        print('错')
score = 0
print('知识竞猜！')
guess1 = input('什么熊生活在北极？')
check_gues(guess1,'北极熊')
guess2 = input('珠穆朗玛峰是世界第几高峰?')
check_gues(guess2,'第一')
print('your score is'+str(score))