import os
import requests
from bs4 import BeautifulSoup

def download_file(url, path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(path, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded: {path}")
    else:
        print(f"Failed to download file. Status code: {response.status_code}")


def is_github_folder_with_files(url):
    # Send an HTTP request to the GitHub repository page
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')

        # Check for the presence of an element or class associated with folders
        folder_indicator = soup.find('span', class_='css-truncate-target')

        # Check for the presence of files within the folder
        file_indicator = soup.find('a', class_='js-navigation-open Link--primary')

        return folder_indicator is not None or file_indicator is not None

    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return False

# Example usage:
url = 'https://github.com/CommanderChrisOrg/CommanderChris/tree/main/src'
if is_github_folder_with_files(url):
    print(f"The URL '{url}' represents a GitHub folder with files.")
else:
    print(f"The URL '{url}' does not represent a GitHub folder with files.")

def scrape_github_repository(url):
    # Send an HTTP request to the GitHub repository page
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')

        # Create a directory with the repository name
        repo_dir = 'CommanderChrisOrg_CommanderChris'
        base_path = "/Users/diliarakaniazova/Downloads"
        os.makedirs(os.path.join(base_path, repo_dir), exist_ok=True)
        

        # Find and download all links (files) on the page
        links = soup.find_all('a', {'class': 'js-navigation-open'})
        for link in links:
            if is_github_folder_with_files(url)
            file_url = 'https://github.com' + link.get('href') + '?raw=true'
            file_name = os.path.join(os.path.join(base_path, repo_dir), link.get('title'))
            download_file(file_url, file_name)
    else:
        print(f"Failed to retrieve the repository page. Status code: {response.status_code}")


# Example usage
github_url = 'https://github.com/CommanderChrisOrg/CommanderChris'
scrape_github_repository(github_url)