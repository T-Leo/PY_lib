#!/usr/bin/env python
# coding: utf-8

# Тема “Вычисления с помощью Numpy”
# 
# lsn01_a_ex01 
# 
# Импортируйте библиотеку Numpy и дайте ей псевдоним np.
# Создайте массив Numpy под названием a размером 5x2, то есть состоящий из 5 строк и 2 столбцов. Первый столбец должен содержать числа 1, 2, 3, 3, 1, а второй - числа 6, 8, 11, 10, 7. Будем считать, что каждый столбец - это признак, а строка - наблюдение. Затем найдите среднее значение по каждому признаку, используя метод mean массива Numpy. Результат запишите в массив mean_a, в нем должно быть 2 элемента.

# In[1]:


import numpy as np


# In[2]:


a = np.array(
    [[1, 2, 3, 3, 1], 
    [6, 8, 11, 10, 7]]
).transpose()
print(a)


# In[3]:


mean_a = np.mean(a, axis = 0)
print(mean_a)


# lsn01_a_ex02
# 
# Вычислите массив a_centered, отняв от значений массива а средние значения соответствующих признаков, содержащиеся в массиве mean_a. Вычисление должно производиться в одно действие. Получившийся массив должен иметь размер 5x2.

# In[4]:


a_centered = a - mean_a
print(a_centered)


# lsn01_a_ex03
# 
# 
# 
# Найдите скалярное произведение столбцов массива a_centered. В результате должна получиться величина a_centered_sp. Затем поделите a_centered_sp на N-1, где N - число наблюдений.

# In[5]:


a_centered_sp = a_centered.T[0] @ a_centered.T[1]
print(a_centered_sp)


# In[6]:


a_centered_sp / (a_centered.shape[0] - 1)


# lsn01_a_ex04
# 
# Число, которое мы получили в конце задания 3 является ковариацией двух признаков, содержащихся в массиве “а”. В задании 4 мы делили сумму произведений центрированных признаков на N-1, а не на N, поэтому полученная нами величина является несмещенной оценкой ковариации.
# Подробнее узнать о ковариации можно здесь: -
# В этом задании проверьте получившееся число, вычислив ковариацию еще одним способом - с помощью функции np.cov. В качестве аргумента m функция np.cov должна принимать транспонированный массив “a”. В получившейся ковариационной матрице (массив Numpy размером 2x2) искомое значение ковариации будет равно элементу в строке с индексом 0 и столбце с индексом 1.

# In[7]:


np.cov(a.T)[0, 1]


# Тема “Работа с данными в Pandas”
# 
# lsn01_b_ex01
# 
# Импортируйте библиотеку Pandas и дайте ей псевдоним pd.

# In[8]:


import pandas as pd


# Создайте датафрейм authors со столбцами author_id и author_name, в которых соответственно содержатся данные: [1, 2, 3] и ['Тургенев', 'Чехов', 'Островский'].

# In[9]:


authors = pd.DataFrame({'author_id':[1, 2, 3], 
                        'author_name':['Тургенев', 'Чехов', 'Островский']}, 
                       columns=['author_id', 'author_name'])
print(authors)


# Затем создайте датафрейм book cо столбцами author_id, book_title и price, в которых соответственно содержатся данные:  
# [1, 1, 1, 2, 2, 3, 3],
# ['Отцы и дети', 'Рудин', 'Дворянское гнездо', 'Толстый и тонкий', 'Дама с собачкой', 'Гроза', 'Таланты и поклонники'],
# [450, 300, 350, 500, 450, 370, 290].

# In[10]:


book = pd.DataFrame({'author_id':[1, 1, 1, 2, 2, 3, 3], 
                     'book_title':['Отцы и дети', 'Рудин', 'Дворянское гнездо', 'Толстый и тонкий', 'Дама с собачкой', 'Гроза', 'Таланты и поклонники'], 
                     'price':[450, 300, 350, 500, 450, 370, 290]}, 
                    columns=['author_id', 'book_title', 'price'])
print(book)


# lsn01_b_ex02
# 
# Получите датафрейм authors_price, соединив датафреймы authors и books по полю author_id.

# In[11]:


authors_price = pd.merge(authors, book, on = 'author_id', how = 'outer')
print(authors_price)


# lsn01_b_ex03
# 
# Создайте датафрейм top5, в котором содержатся строки из authors_price с пятью самыми дорогими книгами.

# In[12]:


top5 = authors_price.nlargest(5, 'price')
print(top5)


# lsn01_b_ex04
# 
# Создайте датафрейм authors_stat на основе информации из authors_price.

# In[13]:


authors_stat = authors_price['author_name'].value_counts()
print(authors_stat)


# Создайте датафрейм authors_stat на основе информации из authors_price. В датафрейме authors_stat должны быть четыре столбца:
# author_name, min_price, max_price и mean_price,
# в которых должны содержаться соответственно имя автора, минимальная, максимальная и средняя цена на книги этого автора.

# In[14]:


authors_stat = authors_price.groupby('author_name').agg({'price':['min', 'max', 'mean']})
authors_stat = authors_stat.rename(columns={'min':'min_price', 'max':'max_price', 'mean':'mean_price'})
print(authors_stat)


# lsn01_b_ex05
# 
# Создайте новый столбец в датафрейме authors_price под названием cover, в нем будут располагаться данные о том, какая обложка у данной книги - твердая или мягкая. В этот столбец поместите данные из следующего списка:
# ['твердая', 'мягкая', 'мягкая', 'твердая', 'твердая', 'мягкая', 'мягкая'].
# Просмотрите документацию по функции pd.pivot_table с помощью вопросительного знака.Для каждого автора посчитайте суммарную стоимость книг в твердой и мягкой обложке. Используйте для этого функцию pd.pivot_table. При этом столбцы должны называться "твердая" и "мягкая", а индексами должны быть фамилии авторов. Пропущенные значения стоимостей заполните нулями, при необходимости загрузите библиотеку Numpy.
# Назовите полученный датасет book_info и сохраните его в формат pickle под названием "book_info.pkl". Затем загрузите из этого файла датафрейм и назовите его book_info2. Удостоверьтесь, что датафреймы book_info и book_info2 идентичны.

# In[15]:


authors_price['cover'] = ['твердая', 'мягкая', 'мягкая', 'твердая', 'твердая', 'мягкая', 'мягкая']
print(authors_price)


# In[16]:


book_info = pd.pivot_table(authors_price, values='price', index=['author_name'], columns=['cover'], aggfunc=np.sum)
book_info['мягкая'] = book_info['мягкая'].fillna(0)
book_info['твердая'] = book_info['твердая'].fillna(0)
print(book_info)


# In[17]:


book_info.to_pickle('book_info.pkl')


# In[18]:


book_info2 = pd.read_pickle('book_info.pkl')


# In[19]:


book_info.equals(book_info2)


# In[ ]:




