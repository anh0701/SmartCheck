import cv2
import numpy as np
import random


def random_rotate(image):
    angle = random.choice([90, 180, 270])
    (h, w) = image.shape[:2]
    M = cv2.getRotationMatrix2D((w // 2, h // 2), angle, 1.0)
    return cv2.warpAffine(image, M, (w, h))


def random_flip(image):
    return cv2.flip(image, random.choice([-1, 0, 1]))


def random_brightness_contrast(image):
    alpha = random.uniform(0.7, 1.3)
    beta = random.randint(-30, 30)
    return cv2.convertScaleAbs(image, alpha=alpha, beta=beta)


def add_noise(image):
    noise = np.random.normal(0, 25, image.shape).astype(np.uint8)
    return cv2.add(image, noise)


def blur(image):
    return cv2.GaussianBlur(image, (3, 3), 0)


def augment(image):
    if random.random() < 0.5:
        image = random_rotate(image)
    if random.random() < 0.5:
        image = random_flip(image)
    if random.random() < 0.7:
        image = random_brightness_contrast(image)
    if random.random() < 0.3:
        image = add_noise(image)
    if random.random() < 0.3:
        image = blur(image)
    return image


def augment_image_cv2(input_path, output_path):
    image = cv2.imread(input_path)
    if image is None:
        raise Exception("Invalid image")

    aug_img = augment(image)

    cv2.imwrite(output_path, aug_img)