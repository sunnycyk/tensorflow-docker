import tensorflow as tf
a = tf.constant([2, 2], name="a")
b = tf.constant([3,6], name="b")
x = tf.add(a, b, name="add")
with tf.Session() as sess:
    writer = tf.summary.FileWriter('./graph', sess.graph)
print(sess.run(x))
# close the writer when you’re done using it
writer.close()