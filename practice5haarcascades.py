import cv2

# Path to the image
image_path = '/Users/edennahiletework/Desktop/53450892137_f5acc4ac55_o.jpg'

# Load the image
image = cv2.imread(image_path)

# Check if the image was successfully loaded
if image is None:
    print(f'Failed to load image at {image_path}')
else:
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Load the pre-trained Haar Cascade classifier
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    # Draw rectangles around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    # Display the image with detected faces
    cv2.imshow('Detected Faces', image)
    
    # Wait for a key press and close all windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
