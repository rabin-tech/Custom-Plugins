"A Checker Plugin Made By Geda Gang"

from pyrogram.errors.exceptions.bad_request_400 import YouBlockedUser

from userge import userge, Message
from userge.utils.exceptions import StopConversation


@userge.on_cmd("bin", about={
    'header': "Bin Lookup",
    'usage': "{tr}bin [Enter bin]\n"})

async def bin(message: Message):
    """ Use to Lookup for a Bin"""
    replied = message.input_str
    if not replied:
        await message.err("```Enter a bin after the command....```", del_in=5)
        return
    chat = "@urcpbot"
    await message.edit("```Getting info, Wait plox ...```")
    msgs = []
    ERROR_MSG = "For your kind information, you blocked bot, Unblock it"
    try:
        async with userge.conversation(chat) as conv:
            try:
                await conv.send_message("!bin {}".format(replied))
            except YouBlockedUser:
                await message.err(f"**{ERROR_MSG}**", del_in=5)
                return
            msgs = await conv.get_response(timeout=5, mark_read=True)
    except StopConversation:
        pass

    try:
        await message.edit(f"`{msgs.text}`")
    except AttributeError:
        await message.edit(f"`It took a lot time to respond!`", del_in=5)
    # for msg in msgs:
    #     await message.edit(f"`{msg.text}`")


@userge.on_cmd("vbv", about={
    'header': "Bin Vbv Lookup",
    'usage': "{tr}vbv [Enter full card in format]\n"})

async def vbv(message: Message):
    """ Use to Lookup Whether a bin is VBV/MSC or not"""
    replied = message.input_str
    if not replied:
        await message.err("```Enter a card after the command....```", del_in=5)
        return
    chat = "@Carol5_bot"
    await message.edit("```Getting info, Wait plox ...```")
    msgs = ''
    ERROR_MSG = "For your kind information, you blocked bot, Unblock it"

    if str(replied[:1]) in ['3','6']:
        await message.err("```Only visa and MasterCard Supported```", del_in=5) 
        return 

    try:
        async with userge.conversation(chat) as conv:
            try:
                await conv.send_message("!vbv {}".format(replied))
            except YouBlockedUser:
                await message.err(f"**{ERROR_MSG}**", del_in=5)
                return
            msgs = await conv.get_response(timeout=50, mark_read=True)
    except StopConversation:
        pass

    try:
        response = msgs.text.rsplit("\n",3)[0]
        await message.edit(f"`{response}`")
    except AttributeError:
        await message.edit(f"`It took a lot time to respond!`", del_in=5)


@userge.on_cmd("b3", about={
    'header': "Check whether the card is live or not in Braintree Gate",
    'usage': "{tr}b3 [Enter full card in format]\n"})

async def b3(message: Message):
    """ To check whether the card is live or not in Braintree"""
    replied = message.input_str
    if not replied:
        await message.err("```Enter a card after the command....```", del_in=5)
        return
    chat = "@Carol5_bot"
    await message.edit("```Getting info, Wait plox ...```")
    msgs = ''
    ERROR_MSG = "For your kind information, you blocked bot, Unblock it"

    try:
        async with userge.conversation(chat) as conv:
            try:
                await conv.send_message("!b3 {}".format(replied))
            except YouBlockedUser:
                await message.err(f"**{ERROR_MSG}**", del_in=5)
                return
            msgs = await conv.get_response(timeout=40, mark_read=True)
    except StopConversation:
        pass

    try:
        await message.edit(f"`{msgs.text}`")
    except AttributeError:
        await message.edit(f"`It took a lot time to respond!`", del_in=5)



@userge.on_cmd("cpp", about={
    'header': "Check whether the card is live or not in stripe-auth Gate",
    'usage': "{tr}cpp [Enter full card in format]\n"})

async def cpp(message: Message):
    """ To check whether the card is live or not in stripe-auth Gate"""
    replied = message.input_str
    if not replied:
        await message.err("```Enter a card after the command....```", del_in=5)
        return
    chat = "@SyntaxChkBot"
    await message.edit("```Getting info, Wait plox ...```")
    msgs = ''
    ERROR_MSG = "For your kind information, you blocked bot, Unblock it"

    try:
        async with userge.conversation(chat) as conv:
            try:
                await conv.send_message("!chk1 {}".format(replied))
            except YouBlockedUser:
                await message.err(f"**{ERROR_MSG}**", del_in=5)
                return
            msgs = await conv.get_response(timeout=50, mark_read=True)
    except StopConversation:
        pass

    try:       
        response = msgs.text.rsplit("\n",4)[0]
        await message.edit(f"`{response}`")
    except AttributeError:
        await message.edit(f"`It took a lot time to respond!`", del_in=5)



@userge.on_cmd("ss", about={
    'header': "Check the card in stripity-stripe auth",
    'usage': "{tr}ccn [Enter full card in format]\n"})

async def ss(message: Message):
    """ To Check the card in stripity-stripe auth"""
    replied = message.input_str
    if not replied:
        await message.err("```Enter a card after the command....```", del_in=5)
        return
    chat = "@Carol5_bot"
    await message.edit("```Getting info, Wait plox ...```")
    msgs = ''
    ERROR_MSG = "For your kind information, you blocked bot, Unblock it"

    try:
        async with userge.conversation(chat) as conv:
            try:
                await conv.send_message("!ss {}".format(replied))
            except YouBlockedUser:
                await message.err(f"**{ERROR_MSG}**", del_in=5)
                return
            msgs = await conv.get_response(timeout=50, mark_read=True)
    except StopConversation:
        pass

    try:
        response = msgs.text.rsplit("\n",3)[0]
        await message.edit(f"`{response}`")
    except AttributeError:
        await message.edit(f"`It took a lot time to respond!`", del_in=5)



