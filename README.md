# Автоматизоване тестування UI - Spotify Web Player

Цей проєкт містить автоматизовані тести для веб-застосунку Spotify, реалізовані в межах Лабораторної роботи №2.

## Стек технологій
- **Мова:** Python 3.12
- **Фреймворк:** Pytest
- **Інструментарій:** Selenium WebDriver, webdriver-manager

## Реалізовані сценарії
1. **Search Functional:** Перевірка коректності роботи пошуку за ключовим словом (Imagine Dragons).
2. **Page Load:** Перевірка успішного завантаження головної сторінки та наявності основних елементів інтерфейсу.

## Як запустити
1. Встановити залежності: `pip install -r requirements.txt`
2. Запустити тести: `pytest test_spotify_ui.py --html=report.html --self-contained-html`
