
def merge_dicts_auto(dict1, dict2, strategy=None, verbose=False):
    result = dict(dict1)  # создаём копию первого словаря

    for key in dict2:
        val1 = result.get(key)       # значение из dict1 (если есть)
        val2 = dict2[key]            # значение из dict2

        # Кастомная стратегия, если определена для ключа
        if strategy and key in strategy:
            action = strategy[key]  # достаём функцию из strategy
            if callable(action):
                result[key] = action(val1, val2)  # применяем стратегию
                if verbose:
                    print(f"[strategy] Ключ '{key}': пользовательская функция -> {result[key]}")
                continue

        # Автоматическая стратегия по типам данных
        if key in result:
            if isinstance(val1, (int, float)) and isinstance(val2, (int, float)):
                result[key] = val1 + val2  # если числа — складываем
                if verbose:
                    print(f"[sum] Ключ '{key}': {val1} + {val2} = {result[key]}")
            elif isinstance(val1, list) and isinstance(val2, list):
                result[key] = val1 + val2  # если списки — объединяем
                if verbose:
                    print(f"[list] Ключ '{key}': {val1} + {val2} = {result[key]}")
            elif isinstance(val1, dict) and isinstance(val2, dict):
                result[key] = merge_dicts_auto(val1, val2, strategy, verbose)  # рекурсивно объединяем вложенные словари
                if verbose:
                    print(f"[dict] Ключ '{key}': объединение вложенных словарей")
            elif isinstance(val1, set) and isinstance(val2, set):
                result[key] = val1 | val2  # если множества — объединяем
                if verbose:
                    print(f"[set] Ключ '{key}': {val1} | {val2} = {result[key]}")
            else:
                result[key] = val2  # если разные типы — заменяем значением из dict2
                if verbose:
                    print(f"[replace] Ключ '{key}': заменено на {val2}")
        else:
            result[key] = val2  # ключ был только в dict2
            if verbose:
                print(f"[new] Ключ '{key}' добавлен со значением {val2}")

    return result
