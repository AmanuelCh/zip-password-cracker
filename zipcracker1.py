import optparse
import zipfile
from threading import Thread

def extract_zip(zfile, password):
    """Attempts to extract the zip file using the given password.
    
    Args:
        zfile (zipfile.ZipFile): The zip file object.
        password (str): The password to try.
    """
    try:
        zfile.extractall(pwd=password.encode('utf-8'))  # Encode password to bytes
        print(f"[+] Password Found: {password}")
        
        # Extract file content
        for info in zfile.infolist():
            if not info.is_dir():
                content = zfile.read(info.filename)
                print(f"File: {info.filename}")
                print(f"Content: {content.decode('utf-8')}")
        
        zfile.close()  # Close the zip file after success
        exit(0)  # Exit the program after success
    except:
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
    passFile = open(dname, 'r')  # Open the dictionary file in read mode

    password_found = False
    for line in passFile:
        password = line.strip()  # Remove newline character from password
        t = Thread(target=extract_zip, args=(zFile, password))
        t.start()
        t.join()  # Wait for the thread to finish before checking the next password
        if password_found:
            break

    if not password_found:
        print("[-] Password not found in the dictionary file.")

if __name__ == "__main__":
    main()
