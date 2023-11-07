### Faculties web page Scraping Repository

This repository contains Python scripts for scraping research data from three leading Indian research institutions:

1. [Indian Institutes of Science Education and Research (IISER) Mohali](https://www.iisermohali.ac.in/faculty/people/faculty)
2. [Indian Institutes of Science Education and Research (IISER) Pune](https://www.iiserpune.ac.in/institute/people)
3. [Indian Institutes of Science Education and Research (IISER) Kolkata](https://www.iiserkol.ac.in/web/en/people/faculty/#gsc.tab=0)

## Overview

The main script, `main.py`, serves the following purposes:

1. **Data Scraping:** It scrapes data from each faculties websites of the three institutions, extracting information related to research projects, publications, or any other relevant data.

2. **Data Storage:** The scraped data is then stored in an SQLite3 database, ensuring a structured and efficient storage mechanism.

3. **Data Analysis:** The script also includes functionality to analyze the scraped data, allowing you to gain insights or perform various operations on the collected information.

The script is properly commented for readers to easily follow along..

#### Webpage
We also built a webpage that we use to explain all the methods we used for our scrapping and analysis.

#### Folders of IISER_Pune and IISER_Kolkata
This folder includes the seperate analysis content for these institutes. IISER Mohali's analysis is done by the main.py itself.

## Usage

To use the `main.py` script, follow these steps:

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/kaushik-iiserm/institutional-scrapping/
