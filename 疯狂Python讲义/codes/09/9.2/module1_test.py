# 两次导入module1，并指定别名为md
import module1 as md
import module1 as md

print(md.my_book)
print(md.say_hi('Charlie'))
user = md.User('孙悟空')
print(user)
user.walk()
