bookName = "疯狂Python"
price = 79
version = "正式版"
if bookName.endswith('Python') and (price < 50 or version == "正式版"):
    print("打算购买这本Python图书")
else:
    print("不购买!")
