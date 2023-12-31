from __future__ import annotations

from re import Pattern
from typing import Union

import discord
import regex as re
from discord.ext.commands.converter import IDConverter, _get_from_guilds
from discord.ext.commands.errors import BadArgument
from melaniebot.core import commands
from melaniebot.core.commands import BadArgument
from rapidfuzz import process
from unidecode import unidecode

IMAGE_LINKS: Pattern = re.compile(r"(https?:\/\/[^\"\'\s]*\.(?:png|jpg|webp|jpeg|gif|png|svg)(\?size=[0-9]*)?)", flags=re.I)
EMOJI_REGEX: Pattern = re.compile(r"(<(a)?:[a-zA-Z0-9\_]+:([0-9]+)>)")
MENTION_REGEX: Pattern = re.compile(r"<@!?([0-9]+)>")
ID_REGEX: Pattern = re.compile(r"[0-9]{17,}")


def _(x):
    return x


class FuzzyMember(IDConverter):
    """This will accept user ID's, mentions, and perform a fuzzy search for
    members within the guild and return a list of member objects matching
    partial names.

    Guidance code on how to do this from:

    """

    async def convert(self, ctx: commands.Context, argument: str) -> list[discord.Member]:
        bot = ctx.bot
        match = self._get_id_match(argument) or re.match(r"<@!?([0-9]+)>$", argument)
        guild = ctx.guild
        result = []
        if match is None:
            # Not a mention
            if guild:
                result.extend(m[2] for m in process.extract(argument, {m: unidecode(m.name) for m in guild.members}, limit=None, score_cutoff=96))

                result.extend(
                    m[2]
                    for m in process.extract(argument, {m: unidecode(m.nick) for m in guild.members if m.nick and m not in result}, limit=None, score_cutoff=96)
                )

        else:
            user_id = int(match.group(1))
            if guild:
                result.append(guild.get_member(user_id))
            else:
                result.append(_get_from_guilds(bot, "get_member", user_id))

        if not result or result == [None]:
            msg = f'Member "{argument}" not found'
            raise BadArgument(msg)

        return result


class GuildConverter(IDConverter):
    """This is a guild converter for fuzzy guild names which is used throughout
    this cog to search for guilds by part of their name and will also accept
    guild ID's.

    Guidance code on how to do this from:

    """

    async def convert(self, ctx: commands.Context, argument: str) -> discord.Guild:
        bot = ctx.bot
        match = self._get_id_match(argument)
        result = None
        if not await bot.is_owner(ctx.author):
            # Don't need to be snooping other guilds unless we're
            # the bot owner
            return
        if match is None:
            # Not a mention
            for g in process.extractOne(argument, {g: unidecode(g.name) for g in bot.guilds}):
                result = g
        else:
            guild_id = int(match.group(1))
            result = bot.get_guild(guild_id)

        if result is None:
            msg = f'Guild "{argument}" not found'
            raise BadArgument(msg)

        return result


class MultiGuildConverter(IDConverter):
    """This is a guild converter for fuzzy guild names which is used throughout
    this cog to search for guilds by part of their name and will also accept
    guild ID's.

    Guidance code on how to do this from:

    """

    async def convert(self, ctx: commands.Context, argument: str) -> list[discord.Guild]:
        bot = ctx.bot
        match = self._get_id_match(argument)
        result = []
        if not await bot.is_owner(ctx.author):
            # Don't need to be snooping other guilds unless we're
            # the bot owner
            return
        if not match:
            # Not a mention
            result.extend(g[2] for g in process.extract(argument, {g: unidecode(g.name) for g in bot.guilds}, limit=None, score_cutoff=75))

        else:
            guild_id = int(match.group(1))
            if guild := bot.get_guild(guild_id):
                result.append(guild)

            else:
                msg = f'Guild "{argument}" not found'
                raise BadArgument(msg)
        if not result:
            msg = f'Guild "{argument}" not found'
            raise BadArgument(msg)

        return result


class ChannelConverter(IDConverter):
    """This is to convert ID's from a category, voice, or text channel via ID's or
    names.
    """

    async def convert(self, ctx: commands.Context, argument: str) -> Union[discord.TextChannel, discord.CategoryChannel, discord.VoiceChannel]:
        match = self._get_id_match(argument) or re.match(r"<#([0-9]+)>$", argument)
        result = None
        guild = ctx.guild

        if match is None:
            # not a mention
            result = discord.utils.get(guild.channels, name=argument)

        else:
            channel_id = int(match.group(1))
            result = guild.get_channel(channel_id)

        if not result:
            msg = f"Channel `{argument}` not found"
            raise BadArgument(msg)
        return result


class PermissionConverter(IDConverter):
    """This is to convert to specific permission names.

    add_reactions attach_files change_nickname connect
    create_instant_invite deafen_members embed_links external_emojis
    manage_channels manage_messages manage_permissions manage_roles
    manage_webhooks mention_everyone move_members mute_members
    priority_speaker read_message_history read_messages send_messages
    send_tts_messages speak stream use_external_emojis
    use_slash_commands use_voice_activation value view_channel

    """

    async def convert(self, ctx: commands.Context, argument: str) -> str:
        valid_perms = [
            "add_reactions",
            "attach_files",
            "connect",
            "create_instant_invite",
            "deafen_members",
            "embed_links",
            "external_emojis",
            "manage_messages",
            "manage_permissions",
            "manage_roles",
            "manage_webhooks",
            "move_members",
            "mute_members",
            "priority_speaker",
            "read_message_history",
            "read_messages",
            "send_messages",
            "send_tts_messages",
            "speak",
            "stream",
            "use_external_emojis",
            "use_slash_commands",
            "use_voice_activation",
            "view_channel",
        ]
        match = re.match(r"|".join(valid_perms), argument, flags=re.I)

        if result := match.group(0):
            return result
        msg = f"Permission `{argument}` not found"
        raise BadArgument(msg)
