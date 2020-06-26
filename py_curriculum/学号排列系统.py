from xpinyin import Pinyin  # 需要xpinyin模块


def sortFunction(lis):  # 对名字进行排序
    pin = Pinyin()
    result = []
    for item in lis:
        result.append((pin.get_pinyin(item), item))
    result.sort()
    tempLength = len(result)
    for i in range(tempLength):
        result[i] = result[i][1]
    print("排序完成！")
    return result


if __name__ == '__main__':
    name_dict = dict()
    name_list = list()
    i = 1
    print("请依次输入学生姓名，输入0结束！")
    while True:
        name = input("请输入第%s个名字：" % (i))
        i += 1
        if name == "0":
            print("名字录入已结束！")
            break;
        else:
            name_list.append(name)
    name_list = sortFunction(name_list)
    tempLength = len(name_list)
    print("录入完成，结果如下：")
    for i in range(tempLength):
        name_dict[i + 1] = name_list[i]
    print("%5s%9s" % ("学号", "姓名"))
    for key in name_dict:
        print("%5d%10s" % (key, name_dict[key]))
