

vowels = ['a','e','i','o','u']

alphabet = input("Enter character : ")

if(alphabet.lower() in vowels or alphabet.upper() in vowels):

    print("{} is Vowel".format(alphabet))
else:

    print("{} is consonent".format(alphabet))