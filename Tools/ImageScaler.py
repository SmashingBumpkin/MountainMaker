
def resize_and_center_crop(image_path, target_width=800, target_height=600):
    # Read the image
    image = cv2.imread(image_path)

    # Get the dimensions of the original image
    original_height, original_width = image.shape[:2]
    # TODO: Should it upscale or should it discard upscales?

    # Calculate the aspect ratio of the original image
    aspect_ratio = original_width / original_height #16:9

    # Calculate the aspect ratio of the target size
    target_aspect_ratio = target_width / target_height #4:3

    # Determine whether to resize based on width or height
    if aspect_ratio >= target_aspect_ratio:
        #old image is height limited so resize based on height
        new_height = target_height
        new_width = int(target_height * aspect_ratio)
        # Resize based on width
    else:
        # Old image is width limited so resize based on width
        new_width = target_width
        new_height = int(target_width / aspect_ratio)

    # Resize the image
    resized_image = cv2.resize(image, (new_width, new_height))

    # Calculate the cropping parameters
    crop_x = max(0, (new_width - target_width) // 2)
    crop_y = max(0, (new_height - target_height) // 2)

    # Perform the centered crop
    cropped_image = resized_image[
        crop_y : crop_y + target_height, crop_x : crop_x + target_width
    ]

    return cropped_image


def load_and_save_scaled_image(inputPath, outputPath):
    resizedImage = resize_and_center_crop(inputPath)
    # Save the resized image
    cv2.imwrite(outputPath, resizedImage)