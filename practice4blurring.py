import cv2
image_path= '/Users/edennahiletework/Desktop/53450892137_f5acc4ac55_o.jpg'
image = cv2.imread(image_path)
if image is None:
    print('failed')

else:
    # Apply Gaussian Blur
    blurred_image = cv2.GaussianBlur(image, (15, 15), 0)
    
    # Display the original and blurred images
    cv2.imshow('Original Image', image)
    cv2.imshow('Blurred Image', blurred_image)
    
    # Wait for a key press and close all windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()


    
cv2.waitKey(0)
cv2.destroyAllWindows()
    
