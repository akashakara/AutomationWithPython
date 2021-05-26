import requests
from bs4 import BeautifulSoup
import ssl
import csv
from csv import writer


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = "https://www.linkedin.com/jobs/search/?f_E=6&geoId=102713980&keywords=data%20science&location=India"
html = requests.get(url)


soup = BeautifulSoup(str(html.content), 'html.parser')

filename = "LinkedIn_Result.csv"
csv_writer = csv.writer(open(filename, 'w'))

results = soup.find(class_='jobs-search__results-list')
print(soup.results)

with open(filename, 'w') as csv_file:
  csv_writer = writer(csv_file)
  headers = ['Title', 'Location', 'Company','Link']
  csv_writer.writerow(headers)
 
  for job_elem in results:

    title = job_elem.find('span', class_='screen-reader-text').get_text()

    location = job_elem.find('span', class_='job-result-card__location').get_text()
    company = job_elem.find('h4', class_='result-card__subtitle').get_text()
    link = job_elem.find("a")["href"]
 


    csv_writer.writerow([title, location, company,link])