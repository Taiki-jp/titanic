# import numpy as np
# import pandas as pd
# import os
# import sys
from modules.datasets import Dataset
from modules.graph_utils import GraphUtils


def main(train: Dataset, test: Dataset,
         gu: GraphUtils):
    # 訓練データの生存 or 死亡の円グラフの作成
    gu.make_pie(data=train.df["Survived"],
                labels=["Survived", "Died"],
                counterclock=False,
                is_savefig=False)
    # 前処理
    train.preprocessing(case="titanic")
    test.preprocessing(case="titanic")
    return


if __name__ == "__main__":
    # 入力ファイルパスの指定
    train_filepath = "inputs/train.csv"
    test_filepath = "inputs/test.csv"
    # 出力ファイルフォルダの指定
    output_filedir = "outputs"
    train = Dataset(train_filepath)
    test = Dataset(test_filepath)
    GU = GraphUtils(inputdir="inputs", outputdir=output_filedir)
    main(train=train, test=test, gu=GU)
