"""
our steps:
1. get music link
2. get meta-text around the music
3. convert text to representation
4. get lots of short videos, stickers and so on
5. convert all of the media in a resprenation in a same space!
6. get line by line and generate image or other medias
7. merge all of the media
8. done and enjoy it:)
"""

music_meta_text = ''

with open("./meta_data/TakKhal.txt", "r", encoding='utf8') as txt_file:
    music_meta_text = txt_file.readlines()


print(music_meta_text)