#! /usr/bin/env python

import magic

def get_mime(file_descr):
    mime = magic.from_buffer(file_descr.read(), mime=True)
    return mime

if __name__ == "__main__":
    with open('captain-snowball.jpg', 'rb') as finput:
        print(get_mime(finput)) 

