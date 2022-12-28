import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
# from matplotlib.font_manager import _rebuild
import shutil
import seaborn as sns

if __name__ == '__main__':
    year = 2000
    data = pd.read_csv('cat_num.csv', index_col=0)
    for i in range(18):
        a = pd.cut(data[str(year)+'_cat1'], [0, 30, 60, 90, 120, 150, 170],
                   labels=[u"(0,30]", u"(30,60]", u"(60,90]", u"(90,120]", u"(120,150]", u"(150, 170]"])
        b = a.value_counts()
        b = b.sort_index()
        c = {'section': b.index, 'frequency': b.values}
        e = pd.DataFrame(c)

        plt.rcParams["font.sans-serif"] = ["SimSun"]
        plt.rcParams["font.family"] = "sans-serif"
        plt.rcParams["axes.unicode_minus"] = False

        ax = plt.figure(figsize=(7, 5)).add_subplot(111)
        sns.barplot(x="section", y="frequency", data=e, color='silver') #palette设置颜色
        # ax.set_ylim([0, 30])
        ax.set_xlabel('区间', fontsize=14)
        ax.set_ylabel('频数', fontsize=14)
        ax.set_title(str(year) + '频数分布图', size=20)
        plt.xticks(fontsize=12)
        plt.yticks(fontsize=12)
        plt.savefig('分年频数分布图/'+str(year))
        # plt.show()
        year = year + 1
