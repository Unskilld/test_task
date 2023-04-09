def bytes_swapper_version_one(number: int) -> int:
    """
    В этой версии сразу переводим число в байты, меняем байты местами и возвращаем число из полученных байтов
    """
    bytes_version = number.to_bytes(length=2)
    reversed_bytes_version = bytes_version[1:] + bytes_version[:1]
    return int.from_bytes(reversed_bytes_version)


def bytes_swapper_version_two(number: int) -> int:
    """
    В этой версии работаем с бинарной формой числа. Сразу переводим его в бинарный вид, потом слева дополняем нулями до
    16 цифр, после чего меняем первые и последние 8 местами и переводим получившуюся строку обратно в число
    с основанием 2.
    """
    binary_form = bin(number)
    string_form = str(binary_form)[2:].rjust(16, '0')
    reversed_string_form = string_form[8:] + string_form[:8]
    return int(reversed_string_form, 2)
