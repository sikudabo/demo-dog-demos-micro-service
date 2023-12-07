import time
from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup as BS
from pathlib import Path 
import json

base_path = Path(__file__).parent 
full_path = f'{base_path}/conditions_urls.json'
disease_names_path = f'{base_path}/disease_names.json'
question_answers_path = f'{base_path}/question_answers.json'
path = Path(full_path)
disease_path = Path(disease_names_path)
qa_path = Path(question_answers_path)
contents = path.read_text()
disease_names_contents = disease_path.read_text()
disease_names = json.loads(disease_names_contents)
condition_urls = json.loads(contents)
idx = 0
question_answers = []

driver = webdriver.Chrome()
base_path = 'https://www.livehealthily.com'

for url in condition_urls:
    driver.get(f'{base_path}{url}')
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, 'p'))
    )
    react_html = driver.page_source
    soup = BS(react_html, 'html.parser')
    p_tags = soup.find_all('p')
    current_text = ''
    for tag in p_tags:
        tag_text = tag.text.replace('*', '')
        tag_text = tag_text.replace('\\', '')
        tag_text = tag_text.replace('<', '')
        tag_text = tag_text.replace('>', '')
        tag_text = tag_text.replace(':', '')
        tag_text = tag_text.replace('/', '')
        current_text += ' ' + tag_text
    current_question_answer = {
        "context": disease_names[idx],
        "question": f'What is {disease_names[idx]}?',
        "answer": current_text.split('Original content Copyright')[0]
    }
    question_answers.append(current_question_answer)
    if idx > len(disease_names):
        break
    idx += 1

print(question_answers)    
contents = json.dumps(list(question_answers))
qa_path.write_text(contents)
print('Wrote the questions and answers')
        


time.sleep(10)

# Close the browser
driver.quit()