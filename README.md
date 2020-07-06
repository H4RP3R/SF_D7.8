## Как запустить  

```
git clone https://github.com/H4RP3R/SF_D6.11.git
cd SF_D6.11
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
python manage.py runserver
```
В БД уже есть данные

## Проверка
С главной страницы можно перейти на DetailView каждой книги, кликнув по названию.  
Добавить книгу с описанием и изображением можно из фронтенда и админки.  
Связать друга с книгой из админки можно как из модели "друг", так и из модели "книга".  
Во фронтенде — через "Одолженные книги".  
Добавить нового друга можно в админке и во фронтенде.  
