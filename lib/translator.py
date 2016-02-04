# coding=utf-8
import cgi
import re
import ssl
import urllib
import urllib2


# Simple Python class for talking to Google's Translate API for free.

# Written by - Adrián Barrio Andrés (https://statickidz.com)
# Version: 1.0

class GoogleTranslate:
    def __init__(self):
        pass

    @staticmethod
    def translate(source, target, text):
        """
        Method to translate a string

        :param source: source language ISO 639-1 Code https://www.loc.gov/standards/iso639-2/php/code_list.php
        :param target: target language ISO 639-1 Code https://www.loc.gov/standards/iso639-2/php/code_list.php
        :param text: text to translate
        :return: translated text
        """

        # Remove certificate verification
        ssl._create_default_https_context = ssl._create_unverified_context

        # Google translate URL
        url = "https://translate.google.com/"

        # POST values
        values = {
            "sl": source,
            "tl": target,
            "js": "n",
            "prev": "_t",
            "hl": "es",
            "ie": "UTF-8",
            "text": text,
            "file": "",
            "edit-text": ""
        }

        # Request headers
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 '
                          '(KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
            'Accept-Encoding': 'none',
            'Accept-Language': 'en-US,en;q=0.8',
            'Connection': 'keep-alive'
        }

        # Encode values to url format
        data = urllib.urlencode(values)

        # Make request
        req = urllib2.Request(url, headers=headers, data=data)

        # Request translation
        try:
            page = urllib2.urlopen(req)
        except urllib2.HTTPError, e:
            return "Error in translation %s" % e.fp.read()

        # Read response and filter results
        content = page.read()
        regextranslation = "<span id=result_box class=\".*?\">(.*?)</span></div>"
        translation = re.search(regextranslation, content).group(1)
        regexclean = "(<!--.*?-->|<[^>]*>)"
        retags = re.compile(regexclean)

        # Remove well-formed tags
        notags = retags.sub('', translation)

        # Clean up anything else by escaping
        translation = cgi.escape(notags)

        return translation
