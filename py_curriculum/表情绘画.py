from emoji import emojize

if __name__ == '__main__':
    while True:
        people = {"1": ":scream:",
                  "2": ":relieved:",
                  "3": ":no_mouth:",
                  "4": ":smile:"}
        nature = {"1": ":tiger:",
                  "2": ":koala:",
                  "3": ":sunny:",
                  "4": ":snowflake:"}
        objects = {"1": ":balloon:",
                   "2": ":gift_heart:",
                   "3": ":christmas_tree:",
                   "4": ":crystal_ball:"}
        print("表情种类如下：")
        print("1>>>People")
        print("2>>>Nature")
        print("3>>>Objects")
        inp = int(input("请输入需要的种类"))
        if inp == 1:
            print("People类表情如下：")
            print(people)
            inp = input("请输入需要的表情：")
            print(emojize(people[inp], use_aliases=True))
        elif inp == 2:
            print("Nature类表情如下：")
            print(people)
            inp = input("请输入需要的表情：")
            print(emojize(nature[inp], use_aliases=True))
        elif inp == 3:
            print("Objects类表情如下：")
            print(people)
            inp = input("请输入需要的表情：")
            print(emojize(objects[inp], use_aliases=True))
        else:
            print("请输入正确的序号")
