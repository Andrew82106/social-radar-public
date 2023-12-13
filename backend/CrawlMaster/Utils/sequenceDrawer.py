import matplotlib.pyplot as plt
from datetime import datetime
from matplotlib.dates import AutoDateLocator, AutoDateFormatter
import pandas as pd
import pprint


def plot_time_series(data_dict, save=None, title='Time Series Data'):
    # 生成日期范围
    start_date = min(data_dict.keys())
    end_date = max(data_dict.keys())
    date_range = []
    for date in pd.date_range(start_date, end_date):
        date_range.append(datetime.strftime(date, "%Y-%m-%d"))

    # 补充不存在的日期对应的值为0
    for date in date_range:
        if date not in data_dict:
            data_dict[date] = 0
    pprint.pprint(data_dict)

    # 将字典按照日期排序
    sorted_data = sorted(data_dict.items(), key=lambda x: datetime.strptime(x[0], "%Y-%m-%d"))
    sorted_dates = [datetime.strptime(date, "%Y-%m-%d") for date, _ in sorted_data]
    sorted_values = [value for _, value in sorted_data]

    # 绘制折线图
    plt.figure(figsize=(10, 6))  # 调整图形尺寸
    plt.plot(sorted_dates, sorted_values)

    # 设置图形标题和标签
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Values')

    # 自动调整日期刻度和标签
    locator = AutoDateLocator(maxticks=20)  # 最多显示15个刻度
    formatter = AutoDateFormatter(locator)
    plt.gca().xaxis.set_major_locator(locator)
    plt.gca().xaxis.set_major_formatter(formatter)
    plt.xticks(rotation=45)  # 旋转日期标签，使其更易读

    # 显示图例和网格线
    plt.legend(['Values'], loc='upper left')
    plt.grid(True)

    # 判断是否保存图形
    if save and isinstance(save, str):
        plt.savefig(save)  # 保存图形，以 save 参数的值作为文件名
        print(f"Figure saved as {save}")
    else:
        plt.show()  # 展示图形

    plt.tight_layout()


if __name__ == '__main__':
    # 示例字典
    data = {
        "2023-11-1": 10,
        "2023-11-2": 15,
        "2023-11-3": 15,
        "2023-11-4": 15,
        "2023-11-5": 15,
        "2023-11-6": 154,
        "2023-11-7": 15,
        "2022-11-10": 130,
        "2022-11-11": 135,
        "2022-11-8": 120,
        "2022-11-9": 10,
    }  # 可以尝试添加更多日期数据进行测试

    # 调用函数绘制折线图
    plot_time_series(data)
