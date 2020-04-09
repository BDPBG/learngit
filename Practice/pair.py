man_age = int(input('男生年龄：'))
man_height = int(input('男生身高：'))
man_weight = int(input('男生体重(公斤)：'))
man_income = int(input('男生收入：'))

woman_age = int(input('女生年龄：'))
woman_height = int(input('女生身高：'))
woman_weight = int(input('女生体重(公斤)：'))
woman_income = int(input('女生收入：'))

if (20 <= woman_age <= 28) and (160 <= woman_height <= 175) and (40 <= woman_weight <= 60) and (
        3000 <= woman_income <= 5000):
    # 在女生符合男生要求的前提下，判断男生是否符合女生的要求
    if (20 <= man_age <= 25) and (170 <= man_height <= 180) and (70 <= man_weight <= 80) and (man_income >= 10000):
        # 假如女生也符合男生的要求
        print('男女配对成功')
    else:
        print('男生不符合女生的要求')
else:
    print('女生不符合男生的要求')
