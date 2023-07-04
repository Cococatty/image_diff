from PIL import Image
import imagehash


def image_similarity(img_path_a, img_path_b):
    # Load the images
    img_a = Image.open(img_path_a)
    img_b = Image.open(img_path_b)

    # Compute the perceptual hashes
    hash_a = imagehash.average_hash(img_a)
    hash_b = imagehash.average_hash(img_b)

    # Compare the hashes and calculate the similarity
    score = 1 - (hash_a - hash_b) / len(hash_a.hash) ** 2
    print('Similarity score:', score)

    return score


