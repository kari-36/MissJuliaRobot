#    MissJuliaRobot (A Telegram Bot Project)
#    Copyright (C) 2019-2021 Julia (https://t.me/MissJulia_Robot)

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, in version 3 of the License.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.

#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see < https://www.gnu.org/licenses/agpl-3.0.en.html/ >.


from sqlalchemy import Boolean, Column, Integer, String, UnicodeText
from julia.modules.sql import BASE, SESSION


class Nightmode(BASE):
    __tablename__ = "nightmode"
    chat_id = Column(String(14), primary_key=True)

    def __init__(self, chat_id):
        self.chat_id = chat_id


Nightmode.__table__.create(checkfirst=True)


def add_nightmode(chat_id: str):
    nightmoddy = Nightmode(str(chat_id))
    SESSION.add(nightmoddy)
    SESSION.commit()


def rmnightmode(chat_id: str):
    rmnightmoddy = SESSION.query(Nightmode).get(str(chat_id))
    if rmnightmoddy:
        SESSION.delete(rmnightmoddy)
        SESSION.commit()


def get_all_chat_id():
    stark = SESSION.query(Nightmode).all()
    SESSION.close()
    return stark


def is_nightmode_indb(chat_id: str):
    try:
        s__ = SESSION.query(Nightmode).get(str(chat_id))
        if s__:
            return str(s__.chat_id)
    finally:
        SESSION.close()
