from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

# from selenium.webdriver.common.keys import Keys

# DRIVER = webdriver.Chrome()


class ScrapperService:

    def navigateToJobsUrl(url, urlAppender):
        return url + urlAppender

    def navigateToAllJobs(driver):

        # 1. find element by name
        selectEleObj = driver.find_element(By.NAME, "tblJobs_length")
        print("response from driver find element request: ", selectEleObj)
        # 2. use select selenium method to select based on value
        selectedEleObj = Select(selectEleObj)
        # 3. click element
        selectedEleObj.select_by_value('100')

    def getTableData(urlAppended):
        tableData = []
        try:
            driver = webdriver.Chrome()
            driver.get(urlAppended)

            ScrapperService.navigateToAllJobs(driver)

            dataElements = WebDriverWait(driver, 5).until(
                EC.presence_of_all_elements_located(
                    (By.XPATH, "//table/tbody/tr")))

            for dataElement in dataElements:
                tableData.append(dataElement.text)
        finally:
            driver.quit()

        return tableData

    def getJobTitleFromEleData(jobPost):
        print("job post data parse val {} on job title function", jobPost)
        return ""

    def getJobLocationFromEleData(jobPost):
        return ""

    def getJobRenumFromEleData(jobPost):
        return ""

    def getJobClosDateFromEleData(jobPost):
        return ""

    def formatJobPostEleData(jobPostEleData):
        jobTitle = ""
        jobLocation = ""
        jobRenumeration = [""]
        jobClosingDate = ""

        formatedElementsMap = {}

        for jobPost in jobPostEleData:
            jobTitle = ScrapperService.getJobTitleFromEleData(jobPost)
            jobLocation = ScrapperService.getJobLocationFromEleData(jobPost)
            jobRenumeration = ScrapperService.getJobRenumFromEleData(jobPost)
            jobClosingDate = ScrapperService.getJobClosDateFromEleData(jobPost)

            formatedElementsMap['title'] = jobTitle
            formatedElementsMap['location'] = jobLocation
            formatedElementsMap['renumeration'] = jobRenumeration
            formatedElementsMap['closingDate'] = jobClosingDate

    def scrapeSiteGivenUrl(self, url):

        formattedData = []

        urlAppender = "/Public/Jobs.aspx"
        urlAppended = ScrapperService.navigateToJobsUrl(url, urlAppender)
        jobPostEleData = ScrapperService.getTableData(urlAppended)

        formattedData = ScrapperService.formatJobPostEleData(jobPostEleData)

        return formattedData

    # 4. Create scrapping methods
    #   4.1 navigateToJobsUrl
    #   4.2 findJobPostElements()
    #   4.3 scrapeElementsOfData()
    # 5. dataToFileConv() definition
    #   5.1 Takes data scraped from elements as param inputs as well as file type
    #   5.2 Returns csv file
    pass
