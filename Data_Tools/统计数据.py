
import pandas as pd

def count_excel_field(file_name, column_name):
    try:
        # 1. 读取 Excel 文件
        # 如果你的文件在其他文件夹，请写完整路径，如 r"D:\data\test.xlsx"
        df = pd.read_excel(file_name)

        # 2. 检查字段是否存在
        if column_name not in df.columns:
            print(f"❌ 错误：表格中没有找到 '{column_name}' 这一列")
            print(f"当前的列名有: {list(df.columns)}")
            return

        # 3. 统计该字段下每个值的出现次数
        stats = df[column_name].value_counts()

        print(f"统计结果【字段：{column_name}】:")
        print("-" * 30)
        print(stats)
        print("-" * 30)
        
        # 4. 获取总数（不含空值）
        total_count = df[column_name].count()
        # 获取去重后的值个数
        unique_count = df[column_name].nunique()
        
        print(f"该列总数据量: {total_count} 条")
        print(f"不同值的个数（去重）: {unique_count} 个")

    except Exception as e:
        print(f"发生错误: {e}")

# --- 调用演示 ---
# 假设你刚刚生成的 Excel 叫 "我的测试数据.xlsx"
# 我们统计“状态”这一列
count_excel_field("订单信息导出.xlsx", "门店编码")