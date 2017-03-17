import tensorflow as tf

a = tf.placeholder(tf.float32, shape=[3])

b = tf.constant([5,5,5], tf.float32)

c = a + b

with tf.Session() as sess:
    writer = tf.summary.FileWriter('./graph', sess.graph)
writer.close()