@userge.on_cmd("csk", about={
    'header': "Check whether the sk is live or not",
    'usage': "{tr}csk [Enter full card in format]\n"})

async def csk(message: Message):
    """ To check whether the sk is live or not"""
    replied = message.input_str
    if not replied:
        await message.err("```Enter a card after the command....```", del_in=5)
        return
    chat = "@uNiqueko_bot"
    await message.edit("```Getting info, Wait plox ...```")
    msgs = ''
    ERROR_MSG = "For your kind information, you blocked bot, Unblock it"

    try:
        async with userge.conversation(chat) as conv:
            try:
                await conv.send_message("!csk {}".format(replied))
            except YouBlockedUser:
                await message.err(f"**{ERROR_MSG}**", del_in=5)
                return
            msgs = await conv.get_response(timeout=50, mark_read=True)
    except StopConversation:
        pass

    try:
        await message.edit(f"`{msgs.text}`")
    except AttributeError:
        await message.edit(f"`It took a lot time to respond!`", del_in=5)



@userge.on_cmd("chk", about={
    'header': "Check whether the cc is live or not in checkout",
    'usage': "{tr}chk [Enter full card in format]\n"})

async def chk(message: Message):
    """ To check whether the cc is live or not in checkout"""
    replied = message.input_str
    if not replied:
        await message.err("```Enter a card after the command....```", del_in=5)
        return
    chat = "@Drexzo_bot"
    await message.edit("```Getting info, Wait plox ...```")
    msgs = ''
    ERROR_MSG = "For your kind information, you blocked bot, Unblock it"

    try:
        async with userge.conversation(chat) as conv:
            try:
                await conv.send_message("!chk {}".format(replied))
            except YouBlockedUser:
                await message.err(f"**{ERROR_MSG}**", del_in=5)
                return
            msgs = await conv.get_response(timeout=50, mark_read=True)
    except StopConversation:
        pass

    try:
        await message.edit(f"`{msgs.text}`")
    except AttributeError:
        await message.edit(f"`It took a lot time to respond!`", del_in=5)



@userge.on_cmd("binn", about={
    'header': "Bin Lookup 2",
    'usage': "{tr}bin [Enter bin]\n"})

async def binn(message: Message):
    """ Use to Lookup for a Bin 2"""
    replied = message.input_str
    if not replied:
        await message.err("```Enter a bin after the command....```", del_in=5)
        return
    chat = "@Dedsec_sam_chkbot"
    await message.edit("```Getting info, Wait plox ...```")
    msgs = []
    ERROR_MSG = "For your kind information, you blocked bot, Unblock it"
    try:
        async with userge.conversation(chat) as conv:
            try:
                await conv.send_message("!bin {}".format(replied))
            except YouBlockedUser:
                await message.err(f"**{ERROR_MSG}**", del_in=5)
                return
            msgs = await conv.get_response(timeout=5, mark_read=True)
    except StopConversation:
        pass

    try:
        await message.edit(f"`{msgs.text}`")
    except AttributeError:
        await message.edit(f"`It took a lot time to respond!`", del_in=5)


@userge.on_cmd("pp", about={
    'header': "Check whether the cc is live or not in paypal",
    'usage': "{tr}bin [Enter card]\n"})

async def pp(message: Message):
    """ Use to check cc in paypal"""
    replied = message.input_str
    if not replied:
        await message.err("```Enter a cc after the command....```", del_in=5)
        return
    chat = "@Carol5_bot"
    await message.edit("```Getting info, Wait plox ...```")
    msgs = []
    ERROR_MSG = "For your kind information, you blocked bot, Unblock it"
    try:
        async with userge.conversation(chat) as conv:
            try:
                await conv.send_message("!pp {}".format(replied))
            except YouBlockedUser:
                await message.err(f"**{ERROR_MSG}**", del_in=5)
                return
            msgs = await conv.get_response(timeout=50, mark_read=True)
    except StopConversation:
        pass

    try:
        response = msgs.text.rsplit("\n",3)[0]
        await message.edit(f"`{response}`")
    except AttributeError:
        await message.edit(f"`It took a lot time to respond!`", del_in=5)


@userge.on_cmd("au", about={
    'header': "Check whether the cc is live or not in authorize",
    'usage': "{tr}bin [Enter card]\n"})

async def au(message: Message):
    """ Use to check cc in authorize"""
    replied = message.input_str
    if not replied:
        await message.err("```Enter a cc after the command....```", del_in=5)
        return
    chat = "@Carol5_bot"
    await message.edit("```Getting info, Wait plox ...```")
    msgs = []
    ERROR_MSG = "For your kind information, you blocked bot, Unblock it"
    try:
        async with userge.conversation(chat) as conv:
            try:
                await conv.send_message("!au {}".format(replied))
            except YouBlockedUser:
                await message.err(f"**{ERROR_MSG}**", del_in=5)
                return
            msgs = await conv.get_response(timeout=5, mark_read=True)
    except StopConversation:
        pass

    try:
        response = msgs.text.rsplit("\n",3)[0]
        await message.edit(f"`{response}`")
    except AttributeError:
        await message.edit(f"`It took a lot time to respond!`", del_in=5)



@userge.on_cmd("link", about={
    'header': "movie/series link Lookup",
    'usage': "{tr}link [Enter name]\n"})

async def link(message: Message):
    """ Use to Lookup for a movie/series link"""
    replied = message.input_str
    replied = replied.replace(" ", "%20")
    if not replied:
        await message.err("```Enter a movie/series name after the command....```", del_in=5)
        return
    await message.edit("<a href='https://witcher.lalbaake456.workers.dev/0:search?q={}'>Click Here Bitch</a>".format(replied))
