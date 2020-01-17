import random
import collections

# 指定随机抽取6个元素，各元素被抽取的权重（概率）不同
print(random.choices(['Python', 'Swift', 'Kotlin'], [5, 5, 1], k=6))
# 下面模拟从52张扑克中随机抽取20张
# 在被抽到的20张牌中，牌面为10（包括J、Q、K）的牌占多大比例
# 生成一个16个tens（代表10）和36个low_cards（代表其他牌）的集合
deck = collections.Counter(tens=16, low_cards=36)
# 从52张牌中随机抽取20张
seen = random.sample(list(deck.elements()), k=20)
# 统计tens元素有多少个，再除以20
print(seen.count('tens') / 20)
