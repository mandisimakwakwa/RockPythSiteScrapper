from services import chromeService as ChromeService


class Main:

    gpgSiteUrl = ""
    provincialSiteUrl = ""
    indeedSiteUrl = ""

    chromeServ = ChromeService()

    def __init__(self):
        self.chromeServ.scrapeGPGSite(self.gpgSiteUrl)
