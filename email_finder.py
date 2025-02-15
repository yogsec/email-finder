import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import argparse
from concurrent.futures import ThreadPoolExecutor

BANNER = """
###########################################
#   Email Finder | Designed by YogSec    #
###########################################
"""

VERSION = '1.0'

# Function to extract emails from a webpage
def extract_emails(url):
    emails = set()
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            found_emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', soup.get_text())
            emails.update(found_emails)
    except Exception as e:
        pass
    return emails

# Function to check common pages for contact information
def crawl_emails_from_website(base_url):
    urls_to_check = [
        base_url,
        urljoin(base_url, '/contact-us'),
        urljoin(base_url, '/contact'),
        urljoin(base_url, '/about'),
        urljoin(base_url, '/support'),
        urljoin(base_url, '/help'),
        urljoin(base_url, '/team'),
        urljoin(base_url, '/careers'),
        urljoin(base_url, '/jobs'),
        urljoin(base_url, '/faq'),
        urljoin(base_url, '/press'),
        urljoin(base_url, '/media'),
        urljoin(base_url, '/partners'),
        urljoin(base_url, '/company'),
        urljoin(base_url, '/privacy-policy'),
        urljoin(base_url, '/terms'),
        urljoin(base_url, '/legal'),
        urljoin(base_url, '/get-in-touch'),
        urljoin(base_url, '/reach-us'),
        urljoin(base_url, '/enquiries'),
        urljoin(base_url, '/feedback'),
        urljoin(base_url, '/customer-support'),
        urljoin(base_url, '/customer-service'),
        urljoin(base_url, '/connect'),
        urljoin(base_url, '/who-we-are'),
        urljoin(base_url, '/meet-the-team'),
        urljoin(base_url, '/en/contact'),
        urljoin(base_url, '/en/about'),
        urljoin(base_url, '/en/support'),
        urljoin(base_url, '/info/contact'),
        urljoin(base_url, '/company/contact'),
    ]

    all_emails = set()

    with ThreadPoolExecutor(max_workers=10) as executor:
        results = executor.map(extract_emails, urls_to_check)

    for emails in results:
        all_emails.update(emails)

    return all_emails

# Main function
def main():
    parser = argparse.ArgumentParser(description='Email Finder | Designed by YogSec')
    parser.add_argument('-v', '--version', action='store_true', help='Show version information')
    parser.add_argument('-l', '--list', type=str, help='Provide a file containing list of URLs')
    parser.add_argument('-d', '--domain', type=str, help='Provide a single URL')
    parser.add_argument('-s', '--save', type=str, help='Save output to a file')
    args = parser.parse_args()

    print(BANNER)

    if args.version:
        print(f'Email Finder | Version {VERSION}')
        return

    urls = []

    if args.list:
        with open(args.list, 'r') as file:
            urls = [line.strip() for line in file.readlines()]

    if args.domain:
        urls.append(args.domain.strip())

    all_emails = set()
    with ThreadPoolExecutor(max_workers=5) as executor:
        results = executor.map(crawl_emails_from_website, [url if url.startswith('http') else 'https://' + url for url in urls])

    for emails in results:
        all_emails.update(emails)

    if args.save:
        with open(args.save, 'w') as output_file:
            for email in all_emails:
                output_file.write(email + '\n')
        print(f'Emails saved to {args.save}')
    else:
        for email in all_emails:
            print(email)

if __name__ == '__main__':
    main()
