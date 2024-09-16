from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

# from selenium.webdriver.common.keys import Keys

# DRIVER = webdriver.Chrome()


class ScrapperService:

    currPaginVal = 0

    def navigateToJobsUrl(url, urlAppender):
        return url + urlAppender

    def navigateToAllJobs(driver):

        # 1. find element by name
        selectEleObj = driver.find_element(By.NAME, "tblJobs_length")
        # print("\n\nresponse from driver find element request: ", selectEleObj)
        # 2. use select selenium method to select based on value
        selectedEleObj = Select(selectEleObj)
        # 3. click element
        selectedEleObj.select_by_value('100')

    def clickNextPageBtn(driver):
        classname = "tblJobs_next"
        # 1. find next button element
        nextBtnEleObj = driver.find_element(By.ID, classname)
        # print("\n\nnext btn ele val : ", nextBtnEleObj)

        # 2. click next button
        nextBtnEleObj.click()

    def getTableData(driver, maxPaginVal, urlAppended):
        tableData = []

        if (ScrapperService.currPaginVal == 0):
            ScrapperService.navigateToAllJobs(driver)

            dataElements = WebDriverWait(driver, 5).until(
                EC.presence_of_all_elements_located(
                    (By.XPATH, "//table/tbody/tr")))

            for dataElement in dataElements:
                tableData.append(dataElement.text)

            # print("currPaginVal before : ", ScrapperService.currPaginVal)
            ScrapperService.currPaginVal += 1
            # print("currPaginVal after : ", ScrapperService.currPaginVal)
            # print("maxPaginVal : ", maxPaginVal)

        elif(ScrapperService.currPaginVal < maxPaginVal):
            ScrapperService.clickNextPageBtn(driver)
            ScrapperService.currPaginVal += 1

            ScrapperService.navigateToAllJobs(driver)

            dataElements = WebDriverWait(driver, 5).until(
                EC.presence_of_all_elements_located(
                    (By.XPATH, "//table/tbody/tr")))

            for dataElement in dataElements:
                tableData.append(dataElement.text)

        return tableData

    def getJobTitleFromEleData(jobPost):
        print("job post data parse val : ", jobPost)
        jobTitle = jobPost.partition("Department")[0]
        print("\n")
        print("job title : ", jobTitle)
        print("\n")
        return jobTitle

    def getJobDepartmentFromEleData(jobPost):
        department = ""
        govDepartmentList = [
            "Agriculture, Land Reform and Rural Development",
            "Basic Education",
            "Civilian Secretariat for Police",
            "Communications and Digital Technologies",
            "Cooperative Governance and Traditional Affairs",
            "Co-Operative Governance and Traditional Affairs",
            "Correctional Services",
            "Defence",
            "Employment and Labour",
            "Forestry, Fisheries and the Environment"
            "Government Communication and Information System",
            "Health",
            "Higher Education and Training",
            "Home Affairs",
            "Human Settlements",
            "Independent Police Investigative Directorate",
            "International Relations and Cooperation",
            "Justice and Constitutional Development",
            "Military Veterans",
            "Mineral Resources and Energy",
            "National School of Government",
            "National Treasury",
            "Office of the Chief Justice",
            "Planning Monitoring and Evaluation",
            "Public Enterprises",
            "Public Service and Administration",
            "Public Service Commission",
            "Public Works and Infrastructure",
            "Infrastructure Development",
            "Science and Innovation",
            "Small Business Development",
            "Social Development",
            "SA Police Service",
            "SA Revenue Service",
            "State Security Agency",
            "Sport, Arts and Culture",
            "Statistics South Africa",
            "Tourism",
            "Trade, Industry and Competition",
            "Transport",
            "Water and Sanitation",
            "Women, Youth and Persons with Disabilities",
            "The Presidency"
        ]

        for govDepartment in govDepartmentList:
            matchRes = jobPost.find(govDepartment)
            if (matchRes >= 0):
                department = govDepartment

        print("department val : ", department)
        print("\n\n")

        return department

    def getJobLocationFromEleData(jobPost):
        return ""

    def getJobRenumFromEleData(jobPost):
        return ""

    def getJobClosDateFromEleData(jobPost):
        return ""

    def formatJobPostEleData(jobPostEleData):
        jobTitle = ""
        jobDepartment = ""
        jobLocation = ""
        jobRenumeration = [""]
        jobClosingDate = ""

        formatedElementsMap = {}

        for jobPost in jobPostEleData:
            jobTitle = ScrapperService.getJobTitleFromEleData(jobPost)
            jobDepartment = ScrapperService.getJobDepartmentFromEleData(jobPost)
            jobLocation = ScrapperService.getJobLocationFromEleData(jobPost)
            jobRenumeration = ScrapperService.getJobRenumFromEleData(jobPost)
            jobClosingDate = ScrapperService.getJobClosDateFromEleData(jobPost)

            formatedElementsMap['title'] = jobTitle
            formatedElementsMap['department'] = jobDepartment
            formatedElementsMap['location'] = jobLocation
            formatedElementsMap['renumeration'] = jobRenumeration
            formatedElementsMap['closingDate'] = jobClosingDate

    def getMaxPaginVal(driver, siteJobsUrl):
        className = "//span/a[last()]"

        ScrapperService.navigateToAllJobs(driver)
        
        # 1. find element by class name
        maxPaginEleObj = driver.find_element(By.XPATH, className)
        maxPaginEleText = maxPaginEleObj.text

        # Get the element by classname
        # print("max pagin element obj")
        # print(maxPaginEleObj)
        
        # print("max pagin element text: ", maxPaginEleText)

        return int(maxPaginEleText)

    def scrapeGPGSiteBySite(siteName, siteUrl):
        formattedData = []
        allJobPostEleData = []

        urlAppender = "/Public/Jobs.aspx"
        urlAppended = ScrapperService.navigateToJobsUrl(siteUrl, urlAppender)

        driver = webdriver.Chrome()
        driver.get(urlAppended)

        # 1. Get max pagination val
        maxPaginVal = ScrapperService.getMaxPaginVal(driver, urlAppended)

        # print("max pagin return val : ", maxPaginVal)
        # maxPaginArrayVal = maxPaginVal - 1
        # print("max pagin array return val : ", maxPaginArrayVal)

        # 2. iterate through max val - 1 to get all posts
        for i in range(maxPaginVal):
            jobPostEleData = ScrapperService.getTableData(driver, maxPaginVal, urlAppended)
            # print("table data successfully retrieved")
            allJobPostEleData.extend(jobPostEleData)
            # print("all job posts ele data extension")
            # print("max pagin itr val : ", i)
            
        driver.quit()

        formattedData = ScrapperService.formatJobPostEleData(allJobPostEleData)
        return formattedData

    def scrapeSiteGivenUrl(self, siteName, siteUrl):
        ScrapperService.scrapeGPGSiteBySite(siteName, siteUrl)

        

    # 4. Create scrapping methods
    #   4.1 navigateToJobsUrl
    #   4.2 findJobPostElements()
    #   4.3 scrapeElementsOfData()
    # 5. dataToFileConv() definition
    #   5.1 Takes data scraped from elements as param inputs as well as file type
    #   5.2 Returns csv file
    pass
