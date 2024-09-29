import requests
from bs4 import BeautifulSoup

url = "https://omgtu.ru/general_information/the-structure/the-department-of-university.php"
response = requests.get(url)

def parse():
    soup = BeautifulSoup(response.content, "html.parser")
    departments = soup.find("div", id="pagecontent")
    departments2 = departments.find_all("a")
    departments_list = [department.text for department in departments2]

    print(departments_list)

    with open("OmGTU_Departaments.txt", "w", encoding="utf-8") as f:
        for departament in departments_list:
            f.write(departament + "\n")

    print("Список кафедр сохранён в файл OmGTU_Departaments.txt")