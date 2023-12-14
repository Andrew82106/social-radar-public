import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from matplotlib.dates import AutoDateLocator, AutoDateFormatter
import pandas as pd
import pprint


def plot_time_series(data_dict, save=None, title='Time Series Data'):
    # 生成日期范围
    dates = sorted(data_dict.keys(), key=lambda x: datetime.strptime(x, "%Y-%m-%d"))

    # 对存在的日期进行处理
    for i, date in enumerate(dates):
        current_date = datetime.strptime(date, "%Y-%m-%d")

        previous_date = current_date - timedelta(days=1)
        previous_date_str = datetime.strftime(previous_date, "%Y-%m-%d")
        if previous_date_str not in data_dict:
            data_dict[previous_date_str] = 0

        next_date = current_date + timedelta(days=1)
        next_date_str = datetime.strftime(next_date, "%Y-%m-%d")
        if next_date_str not in data_dict:
            data_dict[next_date_str] = 0

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
        "2023-11-01": 10,
        "2023-11-02": 15,
        "2023-11-03": 15,
        "2023-11-04": 15,
        "2023-11-05": 15,
        "2023-11-06": 154,
        "2023-11-07": 15,
        "2022-11-10": 130,
    }  # 可以尝试添加更多日期数据进行测试

    # 调用函数绘制折线图
    plot_time_series(data)
