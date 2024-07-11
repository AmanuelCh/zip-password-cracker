## Zip Cracker  🕵️‍♀️

This script helps you crack passwords for zipped files. It's a simple brute-force tool designed for educational purposes. Use it responsibly and ethically cuz this script is intended for testing purposes only. Only use it on your own files or with explicit permission.

### Getting Started

1. Save the script: Download either `zipcracker1.py` or `zipcracker2.py` (they have slightly different implementations, so trying both might help if one fails).
2. Create a password dictionary:  Get a wordlist file like `rockyou.txt` (you can find it online) or create your own file with possible passwords. 
3. Place files in the same directory:  Make sure your script (`zipcracker1.py` or `zipcracker2.py`), the zip file you want to crack, and the wordlist file are in the same directory.
4. Run the script: Open a terminal or command prompt in the directory and run the following command:

      python zipcracker.py -f <your_zip_file.zip> -d <your_wordlist.txt>
   

   - Replace `<your_zip_file.zip>` with the actual name of your zipped file.
   - Replace `<your_wordlist.txt>` with the name of your password dictionary file.

Example:

python zipcracker2.py -f secret_data.zip -d rockyou.txt 


### How It Works

The script reads passwords from the wordlist file and attempts to open the zip file using each password. If a password matches, it extracts the files to the same directory.

### Making It Better

* More Wordlists:  Try different wordlists or combine multiple wordlists for a larger set of potential passwords.
* Custom Wordlists: If you have an idea of the type of password used, create a custom wordlist that includes relevant terms.
* Advanced Tools: For more complex passwords, consider using specialized tools like John the Ripper or Hashcat. 
* Multithreading: Improve performance by using multithreading to test multiple passwords concurrently.

If you want to make the script globally availible, see this [gist](https://gist.github.com/joshwyatt/a6e20d28818b5183258b)
