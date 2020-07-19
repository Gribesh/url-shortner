import pyshorteners
url=input("Enter URL\n")
shortener=pyshorteners.Shortener()
tinyurl=shortener.tinyurl
short_url=tinyurl.short(url)
print("Your short url: \n" , short_url)