print("done")
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
print("done")

#creat data
x_data = np.random.rand(100).astype(np.float32) #生成随机数列
y_data = x_data*0.1+0.3;#需要预测的结果

#creat tensorflow structrue
Weight = tf.Variable(tf.random_uniform([1],-1.0,1.0))#random_uniform矩阵变量(维数,范围)
biases = tf.Variable(tf.zeros([1]))#初始值为0

y=Weight*x_data + biases

loss = tf.reduce_mean(tf.square(y-y_data))#预测值和实际值误差
optimizer = tf.train.GradientDescentOptimizer(0.5)#learning rate
train = optimizer.minimize(loss)#通过优化器减少loss

init=tf.global_variables_initializer()#初始化

#creat tensorflow structrue

sess = tf.Session()
sess.run(init)

fig = plt.figure()#生成图片框
ax = fig.add_subplot(1,1,1)
ax.scatter(x_data,y_data)
plt.ion()
plt.show()

for step in range(200):
    sess.run(train)
    if step % 10 == 0:
        print(step,sess.run(Weight),sess.run(biases))
        try:
            ax.lines.remove(lines[0])
        except Exception:
            pass
        prediction_W = sess.run(Weight)
        prediction_B = sess.run(biases)
        lines = ax.plot(x_data,prediction_W*x_data + prediction_B,'r-',lw=5)
        plt.pause(0.1)