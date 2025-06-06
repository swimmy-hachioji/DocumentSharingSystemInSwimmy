""" HumanIO.Structure.Main
Human interface classのStructureを提供します。

DSSSが利用する全てのHuman interface classは、ここで定義される[HumanIOStructure]を継承しているものとする。
また、HumanIOに関する処理のみを変更する場合、このファイルの所属している[HumanIO]ライブラリ内で完結するものとする。
"""


""" Imports """


from abc import ABC, abstractmethod

from . import Event


"""
    HumanIO
"""


""" Structure """


class Structure(ABC):
    """ HumanIO structure """

    """ Initializer """

    def __init__(
            self,
    ) -> None:
        """ Initialize IO settings """
        return

    """ Event """
    __events: list[Event.EventStructure]
    @property
    def events(self) -> tuple[Event.EventStructure]:

    """ Execute """

    async def __mainloop__(self):
        """ HumanIO mainloop """
        return

    def exe(self):
        """ Start mainloop """
        return

    ...
