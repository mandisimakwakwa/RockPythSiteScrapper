from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# from selenium.webdriver.common.keys import Keys

# DRIVER = webdriver.Chrome()


class ScrapperService:

    def navigateToJobsUrl(url, urlAppender):
        return url + urlAppender

    def getTableData(urlAppended):
        tableData = []

        try:
            driver = webdriver.Chrome()
            driver.get(urlAppended)

            dataElements = WebDriverWait(driver, 5).until(
                EC.presence_of_all_elements_located(
                    (By.XPATH, "//table/tbody/tr")))

            for dataElement in dataElements:
                tableData.append(dataElement.text)
        finally:
            driver.quit()

        return tableData

    def getJobTitleFromPostEleData(jobPost):
        print("job post data parse val {} on job title function", jobPost)
        return ""

    def getJobLocationFromPostEleData(jobPost):
        return ""

    def getJobRenumerationFromPostEleData(jobPost):
        return ""

    def getJobClosingDateFromPostEleData(jobPost):
        return ""

    def formatJobPostEleData(self, jobPostEleData):
        jobTitle = ""
        jobLocation = ""
        jobRenumeration = [""]
        jobClosingDate = ""

        formatedElementsMap = {}

        for jobPost in jobPostEleData:
            jobTitle = self.getJobTitleFromPostEleData(jobPost)
            jobLocation = self.getJobLocationFromPostEleData(jobPost)
            jobRenumeration = self.getJobRenumerationFromPostEleData(jobPost)
            jobClosingDate = self.getJobClosingDateFromPostEleData(jobPost)

            formatedElementsMap['title'] = jobTitle
            formatedElementsMap['location'] = jobLocation
            formatedElementsMap['renumeration'] = jobRenumeration
            formatedElementsMap['closingDate'] = jobClosingDate

    def scrapeSiteGivenUrl(self, url):

        formattedData = []

        urlAppender = "/Public/Jobs.aspx"
        urlAppended = ScrapperService.navigateToJobsUrl(url, urlAppender)
        jobPostElementData = ScrapperService.getTableData(urlAppended)

        formattedData = self.formatJobPostEleData(self, jobPostElementData)

        return formattedData

    # 4. Create scrapping methods
    #   4.1 navigateToJobsUrl
    #   4.2 findJobPostElements()
    #   4.3 scrapeElementsOfData()
    # 5. dataToFileConv() definition
    #   5.1 Takes data scraped from elements as param inputs as well as file type
    #   5.2 Returns csv file
    pass
