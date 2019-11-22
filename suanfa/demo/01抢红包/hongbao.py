# --coding:utf-8--
import random

"""
注意：以下金额统一单位：分
"""


def isright(rest_money, rest_redenvelope_count, minmoney, maxmoney):
    """砍价的合法性校验"""
    # 合法性状态
    flag = True
    avg = rest_money / rest_redenvelope_count
    # 小于最小金额
    if avg < minmoney:
        flag = False
    elif avg > maxmoney:
        flag = False
    return flag


def random_redenvelope(rest_money, rest_redenvelope_count, minmoney, maxmoney):
    """随机分配一个金额"""
    # 如果只有一个红包，直接返回金额
    if rest_redenvelope_count == 1:
        return rest_money
    # 如果最大金额和最小金额相等，则直接返回金额
    if minmoney == maxmoney:
        return minmoney
    # 允许砍价的最大值
    max = rest_money - (rest_redenvelope_count - 1) * minmoney
    # 允许砍价的最小值
    min = rest_money - (rest_redenvelope_count - 1) * maxmoney
    if max < maxmoney:
        maxmoney = max
    if min > minmoney:
        minmoney = min
    return random.randint(minmoney, maxmoney)


def redenvelopelist(total_redenvelope, redenvelope_count, minmoney, maxmoney):
    """抢红包金额列表"""
    # 抢红包列表
    list = []
    # 累计红包金额
    sum = 0
    if not isright(total_redenvelope, redenvelope_count, minmoney, maxmoney):
        return redenvelopelist
    for i in range(redenvelope_count):
        random_money = random_redenvelope(total_redenvelope, redenvelope_count, minmoney, maxmoney)
        total_redenvelope -= random_money
        redenvelope_count -= 1
        list.append(random_money / 100)
        sum += random_money
    # print("sum = {}".format(sum))
    return list


for i in range(10):
    print("redenvelopelist = {}".format(redenvelopelist(10000, 10, 100, 10000)))
