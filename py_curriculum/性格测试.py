def question_1():
    sum = 0
    print("一、你走路的时候：")
    print("A、大步地快走")
    print("B、小步地快走")
    print("C、不快，仰着头走路")
    print("D、不快低着头走路")
    answer = str(input("请输入你的选择：")).upper()
    if answer == "A":
        sum += 6
    if answer == "B":
        sum += 4
    if answer == "C":
        sum += 7
    if answer == "D":
        sum += 2
    return sum


def question_2():
    sum = 0
    print("二、和别人交谈的时候")
    print("A、手臂交叠站着")
    print("B、双手紧握着")
    print("C、一只手或者两只手放在臀部")
    print("D、喷着或推着和你说话的人")
    answer = str(input("请输入你的选择：")).upper()
    if answer == "A":
        sum += 4
    if answer == "B":
        sum += 2
    if answer == "C":
        sum += 5
    if answer == "D":
        sum += 7
    return sum


def question_3():
    sum = 0
    print("三、坐着休息时候，你的习惯是：")
    print("A、两膝盖并拢")
    print("B、两腿交叉")
    print("C、两腿伸直")
    print("D、一腿蜷在身下")
    answer = str(input("请输入你的选择：")).upper()
    if answer == "A":
        sum += 4
    if answer == "B":
        sum += 6
    if answer == "C":
        sum += 2
    if answer == "D":
        sum += 1
    return sum


def question_4():
    sum = 0
    print("四、临睡前的几分钟，你在床上的姿势是：")
    print("A、仰躺，身体伸直")
    print("B、俯躺，身体伸直")
    print("C、侧躺，身体微蜷")
    print("D、蒙头盖脸")
    answer = str(input("请输入你的选择：")).upper()
    if answer == "A":
        sum += 7
    if answer == "B":
        sum += 6
    if answer == "C":
        sum += 4
    if answer == "D":
        sum += 2
    return sum


if __name__ == '__main__':
    print("测试你是什么样的人，请完成以下题目")
    score = 0
    score += question_1()
    score += question_2()
    score += question_3()
    score += question_4()
    print("结果分析：")
    if score <= 11:
        print("内向的悲观者。你在别人眼中是一个害羞的，神经质的、优柔寡断的，需要别人帮助，做任何的决定都需要别人帮你。别人认为你是一个杞人忧天者，一个永远只会看到问题存在的人。")
    elif score <= 18 and score >= 12:
        print(
            "缺乏自信的挑战者。你在别人眼中是一个勤勉刻苦、很挑剔的人。他们认为你是一个谨慎的，十分小心的而稳定辛勤工作的人。如果你做任何冲动的事或者毫无准备的事，你会令他们大吃一惊的。他们认为你会从各个方面、各个角度考察过一切之后还是经常决定不做某件事。")
    elif score <= 23 and score >= 19:
        print(
            "以牙还牙的自我保护者。你在别人眼中是一个明智、谨慎、注重实效的人。他们认为你是一个伶俐，有才且谦虚的人。你不会很快和别人成为朋友，但是一旦成为朋友你对你的朋友会很忠诚，同时也会要求你的朋友对你忠诚。那些真正有机会了解你的人会知道要动摇你对朋友的信任是很艰难的。")
    elif score >= 23:
        print("傲慢的孤独者。你在别人眼中是个自负的，以自我为重心的、有极端支配欲和统治欲的人。别人可能会钦佩你，希望能多像你一点，但是接触久了不会一直相信你，不会和你有更深的接触和来往。")
