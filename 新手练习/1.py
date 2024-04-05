def get_max_score(sore_dic):
    max_score = 0
    max_score_course = ''
    for course, score in sore_dic.items():
        if score > max_score:
            max_score = score
            max_score_course = course
    return max_score_course, max_score


dic = {'语文': 65, '英语': 88, '数学': 99}
print(get_max_score(dic))
