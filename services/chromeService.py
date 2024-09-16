from services import scrapperService as ScrapperService


class ChromeService:

    scrapperServ = ScrapperService.ScrapperService()

    # 1. Create scrapeGPGSite function
    def scrapeGPGSite(self, gpgSiteUrl):
        # print("this is a gpg site url test val")
        # print("site url to scrape: ", gpgSiteUrl)
        self.scrapperServ.scrapeSiteGivenUrl("gpg", gpgSiteUrl)

    # 2. Create scrapeProvGovSite function
    def scrapeProvincialSite(provincialSiteUrl):
        print("this is a prov site url test test")

    # 3. Create scrapeIndeedSite function
    def scrapeIndeedSite(indeedSiteUrl):
        print("this is a indeed site url test")

    # 4. Create dataToFileConverter function
