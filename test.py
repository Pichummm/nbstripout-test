#!/usr/bin/env python
# coding: utf-8

# In[4]:


import random

def print_random_numbers(count, start, end):
    for _ in range(count):
        random_number = random.randint(start, end)
        print(random_number)

# 使用例: 5つのランダムな整数を1から10の範囲で生成
print_random_numbers(5, 1, 10)


# In[3]:


import random

def print_random_numbers(count, start, end):
    for _ in range(count):
        random_number = random.randint(start, end)
        print(random_number)

# 使用例: 5つのランダムな整数を1から10の範囲で生成
print_random_numbers(5, 1, 20)

