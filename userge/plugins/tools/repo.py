# Copyright (C) 2020 by UsergeTeam@Github, < https://github.com/UsergeTeam >.
#
# This file is part of < https://github.com/UsergeTeam/Userge > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/uaudith/Userge/blob/master/LICENSE >
#
# All rights reserved.

from userge import userge, Message, Config, versions, get_version


@userge.on_cmd("repo", about={'header': "get repo link and details"})
async def see_repo(message: Message):
    """see repo"""
    output = f"""
__Repo Userbot__ 😈 **Alpha Z Plugins** 😈

    __Tahan lama sebagai seorang Serge__

    __The Userbot Plugins__
• **Version** : `{get_version()}`
• **License** : {versions.__license__}
• **Copyright** : {versions.__copyright__}
• **Repo** : [AlphaZ Plugins]({Config.UPSTREAM_REPO})
"""
    await message.edit(output)
