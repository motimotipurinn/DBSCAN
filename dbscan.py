import numpy as np
import matplotlib.pyplot as plt
import time
from sklearn.metrics import silhouette_score
from sklearn import cluster, datasets, mixture
from sklearn.neighbors import kneighbors_graph


def cluster_plots(
    set1, set2, colours1="gray", colours2="gray", title1="Dataset 1", title2="Dataset 2"
):

    fig, (ax1, ax2) = plt.subplots(1, 2)
    fig.set_size_inches(6, 3)

    ax1.set_title(title1, fontsize=14)
    ax1.set_xlim(min(set1[:, 0]), max(set1[:, 0]))
    ax1.set_ylim(min(set1[:, 1]), max(set1[:, 1]))
    ax1.scatter(set1[:, 0], set1[:, 1], s=8, lw=0, c=colours1)

    ax2.set_title(title2, fontsize=14)
    ax2.set_xlim(min(set2[:, 0]), max(set2[:, 0]))
    ax2.set_ylim(min(set2[:, 1]), max(set2[:, 1]))
    ax2.scatter(set2[:, 0], set2[:, 1], s=8, lw=0, c=colours2)

    fig.tight_layout()
    plt.show()


sum2 = 0
with open("bbbb.txt", "r", encoding="utf-8") as fin:  # ファイルを開く
    for line in fin.readlines():  # 行をすべて読み込んで1行ずつfor文で回す
        sum2 += 1
dataset1 = np.zeros((sum2, 2))
dataset2 = np.zeros((sum2, 2))
sums = 0
with open("bbbb.txt", "r", encoding="utf-8") as fin:  # ファイルを開く
    for line in fin.read().splitlines():  # 行をすべて読み込んで1行ずつfor文で回す
        row = []  # 行のデータを保存するリスト
        toks = line.split(" ")  # 行を半角スペースで分割する
        num = float(toks[0])  # 整数に変換
        num2 = float(toks[1])  # 整数に変換
        dataset1[sums][0] = num
        dataset1[sums][1] = num2
        dataset2[sums][0] = num
        dataset2[sums][1] = num2
        sums += 1
start_time = time.time()

dbscan_dataset1 = cluster.DBSCAN(eps=10, min_samples=9, metric="euclidean").fit_predict(
    dataset1
)
dbscan_dataset2 = cluster.DBSCAN(eps=10, min_samples=7, metric="euclidean").fit_predict(
    dataset2
)

# noise points are assigned -1
print("--- %s seconds ---" % (time.time() - start_time))
print("Dataset1:")
print(
    "Number of Noise Points: ",
    sum(dbscan_dataset1 == -1),
    " (",
    len(dbscan_dataset1),
    ")",
    sep="",
)
print("Dataset2:")
print(
    "Number of Noise Points: ",
    sum(dbscan_dataset2 == -1),
    " (",
    len(dbscan_dataset2),
    ")",
    sep="",
)
cluster_plots(dataset1, dataset2)
cluster_plots(dataset1, dataset2, dbscan_dataset1, dbscan_dataset2)
print(dbscan_dataset1)
for i in range(len(dbscan_dataset1)):
    print(dbscan_dataset1[i])
# 参考 https://data-analysis-stats.jp/python/dbscan%E3%82%AF%E3%83%A9%E3%82%B9%E3%82%BF%E3%83%BC%E3%81%AE%E8%A7%A3%E8%AA%AC%E3%81%A8%E5%AE%9F%E9%A8%93/
