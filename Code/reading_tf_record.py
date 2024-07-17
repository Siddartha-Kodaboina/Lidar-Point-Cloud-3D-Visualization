import tensorflow as tf

dataset = tf.data.TFRecordDataset(['/Users/sid/Desktop/Personel/SJSU/PP CP Research/Data/uncompressed_lidar_training_100006d9c3e93b6e.tfrecord'])
def _parse_function(example_proto):
    feature_description = {
        'feature1': tf.io.FixedLenFeature([], tf.int64),
        'feature2': tf.io.FixedLenFeature([], tf.string),
    }
    return tf.io.parse_single_example(example_proto, feature_description)

# dataset = tf.data.TFRecordDataset(['path/to/your/file.tfrecord'])
parsed_dataset = dataset.map(_parse_function)
for parsed_record in parsed_dataset:
    print(parsed_record)