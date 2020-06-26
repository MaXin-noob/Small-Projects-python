carNum = {
    "冀A": "河北省石家庄市",
    "冀B": "河北省唐山市",
    "冀C": "河北省秦皇岛市",
    "冀D": "河北省邯郸市",
    "冀E": "河北省刑台市",
    "冀F": "河北省保定市",
    "冀G": "河北省张家口市",
    "冀H": "河北省承德市",
    "冀J": "河北省沧州市",
    "冀R": "河北省廊坊市",
    "冀T": "河北省衡水市",
    "吉A": "吉林省长春市",
    "吉B": "吉林省吉林市",
    "吉C": "吉林省四平市",
    "吉D": "吉林省辽源市",
    "吉E": "吉林省通化市",
    "吉F": "吉林省白山市",
    "吉J": "吉林省松原市",
    "吉G": "吉林省白城市",
    "吉H": "吉林省延边州",
}

if __name__ == '__main__':
    while True:
        inp = input("请输入要查找的车牌号(输入0时结束输入)：")
        num = inp[0:2]
        res = carNum.get(num)
        if num == "0":
            print("本次查询记录已写入文件")
            break
        else:
            if res is not None:
                print("成功查询到您输入的车牌号")
                str_ = "您输入的车牌号 %s 属于 %s " % (inp, res)
                print(str_)
                f = open("./record.txt", mode="a+", encoding="utf-8")
                context = str_ + "\n"
                f.write(context)
                f.close()
            else:
                print("您输入的车牌号没有在数据库中找到，请重试!")
