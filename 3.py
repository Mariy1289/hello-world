#editing

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy


people = ["h","k","m","n","o"]

df_all = pd.DataFrame()
for i in range (10):
    lines = open ("subject_{0}{1}.txt".format(people[i//2],str((i)%2+1)),"r").readlines()
    temp = []
    for l in lines: 
       temp.append (l.split())

    df = pd.DataFrame(temp)
    df.drop(df.loc[df[4]=='0'].index, inplace=True)  # 抽出　４列目が１のものだけ抽出
    
    df['７'] = people[i//2]
    df['8'] = str((i)%2+1)
    # １、２、３、４列目のものは、列名に名前がついてないから勝手に使うとkey error が発生する！
    
    df.drop(columns=[0,1,2,3,4],  inplace = True) #不要なデータを削除
    df[5] = df[5].astype(float)
    df[6] = df[6].astype(float)
    # df_all["8"] = df_all["8"].astype(int)
    df[5] %= 180

    df.plot.scatter(x=5, y=6)
    plt.title('name = {0},no = {1}'.format(people[i//2],str((i)%2+1)) )
    plt.show()

    sns.regplot(x=5, y=6, data=df)
    plt.title('name = {0},no = {1}'.format(people[i//2],str((i)%2+1))) 
    plt.show()
    

    print(df)

    
    df_all = pd.concat([df_all, df], axis=0) #どんどん縦につなげて更新




print(df_all)
print(df_all.dtypes)








