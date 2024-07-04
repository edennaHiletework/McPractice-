import cv2


image_path = '/Users/edennahiletework/Desktop/53450892137_f5acc4ac55_o.jpg'

image = cv2.imread(image_path)


if image is None:
    print('Failed to load image')
else:
  
    (height, width) = image.shape[:2]

  
    center = (width // 2, height // 2)


    angle = 90

  
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)

    rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))


    cv2.imshow('Original Image', image)
    
   
    cv2.imshow('Rotated Image', rotated_image)


    cv2.waitKey(0)
    cv2.destroyAllWindows()
