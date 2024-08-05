#!/usr/bin/env python3

import requests, optparse

def get_options():
    parser = optparse.OptionParser()

    parser.add_option("-u", "--url", dest="url", help="Specify an url to bruteforce.\nEXAMPLE: https://example.org")
    parser.add_option("-w", "--wordlist", dest="wordlist", help="Specify a wordlist path.")

    options = parser.parse_args()[0]

    if not options.url:
        parser.error("\033[91m[-] Please specify an url.")
    elif not options.wordlist:
        parser.error("\033[91m[-] Please specify a wordlist.")
    return options

def request(url):
    try:
        return requests.get(url)
    except requests.exceptions.ConnectionError:
        pass


options = get_options()

target_url = options.url
wordlist_path = options.wordlist

with open(wordlist_path, "r",) as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        test_url = target_url + '/' + word

        response = request(test_url)

        if response:
            print("[+] Discovered URL --> " + test_url)
