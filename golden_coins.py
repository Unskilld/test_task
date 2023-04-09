def where_are_fake_coins(amount_of_buckets: int, real_coins_weight: int, delta_between_real_and_fake: int,
                         weight_of_all_taken_coins: int) -> int:
    """
    Сразу считаем сумму, которая бы получилась, если бы все монеты были настоящими. После этого отнимаем от этой суммы
    реальную сумму, взятую из мешочков. После этого делим получившееся число на разницу между настоящими и ненастоящими
    монетами, получившееся число укажет на мещочек с ненастоящими монетами
    """
    weight_if_all_coins_are_real = sum(
        range(real_coins_weight, amount_of_buckets * real_coins_weight, real_coins_weight))
    delta_between_ideal_and_real_weight = weight_if_all_coins_are_real - weight_of_all_taken_coins
    return int(delta_between_ideal_and_real_weight / delta_between_real_and_fake)
