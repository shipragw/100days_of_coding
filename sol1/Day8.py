logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text, shift_amount, encode_or_decode):
    new_word = []
    if encode_or_decode == "decode":
        shift_amount *= -1
    for letter in original_text:
        if letter not in alphabet:
            new_word.append(letter)
        else:
            x = alphabet.index(letter) + shift_amount
            x %= len(alphabet)
            new_letter = alphabet[x]
            new_word.append(new_letter)

    print(f"Here is the {encode_or_decode}d result : {"".join(new_word)}")

def validated_input(prompt, valid_values):
   while True:
       user_input = input(prompt).lower()
       if user_input not in valid_values:
           print("Wrong input!")
           continue
       return user_input


keep_encoding_decoding = True
while keep_encoding_decoding:
    direction = validated_input("Type 'encode' to encrypt, type 'decode' to decrypt:\n", {"encode", "decode"})
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift, direction)
    replay = validated_input("Type 'yes' if you want to go again. Otherwise type 'no'.\n", {"yes", "no"})
    if replay == "no":
        keep_encoding_decoding = False
        print("GoodBye")
