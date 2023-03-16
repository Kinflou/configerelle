# Standard Imports

# Local Imports

# External Imports


class Navigator:

    @property
    def inner(self) -> dict:
        return self.__inner

    @property
    def previous_index(self) -> str:
        raise NotImplementedError
        # return pre(self.current_index)

    @property
    def previous_item(self) -> str:
        return self.__inner[self.previous_index]

    @property
    def current_index(self) -> str:
        return self.__current

    @current_index.setter
    def current_index(self, value: str):
        self.__current = value

    @property
    def current_item(self):
        try:
            return self[self.__current]
        except KeyError:
            return None

    @current_item.setter
    def current_item(self, value):
        self[self.current_index] = value

    def next_idx(self, part: str):
        self.current_index = next_idx(self, part)

    @property
    def parent_index(self) -> str:
        return parent_idx(self.current_index)

    @property
    def parent_item(self):
        return self.__inner[self.parent_index]

    def __init__(self, value, delimiter: chr = '.', index_raises: bool = True):
        super().__init__()

        self.delimiter = delimiter

        if not value:
            self.__inner = value
        else:
            self.__inner = value

        self.index_raises = index_raises

        self.__current: str | None = None

    def __str__(self):
        return str(self.__inner)

    def __getitem__(self, key: str | list[str | int] | None):
        if not key:
            return self.__inner

        keys = canon_keys(key, self.delimiter)
        val = self.__inner

        navigated = []
        for k in keys:
            if isinstance(val, list):
                if not isinstance(k, int):
                    if self.index_raises:
                        raise IndexError(f'Cannot index at {literal_key(navigated, delimiter=self.delimiter)}'
                                         f' list with a string, try a decimal number')

                    return None

                if k >= len(val):
                    if self.index_raises:
                        raise IndexError(f'Tried to index at {k} but the list only has {len(val)} items')

                    return None

                val = val[k]

            elif isinstance(val, dict):
                if k not in val:
                    if self.index_raises:
                        if not navigated:
                            raise KeyError(f"No value exists for key '{keys[keys.index(k)]}'")
                        else:
                            raise KeyError(f"No value exists for key"
                                           f" '{keys[keys.index(k)]}'"
                                           f" at '{literal_key(navigated, delimiter=self.delimiter)}'")

                    return None

                val = val.get(k, None)
            else:
                if self.index_raises:
                    raise IndexError(f"Cannot index at '{literal_key(navigated, delimiter=self.delimiter)}'"
                                     f" with '{keys[keys.index(k)]}'"
                                     f" since its not a set or collection")

                return None

            navigated.append(k)

        return val

    def __setitem__(self, key: str | list[str | int], value):
        keys = canon_keys(key, self.delimiter)

        if not keys:
            self.__inner = value
            self.current_index = key
            return

        reach = keys_reach_until(self, keys)
        missing = keys[len(reach):len(keys)]

        if len(reach) < len(keys) - 1:
            self.current_index = literal_key(reach, delimiter=self.delimiter)

            for idx in range(len(missing)):
                k = missing[idx]

                if isinstance(k, str):
                    self.next(k, return_index=True)
                    self[self.current_index] = {}
                elif isinstance(k, int):
                    self.next(k, return_index=True)
                    self[self.current_index] = []

        set_at(self, keys, value)
        self.current_index = literal_key(keys, self.delimiter)

    def back(self) -> 'Navigator':
        self.current_index = self.parent_index

        return self

    def next(self, part: str, return_index: bool = False) -> str:
        if not self.current_index:
            self.current_index = part
        else:
            self.current_index = f'{self.current_index}{self.delimiter}{part}'

        if return_index:
            return self.current_index

        return self.current_item

    def next_with(self, part: str, value):
        if not self.current_index:
            self.current_index = part
        else:
            self.current_index = f'{self.current_index}{self.delimiter}{part}'

    def last(self):
        if not isinstance(self.current_item, list):
            return None

        return f'{self.current_index}{self.delimiter}{len(self.current_item) - 1}'

    def parent_last_item_index(self, part: str):
        return last_idx(self, self.current_index, part)


def canon_keys(key: str | list[str], delimiter) -> list[str, int]:
    if key is None:
        return []

    if isinstance(key, str):
        keys = key.split(delimiter)
    elif isinstance(key, list):
        keys = key
    else:
        raise TypeError

    c = []

    for k in keys:
        if k.isdecimal():
            c.append(int(k))
        else:
            c.append(k)

    return c


def literal_key(keys: list[str | int], delimiter: chr) -> str:
    return delimiter.join([str(k) for k in keys])


def missing_until(navigator: Navigator, keys: list[str | int]) -> list[str | int]:
    until = keys_reach_until(navigator, keys)
    return keys[:len(until)]


def keys_reach_until(navigator: Navigator, keys: list[str]) -> list[str | int]:
    val = navigator.inner

    navigated = []
    for k in keys:
        if isinstance(val, list):
            if not isinstance(k, int):
                break

            if k >= len(val):
                break

            val = val[k]

        elif isinstance(val, dict):
            if k not in val:
                break

            val = val.get(k, None)
        else:
            break

        navigated.append(k)

    return navigated


def set_at(navigator: Navigator, keys: list[str | int], value):
    current = navigator.inner

    navigated = []
    for k in keys[:-1]:
        if isinstance(current, list):
            if not isinstance(k, int):
                if navigator.index_raises:
                    raise IndexError(f'Cannot index at {literal_key(navigated, delimiter=navigator.delimiter)}'
                                     f' list with a string, try a decimal number')

                return None

            if k >= len(current):
                if navigator.index_raises:
                    raise IndexError(f'Tried to index at {k} but the list only has {len(current)} items')

                return None

            current = current[k]

        elif isinstance(current, dict):
            if k not in current:
                if navigator.index_raises:
                    raise KeyError(f"No value exists for key '{keys[keys.index(k)]}'"
                                   f" at '{literal_key(navigated, delimiter=navigator.delimiter)}'")

                return None

            current = current.get(k, None)
        else:
            if navigator.index_raises:
                raise IndexError(f"Cannot index at '{literal_key(navigated, delimiter=navigator.delimiter)}'"
                                 f" since its not a set or collection")

            return None

        navigated.append(k)

    if len(keys) < 1:
        navigator.__inner = value
        return

    final_key = keys[-1]
    current[final_key] = value


def next_idx(navigator: Navigator, new) -> str:
    if not navigator.current_index:
        return new

    return navigator.current_index + '.' + new


def parent_idx(child: str | None = None) -> str | None:
    if child:
        parts = child.split('.')
    else:
        return None

    return '.'.join(parts[:-1]) or None


def last_idx(navigator: Navigator, index: str, part: str) -> int | None:
    parent = parent_idx(index)
    val = navigator[parent].get(part, None)

    if not val:
        return None

    vals = navigator[parent][part]

    if not vals:
        return None

    return len(vals) - 1


def last(navigator: Navigator, rule) -> dict | None:
    parent = navigator.parent_index
    name = rule.__name__
    val = navigator[parent].get(name, None)

    if not val:
        return None

    vals = navigator[parent][name]

    if not vals:
        return None

    return navigator[parent][name][-1]


