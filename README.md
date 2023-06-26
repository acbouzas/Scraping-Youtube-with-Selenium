# Scraping-Youtube-with-Selenium

# YouTube Popular Videos Scraper

This project is a web scraping tool that collects information about the popular videos from a YouTube channel. It uses the Selenium library to automate the process of navigating the YouTube website and extracting data such as video titles, view counts, and posting dates.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Output](#output)
- [Contributing](#contributing)
- [License](#license)

## Introduction

As a junior data scientist, I have developed this tool to gather data about the popular videos from a specific YouTube channel. By analyzing this data, you can gain insights into the performance and engagement of the channel's content.

The tool is built using Python programming language and utilizes the Selenium library to automate web browsing. It allows you to extract valuable information from the YouTube website without the need for manual data collection.

## Installation

1. Make sure you have Python installed on your system. You can download it from the official Python website: [https://www.python.org/downloads](https://www.python.org/downloads)

2. Clone this repository to your local machine using the following command:

git clone https://github.com/your-username/your-repository.git


3. Navigate to the project directory:


This will install the necessary libraries, including Selenium and pandas.

## Usage

1. Open the `youtube_scraper.py` file in a text editor of your choice.

2. Modify the `url` variable to specify the YouTube channel URL you want to scrape. For example:

'''python
url = 'https://www.youtube.com/@MindfulScience/videos'

"python youtube_scraper.py" '''

## Output
The tool generates a CSV file that contains the following information for each popular video:

Title: The title of the video.
Views: The number of views the video has received.
Posted: The date when the video was posted.
You can open the CSV file using spreadsheet software such as Microsoft Excel or Google Sheets for further analysis and visualization of the data.

## Contributing
If you have any suggestions, improvements, or bug fixes, please feel free to contribute to this project. You can fork the repository, make your changes, and submit a pull request.
