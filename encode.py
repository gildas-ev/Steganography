# Imports
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import time

class MessageLenghtError(Exception):
    '''Raise when the message is too large compared to the image'''
    pass

int_to_bin = lambda n : format(int(n), 'b').zfill(8) # Converts integer into binary
bin_to_int = lambda bin : int(bin, 2) # Converts binary into integer
str_to_bin = lambda string : (''.join(f'{ord(i):08b}' for i in string)) # Converts string into binary
new_px_value = lambda px, msg : px[:-1] + msg # Return the new value of a pixel with a message bit

def encode(dir, msg, show=False):
    '''Encodes a message in an image using LSB
    
    Parameters
    ----------
    dir : str
        Directory of your image
    msg : str
        Message to encode
    show : bool, optional
        Show the encoded image or not
    
    Raises
    ------
    MessageLenghtError
        The message is too large compared to the image
    '''
    # Load the image and its pixels
    img = Image.open(dir) # Open the image as img
    px = np.array(img) # Load pixels values in a numpy array
    shape = px.shape # Get the initial shape of the numpy array
    px = px.flatten() # Flatten the array for manipulation
    
    # Create the header and the message
    lenght_msg = str(len(msg))
    header = f'LSBFLAG{"0" * (6 - len(lenght_msg))}{lenght_msg}' # The header indicates the presence of a message and its length
    final_msg = f'{header}{msg}' # The encoded message contains the header and the user's message
    bin_msg = str_to_bin(final_msg) # Converts the encoded message into binary
    
    # Encode the message
    if len(bin_msg) > len(px): # If there are more bits in the binary encoded message than pixels RGB values, there is not enough space to encode
        raise MessageLenghtError('The message is too large compared to the image') # So we raise MessageLenghtError
    
    requiered_pixels = len(bin_msg)
    bin_px = np.array(list(map(int_to_bin, px[:requiered_pixels]))) # Converts the requiered pixels only in binary
    new_values_bin = list(map(new_px_value, bin_px, bin_msg)) # Compute the new pixels values with the encoded message
    new_values_int = np.array(list(map(bin_to_int, new_values_bin))) # Converts binary values into integer
    px[:requiered_pixels] = new_values_int # Replace the requiered pixels with the new values
    
    # Create the encoded image
    px = px.astype(dtype=np.uint8) # Image.fromarray function requieres np.uint8 data-type
    px = px.reshape(shape) # Reshape px array as img shape
    encoded = Image.fromarray(px) # Create the new image from the new pixels values array
    encoded_dir = f'{int(time.time())}.png' # Encoded image's directory
    encoded.save(encoded_dir) # Save the new image
    
    if show == True: # Show the encoded image if requested
        plt.imshow(encoded)
        plt.title('Encoded image')
        plt.show()
    
    print(f"Encoded image's directory : {encoded_dir}") # Print the directory where the encoded image is saved

encode(dir='Sample_1.png', msg='Type your message here')
