""" HumanIO.Structure.Event
Human interface classのEventを提供します。
"""


""" Imports """


""" functools """


def gen_private_member(cls: type, key: str) -> str:
    """ TODO: Replace CodingTools.Functools.private_member function """
    return f"_{cls.__name__}{key}"

def gen_value_member(cls: type, key: str) -> str:
    """ TODO: Replace CodingTools.Functools.gen_value_member function """
    if key[:2] == "__": return gen_private_member(cls, key)
    return key


""" class tools """


class Constants:
    """ TODO: Replace CodingTools.BasicStructure.DataClass.Constants class """
    ...


"""
    HumanIO event system
"""


""" Event structure class """


class EventStructure(object):
    """ Event structure class """

    """ Initialize """
    __args__: tuple[str] = ()
    __kwargs__: dict[str, str] = {}

    def __repr__(self):
        args = ", ".join(
            repr(getattr(self, gen_value_member(self.__class__, value_name)))
            for value_name in self.__args__
        )
        kwargs = ", ".join(
            f"{key}={repr(getattr(self, gen_value_member(self.__class__, value_name)))}"
            for key, value_name in self.__kwargs__.items()
        )
        args_text = ", ".join(
            arg_text
            for arg_text in (args, kwargs)
            if not len(arg_text) == 0
        )
        return f"{self.__class__.__name__}({args_text})"

    """ Text """
    def __str__(self):
        return self.__repr__()

    """ Settings """

    def __hash__(self):
        return hash(self.__class__.__name__)

    def __eq__(self, other):
        if isinstance(other, type):
            return self.__class__ == other
        elif isinstance(other, EventStructure):
            return self.__class__ == other.__class__
        elif isinstance(other, str):
            return self.__class__.__name__ == other
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    ...


""" Events """


# Mouse


class Mouse(Constants):
    """ Mouse constants class """
    RIGHT: str = "right"
    LEFT: str = "left"
    WHEEL: str = "wheel"
    ...


class MousePressed(EventStructure):
    """ Mouse pressed event """

    """ Initialize """
    def __init__(self, _button: str):
        """ Initialize settings """
        self.__args__ = ("__button", )

        self.__button = _button
        return

    """ Settings """
    __button: str
    @property
    def button(self) -> str: return self.__button

    def __hash__(self):
        return hash((self.__class__.__name__, self.__button))

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__button == other.__button
        elif isinstance(other, str):
            return self.__button == other
        return False

    ...


class MouseMove(EventStructure):
    """ Mouse move event """

    """ Initialize """
    def __init__(self, _mouse_move_dist: tuple[int, int]):
        """ Initialize settings """
        self.__args__ = ("__move_dist", )

        self.__move_dist = tuple(_mouse_move_dist)
        return

    """ Settings """
    __move_dist: tuple[int, int]
    @property
    def move_dist(self) -> tuple[int, int]: return self.__move_dist

    def __hash__(self):
        return hash(self.__move_dist)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__move_dist == other.__move_dist
        elif isinstance(other, tuple):
            return self.__move_dist == other
        return False

    def __gt__(self, other):
        """ TODO: Create compair functions """
        pass

    ...


# Keyboard


class KeyPressed(EventStructure):
    """ Key pressed event """

    """ Initialize """
    def __init__(self, _key: str):
        """ Initialize settings """
        self.__args__ = ("__key", )

        self.__key = _key
        return

    """ Settings """
    __key: str
    @property
    def key(self) -> str: return self.__key

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__key == other.__key
        elif isinstance(other, str):
            return self.__key == other
        return False

    ...
