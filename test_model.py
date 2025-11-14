import pytest
import tensorflow as tf
import os


def test_check_sv():
    model="emotion_detection.keras"
    assert os.path.exists(model)

def test_check_chrg():    
    model = tf.keras.models.load_model('emotion_detection.keras')
    assert model is not None, "le model n'est pas chargee"