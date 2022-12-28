import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
# from matplotlib.font_manager import _rebuild
import shutil

if __name__ == '__main__':
    hdata = pd.read_csv('del_h.csv')
    gdp = pd.read_excel('../data/GDP167.xlsx')
    region = gdp[['country', 'ISO', 'geo', 're']]

    hdata = pd.merge(hdata, region, how='inner', left_on='ISO', right_on='ISO')
    print(hdata)

    data = {
        'NA': hdata.loc[hdata['re'] == 1],
        'EU': hdata.loc[hdata['re'] == 2],
        'EA': hdata.loc[hdata['re'] == 3],
        'ME': hdata.loc[hdata['re'] == 4],
        'SA': hdata.loc[hdata['re'] == 5],
        'LA': hdata.loc[hdata['re'] == 6],
        'SF': hdata.loc[hdata['re'] == 7]
    }
    print(data)

    years = ['2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009',
             '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017']
    NA, EU, EA, ME, SA, LA, SF = list(), list(), list(), list(), list(), list(), list()

    for i in years:
        NA.append(data['NA'][i].mean())
        EU.append(data['EU'][i].mean())
        EA.append(data['EA'][i].mean())
        ME.append(data['ME'][i].mean())
        SA.append(data['SA'][i].mean())
        LA.append(data['LA'][i].mean())
        SF.append(data['SF'][i].mean())
    mean_data = pd.DataFrame([NA, EU, EA, ME, SA, LA, SF])
    mean_data = mean_data.T
    mean_data.rename(columns={0: 'NA', 1: 'EU', 2: 'EA', 3: 'ME', 4: 'SA', 5: 'LA', 6: 'SF'}, inplace=True)
    mean_data.index = years
    print(mean_data)

    # 构造数据
    y1 = list(mean_data.loc['2000', ])
    y2 = list(mean_data.loc['2017', ])
    x = np.arange(len(y1))
    listdata = ['NA', 'EU', 'EA', 'ME', 'SA', 'LA', 'SF']
    # 绘图
    plt.figure(figsize=(7, 5))
    total_width, n = 0.8, 2  # 柱状图总宽度，有几组数据
    width = total_width / n  # 单个柱状图的宽度
    x1 = x - width / 2  # 第一组数据柱状图横坐标起始位置
    x2 = x1 + width
    plt.bar(x=x1, height=y1, width=width, label='2000', color='#245E71')
    plt.bar(x=x2, height=y2, width=width, label='2017', color='#2AA5A1')

    # 添加数据标签
    # for x_value, y_value in zip(x, y1):
    #     plt.text(x=x_value, y=y_value, s=y_value)
    # for x_value, y_value in zip(x, y2):
    #     plt.text(x=x_value + width, y=y_value, s=y_value)
    plt.rcParams["font.sans-serif"] = ["SimSun"]
    plt.rcParams["font.family"] = "sans-serif"
    plt.rcParams["axes.unicode_minus"] = False
    plt.yticks(fontproperties='Times New Roman', size=16)
    plt.xticks(x, listdata, fontproperties='Times New Roman', size=16)
    plt.legend(prop={'family': 'Times New Roman', 'size': 16})
    plt.title('hs-27产品地区平均高度分布', size=16)
    plt.show()
