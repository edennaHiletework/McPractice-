import cv2
image_path= '/Users/edennahzafiletework/Desktop/53450892137_f5acc4ac55_o.jpg'
image = cv2.imread(image_path)
if image is None:
    print('failed')
else:
    cv2.imshow('Original Image', image)

    
cv2.waitKey(0)
cv2.destroyAllWindows()
    
