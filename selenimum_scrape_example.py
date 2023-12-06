import time
from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup as BS
from pathlib import Path 
import json

symptom_names = []

base_path = Path(__file__).parent 
full_path = f'{base_path}/symptom_names.json'
path = Path(full_path)

driver = webdriver.Chrome()

driver.get('https://www.livehealthily.com/health-library#symptoms')

element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.TAG_NAME, 'p'))
)

react_html = driver.page_source

soup = BS(react_html, 'html.parser')
a_tags = soup.find_all('a')
for tag in a_tags:
    if tag.parent.name == 'li' and tag.text:
        symptom_names.append(tag.text)

contents = json.dumps(symptom_names)
path.write_text(contents)
print('Saved symptom')
time.sleep(10)

# Close the browser
driver.quit()