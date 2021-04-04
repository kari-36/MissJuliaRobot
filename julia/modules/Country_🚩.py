#    MissJuliaRobot (A Telegram Bot Project)
#    Copyright (C) 2019-Present Anonymous (https://t.me/MissJulia_Robot)

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, in version 3 of the License.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.

#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see < https://www.gnu.org/licenses/agpl-3.0.en.html >


import flag
import html, os
from countryinfo import CountryInfo
from julia import *
from julia.events import register
from telethon import types
from telethon.tl import functions
from pymongo import MongoClient
from julia import MONGO_DB_URI
from telethon import events

client = MongoClient()
client = MongoClient(MONGO_DB_URI)
db = client["missjuliarobot"]
approved_users = db.approve


async def is_register_admin(chat, user):
    if isinstance(chat, (types.InputPeerChannel, types.InputChannel)):
        return isinstance(
            (
                await tbot(functions.channels.GetParticipantRequest(chat, user))
            ).participant,
            (types.ChannelParticipantAdmin, types.ChannelParticipantCreator),
        )
    if isinstance(chat, types.InputPeerUser):
        return True


@register(pattern="^/country (.*)")
async def _(event):
    if event.fwd_from:
        return
    approved_userss = approved_users.find({})
    for ch in approved_userss:
        iid = ch["id"]
        userss = ch["user"]
    if event.is_group:
        if await is_register_admin(event.input_chat, event.message.sender_id):
            pass
        elif event.chat_id == iid and event.sender_id == userss:
            pass
        else:
            return
    input_str = event.pattern_match.group(1)
    lol = input_str
    country = CountryInfo(lol)
    try:
        a = country.info()
    except:
        await event.reply("No information available for that country.")
        return

    name = a.get("name")
    hu = str(a.get("altSpellings")).replace("[", "").replace("]", "").replace("'", "")
    area = a.get("area")
    borders = str(a.get("borders")).replace("[", "").replace("]", "").replace("'", "")
    call = str(a.get("callingCodes")).replace("[", "").replace("]", "").replace("'", "")
    capital = a.get("capital")
    currencies = (
        str(a.get("currencies")).replace("[", "").replace("]", "").replace("'", "")
    )
    HmM = a.get("demonym")
    geo = a.get("geoJSON")
    pablo = geo.get("features")
    Pablo = pablo[0]
    PAblo = Pablo.get("geometry")
    EsCoBaR = PAblo.get("type")
    iSo = a.get("ISO")
    isso = []
    for hitler in iSo:
        po = iSo.get(hitler)
        isso.append(po)
    iso = str(isso).replace("[", "").replace("]", "").replace("'", "")
    fla = (a.get("ISO")).get("alpha2")
    nox = fla.upper()
    okie = flag.flag(nox)
    lMAO = str(a.get("languages")).replace("[", "").replace("]", "").replace("'", "")
    nonive = a.get("nativeName")
    waste = a.get("population")
    reg = a.get("region")
    sub = a.get("subregion")
    tom = str(a.get("timezones")).replace("[", "").replace("]", "").replace("'", "")
    lanester = str(a.get("tld")).replace("[", "").replace("]", "").replace("'", "")
    wiki = a.get("wiki")

    caption = f"""**Information Gathered Successfully**
Country Name:- `{name}`
Alternative Spellings:- `{hu}`
Country Area:- `{area} square kilometers`
Borders:- `{borders}`
Calling Codes:- `{call}`
Country's Capital:- `{capital}`
Country's currency:- `{currencies}`
Country's Flag:- `{okie}`
Demonym:- `{HmM}`
Country Type:- `{EsCoBaR}`
ISO Names:- `{iso}`
Languages:- `{lMAO}`
Native Name:- `{nonive}`
Population:- `{waste}`
Region:- `{reg}`
Sub Region:- `{sub}`
Time Zones:- `{tom}`
Top Level Domain:- `{lanester}`
Wikipedia:- `{wiki}`
"""
    await event.reply(caption)


file_help = os.path.basename(__file__)
file_help = file_help.replace(".py", "")
file_helpo = file_help.replace("_", " ")

__help__ = """
 - /country <country name>: Returns info about given country
"""

CMD_HELP.update({file_helpo: [file_helpo, __help__]})
