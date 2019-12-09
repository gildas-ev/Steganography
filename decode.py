# Imports
from PIL import Image
import numpy as np

class LackMessageError(Exception):
    '''Raise when there are no messages'''
    pass

bin_to_str = lambda byte : chr(int(byte, 2)) # Converts binary into string
lsb = lambda n : format(int(n), 'b')[-1] # Return the Least Significant Bit of an integer

def decode(dir):
    '''Decodes an encoded image

    Parameters
    ----------
    dir : str
        Directory of your image
    
    Raises
    ------
    LackMessageError
        There are no message
    '''
    # Load the image and its pixels
    img = Image.open(dir) # Open the image as img
    px = np.array(img) # Load pixels values in a numpy array
    px = px.flatten()  # Flatten the array for manipulation

    # Load the header
    header_lsb = np.array(list(map(lsb, px[:13*8]))) # Least Significant Bit of the first 104 values (the lenght of the header)
    header_bytes = [''.join(header_lsb[i:i+8]) for i in range(0, len(header_lsb), 8)] # Converts bits into bytes
    header = ''.join(map(bin_to_str, header_bytes)) # Converts bytes into string

    # Checks for the presence of a message using the header
    if header[:7] == 'LSBFLAG': # If there is the flag
        len_msg = int(header[7:]) # Load the message length
    else: # If there are no messages
        raise LackMessageError('There are no messages') # Raise LackMessageError
    
    # Decode message
    msg_lsb = np.array(list(map(lsb, px[13*8:(13+len_msg)*8]))) # Least Significant Bit of the encoded pixels (from header to header+len_msg)
    msg_bytes = [''.join(msg_lsb[i:i+8]) for i in range(0, len(msg_lsb), 8)] # Converts bits into bytes
    msg = ''.join(map(bin_to_str, msg_bytes)) # Converts bytes into string
    print(f'Decoded message : {msg}') # Print the decoded message
    
decode(dir='your_image.png')
