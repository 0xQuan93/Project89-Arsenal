import cv2

def distort_image(image_path, distortion_type):
    """Distorts the image using the specified distortion type."""
    image = cv2.imread(image_path)
    if distortion_type == "wave":
        rows, cols = image.shape[:2]
        # Create a wave distortion effect
        mapy, mapx = np.indices((rows, cols), dtype=np.float32)
        mapx = 2 * mapx / (cols - 1) - 1
        mapy = 2 * mapy / (rows - 1) - 1
        r, theta = cv2.cartToPolar(mapx, mapy)
        wave_factor = 0.1  # Adjust for stronger/weaker wave effect
        r = r + wave_factor * np.sin(theta * 10)
        mapx, mapy = cv2.polarToCart(r, theta)
        mapx = ((mapx + 1) * cols - 1) / 2
        mapy = ((mapy + 1) * rows - 1) / 2
        distorted_image = cv2.remap(image, mapx, mapy, cv2.INTER_LINEAR)
    elif distortion_type == "stretch":
        # Create a stretch distortion effect
        distorted_image = cv2.resize(image, None, fx=1.5, fy=1, interpolation=cv2.INTER_CUBIC)
    else:
        distorted_image = image
    return distorted_image

if __name__ == "__main__":
    # Example usage
    image_path = "input.jpg"
    distortion_type = "wave"
    distorted_image = distort_image(image_path, distortion_type)
    cv2.imshow("Distorted Image", distorted_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()