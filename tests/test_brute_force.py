import unittest
from brute_force_logic import image_similarity


class TestBruteForce(unittest.TestCase):

    def setUp(self):
        self.img_dog = 'tests/data/dog_0.jpg'
        self.img_chick = 'tests/data/chick_0.jpg'

    def test_whenDiffImagesProvide_thenScoreIsLow(self):
        score = image_similarity(img_path_a=self.img_dog, img_path_b=self.img_chick)
        self.assertLessEqual(abs(score-0.3437), 0.1)
