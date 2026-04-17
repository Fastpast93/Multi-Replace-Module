Google Docs README: https://docs.google.com/document/d/1xAqLjY_Rq4a20ZqctgIBRaLgJRO8v1ZmNGQnxLURcZg/edit?usp=sharing

Multi-Replace-Module


A module that lets you replace a mass amount of keywords from a string, instead of one at a time like .replace()



This is a personal project of mine, and my first. I highly recommend you use it in your code.

I reserve the right to prevent anyone else from copyright protecting this. You may use this material in any form that doesn't prevent other people or me from using it.

---GUIDE---

Define the replacement dictionary like so:


replacement_dict= {"keyword1":"replacement1", "keyword2":"replacement2", "keyword3":"replacement3"}


You can have any amount of keywords as you like, as long as you have a replacement for each one of them.


Now that you have your dictionary, you can use mul_replace like so:


your_substituted_text = mul_replace(your_string, replacement_dict)


The keywords found in your_string will be replaced by their respective value in the replacement dictionary.



Here's an example:



replacement_dict = {"Hello":"Hi there,", "books":"paper"}


string = "Hello World! I like reading books and coding!"


print(f"Original: {string}")


print(f"Updated:  {mul_replace(string, replacement_dict)}")
