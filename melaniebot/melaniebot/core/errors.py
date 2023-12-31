from __future__ import annotations

import importlib.machinery

import discord

from melaniebot.core.utils.chat_formatting import humanize_number


def _(x):
    return x


class RedError(Exception):
    """Base error class for Melanie-related errors."""


class PackageAlreadyLoaded(RedError):
    """Raised when trying to load an already-loaded package."""

    def __init__(self, spec: importlib.machinery.ModuleSpec, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.spec: importlib.machinery.ModuleSpec = spec

    def __str__(self) -> str:
        return f"There is already a package named {self.spec.name.split('.')[-1]} loaded"


class CogLoadError(RedError):
    """Raised by a cog when it cannot load itself.

    The message will be sent to the user.

    """


class BankError(RedError):
    """Base error class for bank-related errors."""


class BalanceTooHigh(BankError, OverflowError):
    """Raised when trying to set a user's balance to higher than the maximum."""

    def __init__(self, user: discord.abc.User, max_balance: int, currency_name: str, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.user = user
        self.max_balance = max_balance
        self.currency_name = currency_name

    def __str__(self) -> str:
        return f"{self.user}'s balance cannot rise above {humanize_number(self.max_balance)} {self.currency_name}."


class BankPruneError(BankError):
    """Raised when trying to prune a local bank and no server is specified."""


class MissingExtraRequirements(RedError):
    """Raised when an extra requirement is missing but required."""


class ConfigError(RedError):
    """Error in a Config operation."""


class StoredTypeError(ConfigError, TypeError):
    """A TypeError pertaining to stored Config data.

    This error may arise when, for example, trying to increment a value
    which is not a number, or trying to toggle a value which is not a
    boolean.

    """


class CannotSetSubfield(StoredTypeError):
    """Tried to set sub-field of an invalid data structure.

    This would occur in the following example::

        >>> import asyncio
        >>> from melaniebot.core import Config
        >>> config = Config.get_conf(None, 1234, cog_name="Example")
        >>> async def example():
        ...     await config.foo.set(True)
        ...     await config.set_raw("foo", "bar", False)  # Should raise here
        ...
        >>> asyncio.run(example())

    """
