# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup as bs
import json
import random
import os.path


def get_avatar_user(inst_username):
    inst_url = 'https://www.instagram.com'

    response = requests.get(f"{inst_url}/{inst_username}/")

    if response.ok:
        html = response.text
        bs_html = bs(html, 'html.parser')
        bs_html = bs_html.text
        index = bs_html.find('profile_pic_url_hd') + 21
        remaining_text = bs_html[index:]
        remaining_text_index = remaining_text.find('requested_by_viewer') - 3
        string_url = remaining_text[:remaining_text_index]

        print(string_url, "\ndone")

    while True:
        filename = 'av_' + inst_username + '.jpg'
        file_exists = os.path.isfile(filename)

        if not file_exists:
            with open(filename, 'wb+') as handle:
                response = requests.get(string_url, stream=True)
                if not response.ok:
                    print(response)
                for block in response.iter_content(1024):
                    if not block:
                        break
                    handle.write(block)
        else:
            print("file already exist\ndone")
            break


def get_post_from_url(inst_post_url):
    response = requests.get(f"{inst_post_url}")

    if response.ok:
        html = response.text
        bs_html = bs(html, 'html.parser')
        bs_html = bs_html.text
        index = bs_html.find('KL4Bh')
        remaining_text = bs_html[index:]
        remaining_text_index = remaining_text.find('s1080x1080') - 3
        string_url = remaining_text[:remaining_text_index]

        print(string_url, "\ndone")
    while True:
        filename = 'post_1.jpg'
        file_exists = os.path.isfile(filename)

        if not file_exists:
            with open(filename, 'wb+') as handle:
                response = requests.get(string_url, stream=True)
                if not response.ok:
                    print(response)
                for block in response.iter_content(1024):
                    if not block:
                        break
                    handle.write(block)
        else:
            print("file already exist\ndone")
            break


# username = input('enter username: ')
# get_avatar_user(username)
get_post_from_url("https://www.instagram.com/p/B5PhreSgx-P/")
