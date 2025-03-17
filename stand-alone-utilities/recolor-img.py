from PIL import Image, ImageEnhance
import numpy as np
import matplotlib.pyplot as plt


class LineRecolor:
    def __init__(self, input_path, output_path, line_color=(242, 244, 247), threshold=None):
        self.input_path = input_path
        self.output_path = output_path
        self.line_color = line_color  # RGB format
        self.threshold = threshold  # Dynamically calculated or passed threshold value

    def process_image(self):
        # Load image and convert to grayscale
        image = Image.open(self.input_path).convert("L")

        # Enhance contrast to make lines more visible
        enhancer = ImageEnhance.Contrast(image)
        image = enhancer.enhance(2)  # Increase the contrast by a factor of 2 (adjust as needed)

        # Convert to NumPy array
        image_array = np.array(image)

        # Show the enhanced grayscale image to ensure lines are visible
        # plt.imshow(image, cmap='gray')
        # plt.title("Enhanced Grayscale Image")
        # plt.show()

        # Debugging: Check the min and max values of pixels
        print("Enhanced Image min and max pixel values:", image_array.min(), image_array.max())

        # Detect lines based on threshold
        line_mask = image_array < image_array.max()  # Lines are typically darker

        # Debugging: Check the mask
        print("Line mask shape:", line_mask.shape)
        print("Number of lines detected (True values):", np.sum(line_mask))

        # Create a new RGB image with a white background
        colored_image = Image.new("RGB", image.size, (255, 255, 255))  # White background
        colored_array = np.array(colored_image)

        # Apply the new line color where the mask is True
        # This ensures the background stays white and only lines are colored
        colored_array[line_mask] = self.line_color

        # Convert back to image
        final_image = Image.fromarray(colored_array)

        # Save the processed image
        final_image.save(self.output_path)
        print(f"Processed image saved at: {self.output_path}")

def main():
    input_path = "background.png"  # Change to your input file
    output_path = "background-output.png"  # Output file name

    # Try using a dynamically calculated threshold based on image histogram
    recolor = LineRecolor(input_path, output_path)
    recolor.process_image()


if __name__ == "__main__":
    main()
