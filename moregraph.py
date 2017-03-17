import tensorflow as tf
x = 2
y = 3
op1 = tf.add(x, y)
op2 = tf.multiply(x, y)
useless = tf.multiply(x, op1)
op3 = tf.pow(op2, op1)
with tf.Session() as sess:
    op3 = sess.run(op3) 
    writer = tf.summary.FileWriter('./graph', sess.graph)

writer.close()