def LearnMaxLevelDataArray(critery):
    # Программный датасет, состоящий из максимальных значений по уровням знаний и труда в зависимости от доступных критерии.
    if critery == "school":
        da = [
            [
                ['BV6', 'BX6', 'BZ6', 'CB6', 'CD6', 'CE6', 'CG6', 'CI6'],
                ['BV7', 'BX7', 'BZ7', 'CB7', 'CD7', 'CE7', 'CG7', 'CI7']
            ],
            [
                ['BW7', 'BY7', 'CA7', 'CC7', 'CF7', 'CH7', 'CJ7'],
                ['BW7', 'BY7', 'CA7', 'CC7', 'CF7', 'CH7', 'CJ7']
            ]
        ]
    elif critery == "high":
        da = [
            [
                ['AF6', 'AH6', 'AJ6', 'AL6', 'AN6', 'AO6', 'AQ6', 'AS6'],
                ['AF7', 'AH7', 'AJ7', 'AL7', 'AN7', 'AO7', 'AQ7', 'AS7']
            ],
            [
                ['AG6', 'AI6', 'AK6', 'AM6', 'AP6', 'AR6', 'AT6'],
                ['AG7', 'AI7', 'AK7', 'AM7', 'AP7', 'AR7', 'AT7']
            ]
        ]
    elif critery == "mba":
        da = [
            [
                ['AU6', 'AW6', 'AY6', 'BA6', 'BC6', 'BD6', 'BF6', 'BH6'],
                ['AU7', 'AW7', 'AY7', 'BA7', 'BC7', 'BD7', 'BF7', 'BH7']
            ],
            [
                ['AV6', 'AX6', 'AZ6', 'BB6', 'BE6', 'BG6', 'BI6'],
                ['AV7', 'AX7', 'AZ7', 'BB7', 'BE7', 'BG7', 'BI7']
            ]
        ]
    elif critery == "estet":
        da = [
            [
                ['Q6', 'S6', 'U6', 'W6', 'Y6', 'Z6', 'AB6', 'AD6'],
                ['Q7', 'S7', 'U7', 'W7', 'Y7', 'Z7', 'AB7', 'AD7']
            ],
            [
                ['R6', 'T6', 'V6', 'X6', 'AA6', 'AC6', 'AE6'],
                ['R7', 'T7', 'V7', 'X7', 'AA7', 'AC7', 'AE7']
            ]
        ]
    elif critery == "degree":
        da = [
            [
                ['B6', 'D6', 'F6', 'H6', 'J6', 'K6', 'M6', 'O6'],
                ['B7', 'D7', 'F7', 'H7', 'J7', 'K7', 'M7', 'O7']
            ],
            [
                ['C6', 'E6', 'G6', 'I6', 'L6', 'N6', 'P6'],
                ['C7', 'E7', 'G7', 'I7', 'L7', 'N7', 'P7']
            ]
        ]

    return da



mls_scc = LearnMaxLevelDataArray("school")

#print(mls_scc[0][0][0])



for rowm, index in mls_scc:

    print('jj')
    print(index)

    #print(rowm[1][0].index(index))

    #print(rowm[1][0].index(index))

    """
    if row['gender'] == "M":
        input_ssc_level = rd[rowm[1][0].index(index)].value
    if row['gender'] == "F":
        input_ssc_level = rd[rowm[0][0].index(index)].value

    maxlevelbalance = 100 - input_ssc_level #Получает баланс уровня от максимального уровня критерии
    userlevelbalance = 100 - row['ssc_p']

    if maxlevelbalance > userlevelbalance:
        levelbalance = maxlevelbalance - userlevelbalance #Подсчитываем баланс от уровня

    if maxlevelbalance < userlevelbalance:
        levelbalance = userlevelbalance - maxlevelbalance

    for rowms, index in mlsb.iterrows():
        if levelbalance == rowms[index] or levelbalance > rowms[index]:
            # Если текущий баланс уровня соответствует нужным критериям, то система для списка успешных выпускников оставит уровень школьных знании, которого добился выпускник
            #sgl['profile']['info']['school'] = row['ssc_p']
            pass

"""