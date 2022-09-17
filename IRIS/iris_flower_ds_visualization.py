# -*- coding: utf-8 -*-
"""Iris flower ds visualization.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gtXK4TYgThfJYY5K5mtmV_xv77e5zBm2
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

plt.title('Scatter plot between sepal width and sepal length')
flowers_df = sns.load_dataset("iris")
sns.scatterplot(x=flowers_df.sepal_length, y=flowers_df.sepal_width, hue=flowers_df.species, s=100);

setosa_df = flowers_df[flowers_df.species == 'setosa']
versicolor_df = flowers_df[flowers_df.species == 'versicolor']
virginica_df = flowers_df[flowers_df.species == 'virginica']
plt.title('Distribution of Sepal Width')

plt.hist([setosa_df.sepal_width, versicolor_df.sepal_width, virginica_df.sepal_width], 
         bins=np.arange(2, 5, 0.25), 
         stacked=True);

plt.legend(['Setosa', 'Versicolor', 'Virginica']);

flights_df = sns.load_dataset("flights").pivot("month", "year", "passengers")

plt.title("Heatmap for No. of Passengers (1000s)")
sns.heatmap(flights_df);

sns.pairplot(flowers_df, hue='species');

