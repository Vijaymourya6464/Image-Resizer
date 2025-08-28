import cv2
# Configurable Parameters
source = "shadow.jpeg"                # Input image file
destination = "new_resized_image.jpg"    # Output image file

# Resize Options
resize_by_percent = False   # True = resize by percentage, False = resize by custom dimensions
scale_percent = 50          # Used only if resize_by_percent=True

# Custom dimensions (used if resize_by_percent=False)
custom_width = 400
custom_height = 300

# Load the image
# -------------------------------
src = cv2.imread(source, cv2.IMREAD_UNCHANGED)

if src is None:
    print(f"❌ Error: Unable to load image '{source}'. Please check the file path.")
    exit()
# Resize Logic
if resize_by_percent:
    # Calculate new dimensions based on scale percentage
    new_width = int(src.shape[1] * scale_percent / 100)
    new_height = int(src.shape[0] * scale_percent / 100)
else:
    # Use custom dimensions
    new_width = custom_width
    new_height = custom_height

# Resize the image
output = cv2.resize(src, (new_width, new_height), interpolation=cv2.INTER_AREA)

# Save and Display
# -------------------------------
cv2.imwrite(destination, output)
print(f"✅ Image successfully resized and saved as '{destination}'")
print(f"➡️ New Dimensions: {new_width} x {new_height}")

# Show original and resized images for comparison
cv2.imshow("Original Image", src)
cv2.imshow("Resized Image", output)

cv2.waitKey(0)
cv2.destroyAllWindows()
