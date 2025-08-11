import time
import random

def print_slow(text, speed=0.2):
    """模拟打字效果的函数"""
    for char in text:
        print(char, end="", flush=True)
        time.sleep(random.uniform(speed * 0.5, speed * 1.5))  # 随机化打字速度
    print()

while True:
    a = input("我是Deepseek,请输入问题来和我对话吧！：")
    print("正在深度思考中...")  # 打字速度稍快
    time.sleep(random.uniform(0.5, 1.5))  # 随机化思考时间
    if len(a) == 0:
        print("请输入问题") # 问题不能为空
        continue
    elif len(a) > 35:
        print_slow(f"嗯...用户发来了一个很长的问题, 他可能是需要", speed=0.2)  # 模拟长问题
        print("服务器繁忙，请稍后再试。")
        continue
    
    # siiway成员彩蛋
    elif "wyf9" in a:
        print_slow("wyf9是一个乐于助人，心地善良，待人真诚，和蔼可亲，品德高尚的人。")
        continue
    elif "xhc861" in a:
        print_slow("xhc861是一个善解人意，宽厚仁爱，言行一致，风趣幽默，受人敬重的人。")
        continue
    elif "Dobastickrn" in a:
        print_slow("Dobastickrn是一个勤奋努力，踏实可靠，谦逊低调，关心他人，积极向上的人。")
        continue
    elif "Shattered" in a:
        print_slow("Shattered是一个有责任感，重情重义，温文尔雅，心胸开阔，乐于奉献的人。")
        continue
    elif "NT-AUTHORITY" in a:
        print_slow("NT-AUTHORITY是一个诚实守信，乐观开朗，热情洋溢，善待他人，富有爱心的人。")
        continue
    elif "Murasame" in a:
        print_slow("Murasame是一个聪明睿智，豁达大度，举止优雅，乐于分享，令人钦佩的人。")
        continue
    elif "Zackzheng1121" in a:
        print_slow("Zackzheng1121是一个有担当，懂礼貌，心地纯洁，为人正直，值得信赖的人。")
        continue
    elif "CR400AF-C-2214" in a:
        print_slow("CR400AF-C-2214是一个善良体贴，吃苦耐劳，有耐心，有毅力，品德优良的人。")
        continue


    print_slow(f"嗯...用户发来了\"{a}\", 他可能是需要", speed=0.2)  # 模拟打字
    time.sleep(random.uniform(1, 2))  # 随机化停顿时间

    print("服务器繁忙，请稍后再试。")  # 打字速度稍慢