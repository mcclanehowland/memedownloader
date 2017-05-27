import pynstagram
import urllib

with pynstagram.client('hopperclod', 'shorecrest18') as client:
    client.upload('images/image1.jpeg', '#meow')
