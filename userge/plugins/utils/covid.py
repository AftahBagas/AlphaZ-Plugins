# Copyright (C) 2020 by UsergeTeam@Github, < https://github.com/UsergeTeam >.
# This file is part of < https://github.com/UsergeTeam/Userge > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/uaudith/Userge/blob/master/LICENSE >

# Userge Plugin for getting detailed stats of Covid Patients
# Author: Sumanjay (https://github.com/cyberboysumanjay) (@cyberboysumanjay)
# All rights reserved.

from covid import Covid

from userge import userge, Message, pool


@userge.on_cmd("covid", about={
    'header': "lihat detail yang jelas",
    'description': "Situasi real time pasien COVID-19 saat ini dilaporkan di seluruh dunia",
    'flags': {'-l': "daftar negara"},
    'usage': "{tr}covid [flag | country]",
    'examples': ["{tr}covid -l", "{tr}covid", "{tr}covid india"]})
async def covid(message: Message):
    await message.edit("`mengambil covid ...`")
    covid_ = await pool.run_in_thread(Covid)("worldometers")
    country = message.input_str
    result = ""
    if '-l' in message.flags:
        result += "<u>Negara-negara yang Didukung Cmd Covid</u>\n\n`"
        result += '` , `'.join(sorted(filter(lambda x: x, covid_.list_countries())))
        result += "`"
    elif country:
        try:
            data = covid_.get_status_by_country_name(country)
        except ValueError:
            await message.err(f"invalid country name <{country}>!")
            return
        result += f"<u>Status Covid untuk {data['country']}</u>\n\n"
        result += f"**kasus baru** : `{data['new_cases']}`\n"
        result += f"**kematian baru** : `{data['new_deaths']}`\n\n"
        result += f"**kritis** : `{data['critical']}`\n"
        result += f"**aktif** : `{data['active']}`\n"
        result += f"**dikonfirmasi** : `{data['confirmed']}`\n"
        result += f"**meninggal** : `{data['deaths']}`\n"
        result += f"**pulih** : `{data['recovered']}`\n\n"
        result += f"**tes total** : `{data['total_tests']}`\n"
        result += f"**total tes per juta** : `{data['total_tests_per_million']}`\n"
        result += f"**total kasus per juta** : `{data['total_cases_per_million']}`\n"
        result += f"**total kematian per juta** : `{data['total_deaths_per_million']}`\n"
        result += f"**populasi** : `{data['population']}`\n"
    else:
        result += "<u>Status Covid di dunia</u>\n\n"
        result += f"**total kasus aktif** : `{covid_.get_total_active_cases()}`\n"
        result += f"**total kasus yang dikonfirmasi** : `{covid_.get_total_confirmed_cases()}`\n"
        result += f"**total kematian** : `{covid_.get_total_deaths()}`\n"
        result += f"**total pulih** : `{covid_.get_total_recovered()}`\n"
    await message.edit_or_send_as_file(result)
