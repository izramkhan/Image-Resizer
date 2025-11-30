# Created by: Izram Khan
# Date completed: 30-Nov-2025
# Feel free to use and change. It's all yours
#____________________________________________________________________________________________________
import cv2 as cv 
import os
import time

def image_resizer():
    intro()
    while True:
        try:
        # Taking image details
            main_dir = os.getcwd()
            path = input('\n\nEnter the image path: ')
            img_path = os.path.join(main_dir, path)
            img = cv.imread(img_path)
            img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
            
            # Resizing and displaying
            scale = float(input('\nEnter scale i.e(0.5 -> half, 2 -> double): '))
            height, width = img.shape

            new_width = int(width*scale)
            new_height = int(height*scale)
            resize_image = cv.resize(img, (new_width, new_height), interpolation=cv.INTER_CUBIC)
            print(f"Original: {width}x{height}, Resized: {new_width}x{new_height}")

            # Save the resized image to verify
            cv.imwrite('resized_image.jpg', cv.cvtColor(resize_image, cv.COLOR_RGB2BGR))
            print("Resized image saved as 'resized_image.jpg'")
            break

        except ValueError:
            print('\n❌ Error: Please enter an integer!')
        except cv.error:
            print('\n❌ Error: Invalid file path!')

def intro():
    text = '| ** * || WELCOME TO IMAGE RESIZER|| * ** |'
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.06)
    time.sleep(1)

if __name__ == '__main__':
    image_resizer()