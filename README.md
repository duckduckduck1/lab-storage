# lab-storage

Веб-хранилище для данных лаборатории.

## Установка зависимостей

### Production

Установка только runtime-зависимостей:

```bash
python -m pip install -r requirements.txt
```

### Разработка

Установка runtime- и development-зависимостей:

```bash
python -m pip install -r requirements-dev.txt
```

`requirements-dev.txt` подключает `requirements.txt` через `-r`, поэтому
разработчику достаточно второй команды.
