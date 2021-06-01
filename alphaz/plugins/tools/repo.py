# alfareza

from alphaz import alphaz, Message, Config, versions, get_version


@alphaz.on_cmd("repo", about={'header': "get repo link and details"})
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
