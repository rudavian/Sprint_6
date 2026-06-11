# Sprint_6

Автотесты для сервиса Яндекс.Самокат.

Стек: Python, pytest, Selenium, Allure.

## Установка зависимостей

```bash
pip install -r requirements.txt
```

## Запуск всех тестов

```bash
python -m pytest tests -v
```

## Запуск с генерацией Allure-results

```bash
python -m pytest tests --alluredir=allure_results
```

## Просмотр Allure-отчёта

```bash
allure serve allure_results
```
