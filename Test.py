import cv2
import numpy as np

def compare_images(image1_path, image2_path, threshold=30,output_folder="output"):
    # Load the images
    image1 = cv2.imread(image1_path)
    image2 = cv2.imread(image2_path)
    
    # Check if the images have the same size
    if image1.shape != image2.shape:
        raise ValueError("Images must have the same dimensions")
    
    # Convert images to grayscale
    gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
    
    # Compute the absolute difference between the two images
    diff = cv2.absdiff(gray1, gray2)
    
    # Threshold the difference to highlight significant changes
    _, thresh = cv2.threshold(diff, threshold, 255, cv2.THRESH_BINARY)
    
    # Find contours of the differences
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Draw rectangles around the differences
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(image1, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.rectangle(image2, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    # Display the results
    # cv2.imshow('Differences Image 1', image1)
    # cv2.imshow('Differences Image 2', image2)
    # cv2.imshow('Differences Highlighted', thresh)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    
    cv2.imwrite(f"{output_folder}\Original\Differences_Image1.jpg",image1)
    cv2.imwrite(f"{output_folder}\Original\Differences_Image2.jpg",image2)
    cv2.imwrite(f"{output_folder}\Differnce\Differences_Image1.jpg",thresh)

# Example usage
compare_images(
    r"C:\Users\rohit.pandey\OneDrive - Walker Digital Table Systems\Documents\PythonLearning\Image1.jpg",
    r"C:\Users\rohit.pandey\OneDrive - Walker Digital Table Systems\Documents\PythonLearning\Image2.jpg",
    output_folder=r"C:\Users\rohit.pandey\OneDrive - Walker Digital Table Systems\Documents\PythonLearning\Compare"
)
