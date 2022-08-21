#生成一个随机的uuid
import random
import uuid
nums=input("请输入生成的uuid个数：")
nums=int(nums)
for i in range(nums):
    print(uuid.uuid5(uuid.NAMESPACE_DNS, str(random.randint(0, 100))))