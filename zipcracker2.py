import optparse
import zipfile
from threading import Thread
import time

def extract_zip(zfile, password):
    """Attempts to extract the zip file using the given password.
    
    Args:
        zfile (zipfile.ZipFile): The zip file object.
        password (str): The password to try.
    """
    try:
        zfile.extractall(pwd=password.encode('utf-8'))  # Convert password to bytes
        print(f"[+] Password Found: {password}\n")
        print(f"Successfully extracted files to the current directory.\n")
        zFile.close()
        exit(0)  # Exit the program after success
    except Exception as e:  # Catch any exception during extraction
        print(f"[-] Password '{password}' failed.")
        pass

def main():
    """Parses command-line arguments and starts the brute-force process."""
    parser = optparse.OptionParser("usage %prog -f <zipfile> -d <dictionary>")
    parser.add_option('-f', dest='zname', type='string', help='specify zip file')
    parser.add_option('-d', dest='dname', type='string', help='specify dictionary file')
    (options, args) = parser.parse_args()

    if options.zname is None or options.dname is None:
        print(parser.usage)
        exit(0)

    zname = options.zname
    dname = options.dname

    zFile = zipfile.ZipFile(zname)
    passFile = open(dname, 'r')

    start_time = time.time()  # Get start time for tracking

    for line in passFile:
        password = line.strip()
        t = Thread(target=extract_zip, args=(zFile, password))
        t.start()

    # Wait for threads to finish (if no password found)
    while True:
        if time.time() - start_time > 60:  # Check every 60 seconds
            print("[-] No password found in the dictionary after 1 minute. Exiting...")
            zFile.close()
            break

if __name__ == "__main__":
    main()
