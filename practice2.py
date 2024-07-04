import cv2
image_path= '/Users/edennahiletework/Desktop/53450892137_f5acc4ac55_o.jpg'
image = cv2.imread(image_path)
if image is None:
    print('failed')
else:
    cv2.imshow('Original Image', image)
    
scale_percent = 50  # percent of original size
width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)
dim = (width, height)
resized_image = cv2.resize(image, dim)
cv2.imshow('Scaled Image', resized_image)
    

    
cv2.waitKey(0)
cv2.destroyAllWindows()
    
