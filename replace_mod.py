#replace_mod
def mul_replace(string, dict):
    for key, value in dict.items():
        string = string.replace(key, value)
    return string
if __name__ == '__main__':
    print('Guide')
    print('Define the replacement dictionary like so:')
    print('replacement_dict= {"item1":"replacement1", "item2":"replacement2", "item3":"replacement3"}')
    print('You can add any amount of items and replacements as you like.')
    print('Now that you have your dictionary, you can use mul_replace like so:')
    print('your_substituted_text = mul_replace(your_string, replacement_dict)')
    print('The items found in your_string will be replaced by their respective value in the replacement dictionary.')
    replacement_dict = {"Hello":"Hi there,", "books":"paper"}
    string = "Hello World! I like reading books and coding!"
    print(f"Original: {string}")
    print(f"Updated:  {mul_replace(string, replacement_dict)}")

#Guide
#Define the replacement dictionary like so:
#replacement_dict= {"item1":"replacement1", "item2":"replacement2", "item3":"replacement3"}
#You can add any amount of items and replacements as you like.
#Now that you have your dictionary, you can use mul_replace like so:
#your_substituted_text = mul_replace(your_string, replacement_dict)
#The keywords found in your_string will be replaced by their respective value in the replacement dictionary.
#Heres an example:
#replacement_dict = {"Hello":"Hi there,", "books":"paper"}
#string = "Hello World! I like reading books and coding!"
#print(f"Original: {string}")
#print(f"Updated:  {mul_replace(string, replacement_dict)}")
