from setuptools.command.easy_install import main as install

req_list = '''sys
              imaplib
              getpass
              email
              datetime
              requests
              json
              googlemaps
              datetime
              time
              xml
              re
              validate_email
           '''.split()

def main():
    for pkg in req_list:
        try:
            __import__(pkg)
        except ImportError:
            install([pkg])
