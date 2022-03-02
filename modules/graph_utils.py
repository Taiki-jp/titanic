from typing import List, Union
import numpy as np
import pandas as pd
import os
import sys
import seaborn as sns
import matplotlib.pyplot as plt
# NOTE: インタラクティブウィンドウでは実行ファイルと同じ階層にあるファイルを簡単にインポートできる
# NOTE: mainを通して本ファイルをインポートした場合はModuleNotFoundErrorになる
# from datasets import Dataset

# 可視化のためのグラフ作成関数をまとめたクラス
class GraphUtils():
    def __init__(self, inputdir: str,
                 outputdir: str) -> None:
        self.inputdir = inputdir
        self.outputdir = outputdir
        pass

    def make_pie(self, data: Union[pd.DataFrame, pd.Series],
                 labels: List[str], counterclock: bool,
                 is_savefig: bool,
                 startangle=90, autopct="%1.1f%%", pctdistance=0.7
                 ):
        # 実装としてはpd.Seriesのみに関してしておく
        assert isinstance(data, pd.Series), "pd.Series型をdataに渡してください"
        plt.pie(data.value_counts(), labels=labels,
                counterclock=counterclock,
                startangle=startangle,
                autopct=autopct,
                pctdistance=pctdistance)
        png_path = os.path.join(self.outputdir, "pi.png")
        if is_savefig and not os.path.exists(png_path):
            print("make new pi.png file")
            plt.savefig(png_path)
        else:
            print("*** NOTE: if you want to save png file, delete pi.png file. ***")
            plt.show()

        

if __name__ == "__main__":
    GU = GraphUtils()