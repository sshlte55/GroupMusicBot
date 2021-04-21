from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgQAAx0CTv65QgABBfJlYF6VCrGMm6OJ23AxHmD6qUSWESsAAhoQAAKm8XEeD5nrjz5IJFYeBA")
    await message.reply_text(
        f"""**Hai saya {bn} 
Saya bisa memutar musik di panggilan suara grup Anda. Dikembangkan oleh [ɢᴏᴏᴅ ʙᴏʏs](https://t.me/GB_03101999).

Tambahkan saya ke grup Anda dan mainkan musik dengan bebas!
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📝 Daftar Perintah Bot", url="https://telegra.ph/Ultroid-04-21")
                  ],[
                    InlineKeyboardButton(
                        "👮🏻‍♀ Assistant Bot", url="https://t.me/GB_Assistant"
                    ),
                    InlineKeyboardButton(
                        "👑 pemilik Bot", url="https://t.me/GB_03101999"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "➕ Tambahkan ke Grup Anda ➕", url="https://t.me/GB_VcMusicBot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Group Music Player Online ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "👑 Pemilik Bot", url="https://t.me/GB_03101999")
                ]
            ]
        )
   )
