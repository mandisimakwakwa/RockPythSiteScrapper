from services import chromeService as ChromeService


class Main:

    gpgSiteUrl = "https://jobs.gauteng.gov.za/"
    provincialSiteUrl = ""
    indeedSiteUrl = ""

    chromeServ = ChromeService.ChromeService()

    def __init__(self):
        print("constructor called")
        Main.chromeServ.scrapeGPGSite(Main.gpgSiteUrl)


object = Main()
