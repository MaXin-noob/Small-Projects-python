import random

item = 0
scoreSum = 0
score = list()
score_ = list()
result = list()
random.seed(0)
if __name__ == '__main__':
    for i in range(0, 10):
        ran = random.randint(1, 100)
        score.append(ran)
    print("裁判打分结果是:", end="")
    print(score)
    score_ = score.copy()
    score_max = max(score)
    score_min = min(score)
    print("其中最高分是%d分" % score_max)
    print("其中最低分是%d分" % score_min)
    score.remove(score_max)
    score.remove(score_min)
    for i in score:
        item += i
        scoreSum = int(item / 8)
    print("该选手的平均分是：%d分" % scoreSum)
    for i in score_:
        ran = abs(i - scoreSum)
        result.append(ran)
    first = abs(min(result) - scoreSum)
    second = abs(max(result) - scoreSum)
    print("其中最公平的裁判打分为：%d分" % first)
    print("其中最不公平的裁判打分为：%d分" % second)
