#coding:utf-8
import tensorflow as tf
#定义待优化参数w初值赋5
w = tf.Variable(tf.constant(5, dtype=tf.float32))
#定义损失函数loss
loss = tf.square(w+1)#tf.square()是对a里的每一个元素求平方
#定义反向传播方法
train_step = tf.train.GradientDescentOptimizer(0.2).minimize(loss)
#生成会话，训练40轮
with tf.Session() as sess:
    init_op=tf.global_variables_initializer()#初始化
    sess.run(init_op)#初始化
    for i in range(40):#训练40轮
        sess.run(train_step)#训练
        w_val = sess.run(w)#权重
        loss_val = sess.run(loss)#损失函数
        print ("After %s steps: w is %f,   loss is %f." % (i, w_val,loss_val))#打印
