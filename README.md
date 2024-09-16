# RockPythSiteScrapper

## Description
The RockPythSiteScrapper project is a project that scrapes data from south african job sites.
The data that is scrapped from these sites is then pushed to a data file.

Supported site links : 
1. https://jobs.gauteng.gov.za/

On the pipeline for support
1. https://provincialgovernment.co.za/
2. https://za.indeed.com/

### Arch Linux Setup
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
4. Install selenium web driver :
   ```
   pip install selenium
   ```
5. Install requests for restful api support :
   ```
   pip install requests
   ```
6. Activate virtual env :
   ```
   source env/bin/activate
   ```
7. Run project :
   ```
   python main.py > output.txt
   ```