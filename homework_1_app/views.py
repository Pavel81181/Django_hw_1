from django.http import HttpResponse
import logging
# Create your views here.

logger = logging.getLogger(__name__)
def main(request):
    main = """
            <div>
                <h1>Главная страница</h1>
                <h2>Домашнее задание к уроку №1:</h2>
                <p>Создайте пару представлений в вашем первом приложении:</p>
                <ul>
                    <li>главная</li>
                    <li>о себе</li>
                </ul>
                <p>Внутри каждого представления должна быть переменная html — многострочный текст с HTML-вёрсткой и данными о вашем первом Django-сайте и о вас.</p>
                <p>Сохраняйте в логи данные о посещении страниц.</p>
            </div>
            <form action='http://127.0.0.1:8000/about/' target="_blank">
                <button>О себе</button>
            </form>
            <br>
            <footer>
                <div>
                    <p> Все права защищены </p>
                </div>
            </footer>
            """
    logger.info('Main page accessed')
    return HttpResponse(main)

def about(request):
    about = """
                <div>
                    <h1>Обо мне</h1>
                    <h2>Меня зовут Павел Бажин</h2>
                    <p>Мне 42 года.</p>
                    <p>Я живу в городе Волгоград</p>
                    <p>Работаю директором по маркетингу</p>
                    <p>Учусь на разработчика Python</p>
                </div>
                
                <form action='http://127.0.0.1:8000/' target="_blank">
                <button>На главную</button>
            </form>
            <br>
            <footer>
                <div>
                    <p> Все права защищены </p>
                </div>
            </footer>
                """
    logger.info('About page accessed')
    return HttpResponse(about)