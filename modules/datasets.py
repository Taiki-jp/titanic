import numpy as np
import pandas as pd
import os
import sys
from typing import List, Tuple

class Dataset():
    def __init__(self, filename: str) -> None:
        self.df: pd.DataFrame = pd.read_csv(filename)
        pass

    def preprocessing(self, case: str) -> None:
        if case == "titanic":
            return self.__preprocess_titanic()
        else:
            print("Hasn't Implemented yet")
    
    def __preprocess_titanic(self) -> None:
        # ラベル名をカテゴリカルに変換
        self.df['Sex'].replace('female', 0, inplace=True)
        self.df['Sex'].replace('male', 1, inplace=True)
        
        # 名前が空の人は中央値で置き換え
        median_age = self.df["Age"].median()
        self.df['Age'] = self.df['Age'].replace(np.nan, median_age)
        
        self.df['Embarked'] = self.df['Embarked'].replace(np.nan, 'S')
        dummies_embarked = pd.get_dummies(self.df.Embarked, prefix='Embarked')
        self.df = pd.concat([self.df, dummies_embarked], axis=1)

        self.df.Cabin.fillna('X', inplace=True)
        self.df.Cabin=self.df.Cabin.apply(lambda x: x[0])
        dummies_cabin = pd.get_dummies(self.df.Cabin, prefix='Cabin')
        
        self.df = pd.concat([self.df, dummies_cabin], axis=1)
        self.df.drop(['Embarked','Name','Ticket','Cabin'], axis=1, inplace=True)
        return
