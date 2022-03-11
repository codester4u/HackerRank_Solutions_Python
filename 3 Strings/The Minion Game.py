def minion_game(string):
    # your code goes here
    vowels = 'AEIOU'
    S_score, K_score = 0, 0
    n = len(string)
    for i in range(n):
        score = n - i
        if string[i] in vowels:
            K_score += score
        else:
            S_score += score
    if S_score == K_score:
        print('Draw')
    if S_score > K_score:
        print('Stuart {}'.format(S_score))
    if S_score < K_score:
        print('Kevin {}'.format(K_score))

