import string
import random

class Codec:

    chars = string.ascii_letters + "1234567890"

    def __init__(self):
        self.url2code = {}
        self.code2url = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """

        if longUrl not in self.url2code.keys():
            code = ""
            for _ in range(6):
                code += random.choice(self.chars)

            shortUrl = "http://tinyurl.com/" + code
            self.url2code[longUrl] = shortUrl
            self.code2url[shortUrl] = longUrl

        return self.url2code[longUrl]



    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """

        return self.code2url[shortUrl]
