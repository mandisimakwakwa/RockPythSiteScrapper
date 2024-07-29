# RockPythSiteScrapper

## Description
The RockPythSiteScrapper project is a project that scrapes data from south african job sites.
The data that is scrapped from these sites is then pushed to a data file.

Supported site links : 
1. https://jobs.gauteng.gov.za/
2. https://provincialgovernment.co.za/
3. https://za.indeed.com/

### Linux Setup
1. Install Python :
     ```
     sudo pacman -Syyu python
     ```
2. Install pip :
   ```
   sudo pacman -Syyu pip
   ```
3. Install virtual env :
   ```
   python -m venv /path/to/env
   ```
4. Activate virtual env :
   ```
   source venv/bin/activate
   ```
5. Install selenium web driver :
   ```
   pip install selenium
   ```
6. Install requests for restful api support :
   ```
   pip install requests
   ```
