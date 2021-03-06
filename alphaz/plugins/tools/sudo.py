""" setup sudos """

# alfareza

import asyncio

from pyrogram.errors.exceptions.bad_request_400 import PeerIdInvalid

from userge import alphaz, Message, Config, get_collection

SAVED_SETTINGS = get_collection("CONFIGS")
SUDO_USERS_COLLECTION = get_collection("sudo_users")
SUDO_CMDS_COLLECTION = get_collection("sudo_cmds")


async def _init() -> None:
    s_o = await SAVED_SETTINGS.find_one({'_id': 'SUDO_ENABLED'})
    if s_o:
        Config.SUDO_ENABLED = s_o['data']
    async for i in SUDO_USERS_COLLECTION.find():
        Config.SUDO_USERS.add(i['_id'])
    async for i in SUDO_CMDS_COLLECTION.find():
        Config.ALLOWED_COMMANDS.add(i['_id'])


@alphaz.on_cmd("sudo", about={'header': "enable / disable sudo access"}, allow_channels=False)
async def sudo_(message: Message):
    """ enable / disable sudo access """
    if Config.SUDO_ENABLED:
        Config.SUDO_ENABLED = False
        await message.edit("`sudo disabled !`", del_in=3)
    else:
        Config.SUDO_ENABLED = True
        await message.edit("`sudo enabled !`", del_in=3)
    await SAVED_SETTINGS.update_one(
        {'_id': 'SUDO_ENABLED'}, {"$set": {'data': Config.SUDO_ENABLED}}, upsert=True)


@alphaz.on_cmd("addsudo", about={
    'header': "tambahkan pengguna sudo",
    'usage': "{tr}addsudo [username | reply to msg]"}, allow_channels=False)
async def add_sudo(message: Message):
    """ tambahkan pengguna sudo """
    user_id = message.input_str
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
    if not user_id:
        await message.err(f'user: `{user_id}` not found!')
        return
    if isinstance(user_id, str) and user_id.isdigit():
        user_id = int(user_id)
    try:
        user = await message.client.get_user_dict(user_id)
    except PeerIdInvalid as p_e:
        await message.err(p_e)
        return
    if user['id'] in Config.SUDO_USERS:
        await message.edit(f"user : `{user['id']}` sudah di **SUDO**!", del_in=5)
    else:
        Config.SUDO_USERS.add(user['id'])
        await asyncio.gather(
            SUDO_USERS_COLLECTION.insert_one({'_id': user['id'], 'men': user['mention']}),
            message.edit(f"user : `{user['id']}` added to **SUDO**!", del_in=5, log=__name__))


@alphaz.on_cmd("delsudo", about={
    'header': "hapus pengguna sudo",
    'flags': {'-all': "remove all sudo users"},
    'usage': "{tr}delsudo [user_id | reply to msg]\n{tr}delsudo -all"}, allow_channels=False)
async def del_sudo(message: Message):
    """ hapus pengguna sudo """
    if '-all' in message.flags:
        Config.SUDO_USERS.clear()
        await asyncio.gather(
            SUDO_USERS_COLLECTION.drop(),
            message.edit("**SUDO** pengguna dihapus!", del_in=5))
        return
    user_id = message.filtered_input_str
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
    if not user_id:
        await message.err(f'user: `{user_id}` not found!')
        return
    if isinstance(user_id, str) and user_id.isdigit():
        user_id = int(user_id)
    if not isinstance(user_id, int):
        await message.err('invalid type!')
        return
    if user_id not in Config.SUDO_USERS:
        await message.edit(f"user : `{user_id}` not in **SUDO**!", del_in=5)
    else:
        Config.SUDO_USERS.remove(user_id)
        await asyncio.gather(
            SUDO_USERS_COLLECTION.delete_one({'_id': user_id}),
            message.edit(f"user : `{user_id}` removed from **SUDO**!", del_in=5, log=__name__))


