#coding:utf-8
import tensorflow as tf  #引入模块

a = tf.constant([1.0, 2.0])   #定义一个张量等于[1.0,2.0]
b = tf.constant([3.0, 4.0])   #定义一个张量等于[3.0,4.0]
result = a+b                  #实现 a 加 b 的加法
print (result)                  #打印出结果
