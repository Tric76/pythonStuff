A "secret language" experiment with a fixed code, so anyone with the program can both encode and decode any message without a secret key.
I use this little project to practise my freshly aquired coding skills.
I know I could have used a cryptography library, but I find it entertaining to think about ways to encrypt messages like I would have done as a kid.
This program translates the letters into numbers and messes around with it to make it less obvious to decode.
Version 6 works with a "rolling code", so the letter A will translate to 10 and after 8 characters it will add 1 to each translation so A will become 11 etc.
Version 7 will scramble around the encrypted code even more (changing the order), but is not yes stable/ work as intended.
The program can both encode and decode and will filter most of the wrong input (for now only alphabetical characters and some punctuation marks).
Maybe someone will enjoy it.
