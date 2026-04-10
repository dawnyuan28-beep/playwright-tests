import pandas as pd  # 导入处理表格的库
import random

# 1. 准备一个空的列表来存数据
data_list = []

# 2. 循环 50 次，生成 50 条数据
for i in range(1, 51):
    username = f"test_user_{i:03d}"  # 生成 test_user_001 这种格式
    phone = "138" + "".join(random.choices("0123456789", k=8))
    data_list.append({"用户名": username, "手机号": phone, "状态": "待激活"})

# 3. 把数据塞进“表格对象”并保存
df = pd.DataFrame(data_list)
df.to_excel("我的测试数据.xlsx", index=False)

print("✅ 任务完成！'我的测试数据.xlsx' 已生成在当前文件夹。")