"""
    SSL Checking Tool
    By Official Muffin
    08/09/2021
"""
import requests


def status_code_200():
    print("*******************************")
    print("*        Response 200         *")
    print("*   Certificate Verification  *")
    print("*          VERIFIED!          *")
    print("*******************************\n")


def main():
    while True:
        print("1) Secure HTTPS")
        print("2) Insecure HTTP")
        print("Please select http method (1 or 2): \n")

        method = input()
        if method == '1':
            https = "https://"
            url = str(https + input("Please input a url (excluding https://): "))
        elif method == '2':
            http = "http://"
            url = str(http + input("Please input a url (excluding http://): "))
        else:
            print("Invalid Input")
            continue

        try:
            response = requests.get(url, verify=True)
            if response.status_code == 410:
                print("Site has been disabled\n")
            elif response.status_code == 200:
                status_code_200()
        except requests.exceptions.SSLError:
            print("*****************************")
            print("*         WARNING!          *")
            print("*  Certificate Verification *")
            print("*          FAILED!          *")
            print("*  Certificate has Expired  *")
            print("*****************************\n")
            another = input("Do you want to try another?: (Y/n)\n")
            if another == 'Y':
                continue
            elif another == 'n':
                return 0

        except requests.exceptions.ConnectionError:
            print("Site does not exist")


if __name__ == '__main__':
    main()
