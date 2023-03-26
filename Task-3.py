from pyshorteners import *
url=input("Enter the Long Link That You Would Like to Shorten:")
print('The Short link is :> ',Shortener().tinyurl.short(url))