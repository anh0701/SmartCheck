import os
from repositories.image_processing import augment_image_cv2

INPUT_FOLDER = "dataset/images"
OUTPUT_FOLDER = "dataset/images_aug"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# num_aug trong khoảng 3 - 5 là tốt, nhiều quá có thể model dễ overfit vào noise giả

def augment_dataset(num_aug=3):
    results = []

    for filename in os.listdir(INPUT_FOLDER):
        input_path = os.path.join(INPUT_FOLDER, filename)

        if not filename.lower().endswith((".jpg", ".png", ".jpeg")):
            continue

        name, ext = os.path.splitext(filename)

        for i in range(num_aug):
            output_name = f"{name}_aug_{i}{ext}"
            output_path = os.path.join(OUTPUT_FOLDER, output_name)

            augment_image_cv2(input_path, output_path)
            results.append(output_path)

    return results