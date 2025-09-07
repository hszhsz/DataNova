# 🚀 DataNova Web UI

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> Создано на базе открытого кода, возвращено в открытый код.

Это веб-интерфейс для [`DataNova`](https://github.com/hszhsz/DataNova).

## Быстрый старт

### Предварительные требования

- [`DataNova`](https://github.com/hszhsz/DataNova)
- Node.js (v22.14.0+)
- pnpm (v10.6.2+) как менеджер пакетов

### Конфигурация

Создайте файл `.env` в корне проекта и настройте следующие переменные окружения:

- `NEXT_PUBLIC_API_URL`: URL API DataNova.

Всегда лучше начать с примера файла и отредактировать файл `.env` со своими значениями:

```bash
cp .env.example .env
```

## Как установить

DataNova Web UI использует `pnpm` как менеджер пакетов.
Для установки зависимостей выполните:

```bash
cd web
pnpm install
```

## Как запустить в режиме разработки

> [!ПРИМЕЧАНИЕ]
> Убедитесь, что сервис Python API запущен перед запуском веб-интерфейса.

Запустите сервер разработки веб-интерфейса:

```bash
cd web
pnpm dev
```

По умолчанию веб-интерфейс будет доступен по адресу `http://localhost:3000`.

Вы можете установить переменную окружения `NEXT_PUBLIC_API_URL`, если используете другой хост или расположение.

```ini
# .env
NEXT_PUBLIC_API_URL=http://localhost:8000/api
```

## Docker

Вы также можете запустить этот проект с помощью Docker.

Сначала прочитайте [конфигурацию](#конфигурация) ниже. Убедитесь, что файл `.env` готов.

Во-вторых, чтобы собрать образ Docker вашего веб-сервера:

```bash
docker build --build-arg NEXT_PUBLIC_API_URL=YOUR_DATANOVA_API -t datanova-web .
```

Наконец, запустите контейнер Docker с веб-сервером:

```bash
# Замените datanova-web-app на предпочитаемое вами имя контейнера
docker run -d -t -p 3000:3000 --env-file .env --name datanova-web-app datanova-web

# остановить сервер
docker stop datanova-web-app
```

### Docker Compose

Вы также можете настроить этот проект с помощью docker compose:

```bash
# сборка образа docker
docker compose build

# запуск сервера
docker compose up
```

## Лицензия

Этот проект с открытым исходным кодом доступен по [лицензии MIT](../LICENSE).

## Благодарности

Мы выражаем искреннюю благодарность сообществу открытого исходного кода за их бесценный вклад.
DataNova построен на фундаменте этих выдающихся проектов:

В частности, мы хотим выразить глубокую признательность:

- [Next.js](https://nextjs.org/) за их исключительный фреймворк
- [Shadcn](https://ui.shadcn.com/) за их минималистичные компоненты, которые питают наш интерфейс
- [Zustand](https://zustand.docs.pmnd.rs/) за их потрясающее управление состоянием
- [Framer Motion](https://www.framer.com/motion/) за их удивительную библиотеку анимации
- [React Markdown](https://www.npmjs.com/package/react-markdown) за их исключительный рендеринг markdown и настраиваемость
- И наконец, особая благодарность [SToneX](https://github.com/stonexer) за его большой вклад в [визуальный эффект токен-за-токеном](./src/core/rehype/rehype-split-words-into-spans.ts)

Эти выдающиеся проекты формируют основу DataNova и демонстрируют трансформирующую силу сотрудничества в открытом исходном коде.