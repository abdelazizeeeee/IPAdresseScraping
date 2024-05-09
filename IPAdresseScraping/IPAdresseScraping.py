from selenium import webdriver

class ProxyScraper:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.url = "https://spys.one/en/socks-proxy-list/"
        
    def fetch_ip_addresses(self, max_proxies):
        ip_addresses = []

        self.driver.get(self.url)

        for i in range(3, max_proxies):
            try:
                x_path = f'/html/body/table[2]/tbody/tr[4]/td/table/tbody/tr[{i}]/td[1]/font'
                element = self.driver.find_element("xpath", x_path)
                text = element.text
                ip_addresses.append(text)
            except Exception as e:
                print(f"Element not found for XPath: {x_path}")

        self.driver.quit()  
        return ip_addresses


proxy_scraper = ProxyScraper()
ip_addresses = proxy_scraper.fetch_ip_addresses(10)
print(ip_addresses)
print(len(ip_addresses))
