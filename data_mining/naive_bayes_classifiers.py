#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def classifier(testdata: dict, pdict: dict):
    outlook = 'outlook=' + testdata["outlook"]
    temp = 'temp=' + testdata["temp"]
    humidity = 'humidity=' + testdata["humidity"]
    windy = 'windy=' + str(testdata['windy']).lower()
    total_times = pdict['play_times'] + pdict['not_play_times']
    p_play = pdict['play_times'] / total_times
    p_not_play = pdict['not_play_times'] / total_times

    p_yes = pdict[outlook + '|true'] * \
            pdict[temp + '|true'] * \
            pdict[humidity + '|true'] * \
            pdict[windy + '|true'] * \
            p_play

    p_no = pdict[outlook + '|false'] * \
           pdict[temp + '|false'] * \
           pdict[humidity + '|false'] * \
           pdict[windy + '|false'] * \
           p_not_play

    # print(p_yes)
    # print(p_no)

    if p_yes > p_no:
        return True
    else:
        return False


if __name__ == '__main__':
    data_list = [
        {"outlook": 'sunny', "temp": 'hot', "humidity": 'high', "windy": False, "play": False},
        {"outlook": 'sunny', "temp": 'hot', "humidity": 'high', "windy": True, "play": False},
        {"outlook": 'overcast', "temp": 'hot', "humidity": 'high', "windy": False, "play": True},
        {"outlook": 'rainy', "temp": 'mid', "humidity": 'high', "windy": False, "play": True},
        {"outlook": 'rainy', "temp": 'cool', "humidity": 'normal', "windy": False, "play": True},
        {"outlook": 'rainy', "temp": 'cool', "humidity": 'normal', "windy": True, "play": False},
        {"outlook": 'overcast', "temp": 'cool', "humidity": 'normal', "windy": True, "play": True},
        {"outlook": 'sunny', "temp": 'mid', "humidity": 'high', "windy": False, "play": False},
        {"outlook": 'sunny', "temp": 'cool', "humidity": 'normal', "windy": False, "play": True},
        {"outlook": 'rainy', "temp": 'mid', "humidity": 'normal', "windy": False, "play": True},
        {"outlook": 'sunny', "temp": 'mid', "humidity": 'normal', "windy": True, "play": True},
        {"outlook": 'overcast', "temp": 'mid', "humidity": 'high', "windy": True, "play": True},
        {"outlook": 'overcast', "temp": 'hot', "humidity": 'normal', "windy": False, "play": True},
        {"outlook": 'rainy', "temp": 'mid', "humidity": 'high', "windy": True, "play": False}
    ]

    # 计算各种条件概率
    p = dict()
    # 创建键值对并赋初值0
    for data in data_list:
        for k, v in data.items():
            if not k == 'play':
                p['' + k + '=' + str(v).lower() + '|' + 'false'] = 0.0
                p['' + k + '=' + str(v).lower() + '|' + 'true'] = 0.0

    # 统计频数
    for data in data_list:
        # outlook:sunny
        if data["outlook"] == "sunny":
            if not data["play"]:
                p["outlook=sunny|false"] += 1
            if data["play"]:
                p["outlook=sunny|true"] += 1

        # outlook:rainy
        if data["outlook"] == "rainy":
            if not data["play"]:
                p["outlook=rainy|false"] += 1
            if data["play"]:
                p["outlook=rainy|true"] += 1

        # outlook:overcast
        if data["outlook"] == "overcast":
            if not data["play"]:
                p["outlook=overcast|false"] += 1
            if data["play"]:
                p["outlook=overcast|true"] += 1

        # temp:hot
        if data["temp"] == "hot":
            if not data["play"]:
                p["temp=hot|false"] += 1
            if data["play"]:
                p["temp=hot|true"] += 1

        # temp:mid
        if data["temp"] == "mid":
            if not data["play"]:
                p["temp=mid|false"] += 1
            if data["play"]:
                p["temp=mid|true"] += 1

        # temp:cool
        if data["temp"] == "cool":
            if not data["play"]:
                p["temp=cool|false"] += 1
            if data["play"]:
                p["temp=cool|true"] += 1

        # humidity:high
        if data["humidity"] == "high":
            if not data["play"]:
                p["humidity=high|false"] += 1
            if data["play"]:
                p["humidity=high|true"] += 1

        # humidity:normal
        if data["humidity"] == "normal":
            if not data["play"]:
                p["humidity=normal|false"] += 1
            if data["play"]:
                p["humidity=normal|true"] += 1

        # windy:no
        if not data["windy"]:
            if not data["play"]:
                p["windy=false|false"] += 1
            if data["play"]:
                p["windy=false|true"] += 1

        # windy:yes
        if data["windy"]:
            if not data["play"]:
                p["windy=true|false"] += 1
            if data["play"]:
                p["windy=true|true"] += 1

        if data["play"]:
            p["play_times"] = p.get("play_times", 0) + 1
        else:
            p["not_play_times"] = p.get("not_play_times", 0) + 1

    for k in p.keys():
        if k == 'play':
            continue
        if k[-5::] == 'false':
            p[str(k)] /= p["not_play_times"]
        elif k[-4::] == 'true':
            p[str(k)] /= p["play_times"]

    for item in p.items():
        print(item)

    today = {"outlook": 'sunny', "temp": 'hot', "humidity": 'normal', "windy": False, "play": False}
    print(classifier(today, p))
