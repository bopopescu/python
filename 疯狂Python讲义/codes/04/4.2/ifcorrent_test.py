age = 45
if age > 60:
    print("老年人")
# 在原本的if条件中增加了else的隐含条件
elif age > 40 and not (age > 60):
    print("中年人")
# 在原本的if条件中增加了else的隐含条件
elif age > 20 and not (age > 60) and not (age > 40 and not (age > 60)):
    print("年轻人")
