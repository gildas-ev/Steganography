# Steganography software in python
Steganography is the practice of concealing a file, message, image, or video within another file, message, image, or video.
The first recorded use of the term was in 1499 by Johannes Trithemius in his *Steganographia*, a treatise on cryptography and steganography, disguised as a book on magic.

The advantage of steganography over cryptography alone is that the intended secret message does not attract attention to itself as an object of scrutiny. Plainly visible encrypted messages, no matter how unbreakable they are, arouse interest and may in themselves be incriminating in countries in which encryption is illegal. Whereas cryptography is the practice of protecting the contents of a message alone, steganography is concerned both with concealing the fact that a secret message is being sent and its contents.

## Prerequisites
- Python 3.6 or greater
- pillow
- numpy
- matplotlib

## Getting started
**How to encode a message in an image :**

Use *encode.py*, and set the image to use and your message l69 :
```python
encode(dir='Sample_1.png', msg='Type your message here')
```
**How to decode a message in an image :**

Use *decode.py*, and set the image to decode l47 :
```python
decode(dir='your_image.png')
```
Sample images are mine, you can use them freely.

I recommend using .png or .jpg images.

## Example
This image hides a message, use *decode.py* ;)
![Sample](https://github.com/gildas-ev/Steganography/blob/master/Sample_1.png)

## Author
Hi ! My name is Gildas, I'm 15 and I have been learning python for 3 years. I am French. I love sciences and I want to become an engineer.

## License
This project is licensed under the MIT License - see the LICENSE.md file for details
