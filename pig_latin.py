"""
Program to translate the word to pig latin
"""


def translate_to_pg(WRD):
    """
    Description: TRnslate to pig latin

    INPUT: {Type - String} WRD

    RETURNS: {String} trslated WRD
    """
    if WRD[0] in 'aeiou':
        return WRD.__add__('ay')
    return WRD[1:].__add__(WRD[0]).__add__('ay')


if __name__ == '__main__':
    WORD = input('Enter the word to be transalated: ')
    print(translate_to_pg(WORD))
