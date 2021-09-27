import string
import re

url_dict={}

# iter=26
# # shortURL = ""
# # longURL = ""
# # s_len=26
# l = ['a']*12
# def c_string(iter):
#     char = iter % 26
#     pos = int(iter / 26)
#     print(pos)
#     if iter >= 26:
#         l[0] = chr(97+int(char+1))
#     if pos < 12:
#         l[int(pos)] = chr(97+int(char))
#     # else:
#     #     pos %= pos
#     #     l[int(pos)] = chr(97+int(char))
#     return ''.join(i for i in l)
    # for i in range(s_len):
    # if iter == 0: print(chr(97), end="")
    # elif: iter >
    # for j in range(s_len-1):
    #     print(chr(97 + iter), end="")
        # c_string(iter, s_len-1)
        # s_len -= 1

# print(c_string(iter))


    # print("")
    # for j in range(26):
    #     print(chr(97+j), end="")

# print(c_string(iter))
# print("")
# lst = list(string.ascii_lowercase)
# lst = ['a', 'b', 'c']
# char_str = string.ascii_lowercase
# def n_length_combo(lst, n, q):
#     if n == 0:
#         return [[]]
#     l = []
#
#     for i in range(0, len(lst)):
#
#         m = lst[i]
#         remLst = lst[i + 1:]
#
#         for p in n_length_combo(remLst, n - 1, q):
#             l.append([m] + p)
#             if l.index([m] + p) == q: return l
#     return l


# Driver code
# if __name__ == "__main__":
# iter=132
# arr = "abc"
# arr = string.ascii_lowercase
#
# # char = iter % 26
# pos = int(iter / 26)
# # print(pos)
# #
# alpha_combi = n_length_combo([x for x in arr], 2, 325 - iter)
# for i in range(len(alpha_combi)):
#     print(''.join(alpha_combi[i]))
#     # print(alpha_combi)
#     # pass
# print(len(alpha_combi))
# print(''.join(random.choices(string.ascii_uppercase + string.digits, k=N)))
# print(alpha_combi)
# for i in range(12):
#     n_length_combo([x for x in ''.join(lst)], i)



class UrlShortener:
    global count
    count = 1
    def __init__(self):
        pass

    def trc(self, n):
        if (n == 0): pass
        if (n >= 1 and n <= 26): return chr(n + 96)
        else:
            charac = str(self.trc(int(n / 26)))
            x = n % 26
            if x == 0: x = 26 #return chr(ord(charac) - 1) + 'z'
            if (x <= 26): charac += chr(x + 96)
        return charac

    def shorten(self, longURL):
        global count
        if longURL not in url_dict.values():
            # for i in range(1, 128):
            #     print(self.trc(i))

            key = "short.ly/" + str(self.trc(count))
            url_dict[key] = longURL
            count += 1
            return key
        else:
            for x, y in url_dict.items():
                print(x, y)
                if y is longURL: return x

    def redirect(self, shortURL):
        for x, y in url_dict.items():
            print(x, y)
            if x is shortURL: return y

# def test_format(string):
#     return re.search("^short.ly\/[a-z]{1,4}.\/$", string)

urlShortener = UrlShortener()
shortUrl1 = urlShortener.shorten("https://www.codewars.com/kata/5ef9c85dc41b4e000f9a645f")
print(shortUrl1)
longUrl1 = urlShortener.redirect(shortUrl1)
print(longUrl1, "https://www.codewars.com/kata/5ef9c85dc41b4e000f9a645f")
short_url2 = urlShortener.shorten("https://www.codewars.com/kata/5ef9c85dc41b4e000f9a645f")
print(short_url2)
longUrl2 = urlShortener.redirect(short_url2)
print(longUrl2, "https://www.codewars.com/kata/5ef9c85dc41b4e000f9a645f")


# print(test_format(shortUrl1))
# const chai = require("chai");
# const assert = chai.assert;
# chai.config.truncateThreshold = 0;
#
# const testFormat=string=> {
#   assert.isTrue(/^short.ly\/[a-z]{1,4}$/.test(string), `"${ string }" url format is incorrect: should starts with "short.ly/", with length<14 and only lowercase letters a the end.`);
# }
#
# describe("Should pass all of these", function() {
#   it("Testing two different URLs", function() {
#     const urlShortener = new UrlShortener();
#     let shortUrl1 = urlShortener.shorten("https://www.codewars.com/kata/5ef9ca8b76be6d001d5e1c3e");
#     testFormat(shortUrl1);
#     let shortUrl2 = urlShortener.shorten("https://www.codewars.com/kata/5efae11e2d12df00331f91a6");
#     testFormat(shortUrl2);
#     assert.equal(urlShortener.redirect(shortUrl1), "https://www.codewars.com/kata/5ef9ca8b76be6d001d5e1c3e");
#     assert.equal(urlShortener.redirect(shortUrl2), "https://www.codewars.com/kata/5efae11e2d12df00331f91a6");
#   });
#   it("Testing same URLs", function() {
#     const urlShortener = new UrlShortener();
#     let shortUrl1 = urlShortener.shorten("https://www.codewars.com/kata/5ef9c85dc41b4e000f9a645f");
#     testFormat(shortUrl1);
#     let shortUrl2 = urlShortener.shorten("https://www.codewars.com/kata/5ef9c85dc41b4e000f9a645f");
#     testFormat(shortUrl2);
#     assert.equal(shortUrl1, shortUrl2, "Should work with same long URLs");
#     assert.equal(urlShortener.redirect(shortUrl1), "https://www.codewars.com/kata/5ef9c85dc41b4e000f9a645f");
#   });
# });