@alphaz.on_cmd("vsudo", about={'header': "lihat pengguna sudo"}, allow_channels=False)
async def view_sudo(message: Message):
    """ lihat pengguna sudo """
    if not Config.SUDO_USERS:
        await message.edit("**SUDO** pengguna tidak ditemukan!", del_in=5)
        return
    out_str = '?????? **SUDO USERS** ??????\n???AlphaZ Plugins???** \n\n'
    async for user in SUDO_USERS_COLLECTION.find():
        out_str += f" ???? {user['men']} ???????? `{user['_id']}`\n"
    await message.edit(out_str, del_in=0)


@alphaz.on_cmd("addscmd", about={
    'header': "tambahkan perintah sudo",
    'flags': {'-all': "tambahkan semua perintah ke sudo"},
    'usage': "{tr}addscmd [command name]\n{tr}addscmd -all"}, allow_channels=False)
async def add_sudo_cmd(message: Message):
    """ add sudo cmd """
    if '-all' in message.flags:
        await SUDO_CMDS_COLLECTION.drop()
        Config.ALLOWED_COMMANDS.clear()
        tmp_ = []
        for c_d in list(userge.manager.enabled_commands):
            t_c = c_d.lstrip(Config.CMD_TRIGGER)
            tmp_.append({'_id': t_c})
            Config.ALLOWED_COMMANDS.add(t_c)
        await asyncio.gather(
            SUDO_CMDS_COLLECTION.insert_many(tmp_),
            message.edit(f"**Added** all (`{len(tmp_)}`) commands to **SUDO** cmds!",
                         del_in=5, log=__name__))
        return
    cmd = message.input_str
    if not cmd:
        await message.err('input not found!')
        return
    cmd = cmd.lstrip(Config.CMD_TRIGGER)
    if cmd in Config.ALLOWED_COMMANDS:
        await message.edit(f"cmd : `{cmd}` already in **SUDO**!", del_in=5)
    elif cmd not in (c_d.lstrip(Config.CMD_TRIGGER)
                     for c_d in list(userge.manager.enabled_commands)):
        await message.edit(f"cmd : `{cmd}` ????, is that a command ?", del_in=5)
    else:
        Config.ALLOWED_COMMANDS.add(cmd)
        await asyncio.gather(
            SUDO_CMDS_COLLECTION.insert_one({'_id': cmd}),
            message.edit(f"cmd : `{cmd}` added to **SUDO**!", del_in=5, log=__name__))


@alphaz.on_cmd("delscmd", about={
    'header': "hapus perintah sudo",
    'flags': {'-all': "hapus semua perintah sudo"},
    'usage': "{tr}delscmd [command name]\n{tr}delscmd -all"}, allow_channels=False)
async def del_sudo_cmd(message: Message):
    """ delete sudo cmd """
    if '-all' in message.flags:
        Config.ALLOWED_COMMANDS.clear()
        await asyncio.gather(
            SUDO_CMDS_COLLECTION.drop(),
            message.edit("**SUDO** cmds cleared!", del_in=5))
        return
    cmd = message.filtered_input_str
    if not cmd:
        await message.err('input not found!')
        return
    if cmd not in Config.ALLOWED_COMMANDS:
        await message.edit(f"cmd : `{cmd}` not in **SUDO**!", del_in=5)
    else:
        Config.ALLOWED_COMMANDS.remove(cmd)
        await asyncio.gather(
            SUDO_CMDS_COLLECTION.delete_one({'_id': cmd}),
            message.edit(f"cmd : `{cmd}` removed from **SUDO**!", del_in=5, log=__name__))


@alphaz.on_cmd("vscmd", about={'header': "lihat sudo cmds"}, allow_channels=False)
async def view_sudo_cmd(message: Message):
    """ lihat sudo cmds """
    if not Config.ALLOWED_COMMANDS:
        await message.edit("**SUDO** cmds tidak ditemukan!", del_in=5)
        return
    out_str = f"???? **SUDO CMDS** ????\n???AlphaZ Plugins???\n\n**trigger** : `{Config.SUDO_TRIGGER}`\n\n"
    async for cmd in SUDO_CMDS_COLLECTION.find().sort('_id'):
        out_str += f"`{cmd['_id']}`  "
    await message.edit_or_send_as_file(out_str, del_in=0)
