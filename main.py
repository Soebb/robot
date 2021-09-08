import time
from configs import Config
from pyrogram import Client, filters, idle
from pyrogram.errors import QueryIdInvalid
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, InlineQuery, InlineQueryResultArticle, \
    InputTextMessageContent
import os
import io
from PIL import Image
import mutagen
from mutagen.mp3 import MP3
import requests
from music_tag import load_file
from pyrogram.errors import FloodWait


BOT_TOKEN = os.environ["BOT_TOKEN"]
Bot = Client(
    "Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)


START_TXT = """
Hi {}, I'm test bot
"""

START_BTN = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Source Code', url='https://github.com/samadii/ChannelForwardTagRemover'),
        ]]
    )
# User Client for Searching in Channel.
User = Client(
    session_name=Config.USER_SESSION_STRING,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH
)




@Bot.on_message(filters.command(["start"]))
async def start(bot, update):
    text = START_TXT.format(update.from_user.mention)
    reply_markup = START_BTN
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )
Musi = "-1001271917335 -1001516208383"
Musics = set(int(x) for x in Musi.split())


@Bot.on_message(filters.channel & filters.audio)
async def tag(bot, m):
    if (m.chat.id == -1001516208383):
        if "wikiseda" in m.caption:
            m.copy(chat_id=-1001271917335)

    fname = m.audio.file_name
    if fname.__contains__("@") or fname.__contains__("["):
        first = fname.split(' ')[0]
        if "@" in first:
            filename = fname.split(f'{first}', -1)
        elif fname.__contains__("(@") and not "@" in first:
            filename = fname.split("(@")[-2]
        elif fname.__contains__("[@") and not "@" in first:
            filename = fname.split("[@")[-2]
        elif fname.__contains__("[") and not "@" in first:
            filename = fname.split("[")[-2]
        elif (not "@" in first) and (not fname.__contains__("(@") or fname.__contains__("[") or fname.__contains__("[@")):
            filename = fname.split("@")[-2]
    else:
        filename = fname
  
    
    try:
        m = await bot.get_messages(m.chat.id, m.message_id)
        file = await m.download(file_name="temp/file.mp3")
        await m.delete()
        music = load_file("temp/file.mp3")
        t = f"{music['title']}"
        a = f"{music['artist']}"
        al = f"{music['album']}"
        g = f"{music['genre']}"
        c = f"{music['comment']}"
        l = f"{music['lyrics']}"
        ar = music['artwork']
        image_data = ar.value.data
        img = Image.open(io.BytesIO(image_data))
        img.save("artwork.jpg")
    except Exception as e:
        print(e)
    
    
    if g.__contains__("@") or g.__contains__("["):
        first = g.split(' ')[0]
        if "@" in first:
            genre = g.split(f'{first}', -1)
        elif g.__contains__("(@") and not "@" in first:
            genre = g.split("(@")[-2]
        elif g.__contains__("[@") and not "@" in first:
            genre = g.split("[@")[-2]
        elif g.__contains__("[") and not "@" in first:
            genre = g.split("[")[-2]
        elif (not "@" in first) and (not g.__contains__("(@") or g.__contains__("[") or g.__contains__("[@")):
            genre = g.split("@")[-2]
    else:
        genre = g

    
    if l.__contains__("@") or l.__contains__("["):
        first = l.split(' ')[0]
        if "@" in first:
            lyrics = l.split(f'{first}', -1)
        elif l.__contains__("(@") and not "@" in first:
            lyrics = l.split("(@")[-2]
        elif l.__contains__("[@") and not "@" in first:
            lyrics = l.split("[@")[-2]
        elif l.__contains__("[") and not "@" in first:
            lyrics = l.split("[")[-2]
        elif (not "@" in first) and (not l.__contains__("(@") or l.__contains__("[") or l.__contains__("[@")):
            lyrics = l.split("@")[-2]
    else:
        lyrics = l

    if c.__contains__("@") or c.__contains__("["):
        first = c.split(' ')[0]
        if "@" in first:
            comment = c.split(f'{first}', -1)
        elif c.__contains__("(@") and not "@" in first:
            comment = c.split("(@")[-2]
        elif c.__contains__("[@") and not "@" in first:
            comment = c.split("[@")[-2]
        elif c.__contains__("[") and not "@" in first:
            comment = c.split("[")[-2]
        elif (not "@" in first) and (not c.__contains__("(@") or c.__contains__("[") or c.__contains__("[@")):
            comment = c.split("@")[-2]
    else:
        comment = c

    if t.__contains__("@") or t.__contains__("["):
        first = t.split(' ')[0]
        if "@" in first:
            title = t.split(f'{first}', -1)
        elif t.__contains__("(@") and not "@" in first:
            title = t.split("(@")[-2]
        elif t.__contains__("[@") and not "@" in first:
            title = t.split("[@")[-2]
        elif t.__contains__("[") and not "@" in first:
            title = t.split("[")[-2]
        elif (not "@" in first) and (not t.__contains__("(@") or t.__contains__("[") or t.__contains__("[@")):
            title = t.split("@")[-2]
    else:
        title = t

    if al.__contains__("@") or al.__contains__("["):
        first = al.split(' ')[0]
        if "@" in first:
            album = al.split(f'{first}', -1)
        elif al.__contains__("(@") and not "@" in first:
            album = al.split("(@")[-2]
        elif al.__contains__("[@") and not "@" in first:
            album = al.split("[@")[-2]
        elif al.__contains__("[") and not "@" in first:
            album = al.split("[")[-2]
        elif (not "@" in first) and (not al.__contains__("(@") or al.__contains__("[") or al.__contains__("[@")):
            album = al.split("@")[-2]
    else:
        album = al

    if a.__contains__("@") or a.__contains__("["):
        first = a.split(' ')[0]
        if "@" in first:
            artist = a.split(f'{first}', -1)
        elif a.__contains__("(@") and not "@" in first:
            artist = a.split("(@")[-2]
        elif a.__contains__("[@") and not "@" in first:
            artist = a.split("[@")[-2]
        elif a.__contains__("[") and not "@" in first:
            artist = a.split("[")[-2]
        elif (not "@" in first) and (not a.__contains__("(@") or a.__contains__("[") or a.__contains__("[@")):
            artist = a.split("@")[-2]
    else:
        artist = a

    if (m.chat.id == -1001271917335) and ("wikiseda" in m.caption):
        await bot.send_photo(
            chat_id=m.chat.id,
            caption="🎤" + artist + " - " + title + "🎼" + "\n\n" + "#" + artist.split(f"{artist}", 0)[0].replace(" ", "_") + " #" + title.split(f"{title}", 0)[0].replace(" ", "_") + "\n\n" + "🆔👉 @dlmacvin_music",
            photo=open('artwork.jpg', 'rb')
        )
    elif (m.chat.id == -1001516208383) and (not "wikiseda" in m.caption):
        await bot.send_photo(
            chat_id=m.chat.id,
            caption="🎤" + artist + " - " + title + "🎼" + "\n\n" + "#" + artist.split(f"{artist}", 0)[0].replace(" ", "_") + " #" + title.split(f"{title}", 0)[0].replace(" ", "_") + "\n\n" + "🆔👉 @dlmacvin_music",
            photo=open('artwork.jpg', 'rb')
        )
    elif not m.chat.id in Musics:
        await bot.send_photo(
            chat_id=m.chat.id,
            caption="🎤" + artist + " - " + title + "🎼" + "\n\n" + "#" + artist.split(f"{artist}", 0)[0].replace(" ", "_") + " #" + title.split(f"{title}", 0)[0].replace(" ", "_") + "\n\n" + "🆔👉 @dlmacvin_music",
            photo=open('artwork.jpg', 'rb')
        )
    
    if (m.chat.id == -1001271917335) and ("wikiseda" in m.caption):
        audio = MP3(file)
        length = audio.info.length * 0.33
        l2 = (audio.info.length * 0.33) + 30
        if audio.info.length > l2:
            os.system("ffmpeg -ss " + str(length) + " -t 30 -y -i \"" + file + "\" -ac 1 -map 0:a -codec:a libopus -b:a 128k -vbr off -ar 24000 temp/output.ogg")
        else:
            os.system("ffmpeg -ss 0 -t 30 -y -i \"" + file + "\" -ac 1 -map 0:a -codec:a libopus -b:a 128k -vbr off -ar 24000 temp/output.ogg")
        sendVoice(m.chat.id, "temp/output.ogg", f"🎤{artist} - {title}🎼\n\n🆔👉 @dlmacvin_music")
    elif (m.chat.id == -1001516208383) and (not "wikiseda" in m.caption):
        audio = MP3(file)
        length = audio.info.length * 0.33
        l2 = (audio.info.length * 0.33) + 30
        if audio.info.length > l2:
            os.system("ffmpeg -ss " + str(length) + " -t 30 -y -i \"" + file + "\" -ac 1 -map 0:a -codec:a libopus -b:a 128k -vbr off -ar 24000 temp/output.ogg")
        else:
            os.system("ffmpeg -ss 0 -t 30 -y -i \"" + file + "\" -ac 1 -map 0:a -codec:a libopus -b:a 128k -vbr off -ar 24000 temp/output.ogg")
        sendVoice(m.chat.id, "temp/output.ogg", f"🎤{artist} - {title}🎼\n\n🆔👉 @dlmacvin_music")
    elif not m.chat.id in Musics:
        audio = MP3(file)
        length = audio.info.length * 0.33
        l2 = (audio.info.length * 0.33) + 30
        if audio.info.length > l2:
            os.system("ffmpeg -ss " + str(length) + " -t 30 -y -i \"" + file + "\" -ac 1 -map 0:a -codec:a libopus -b:a 128k -vbr off -ar 24000 temp/output.ogg")
        else:
            os.system("ffmpeg -ss 0 -t 30 -y -i \"" + file + "\" -ac 1 -map 0:a -codec:a libopus -b:a 128k -vbr off -ar 24000 temp/output.ogg")
        sendVoice(m.chat.id, "temp/output.ogg", f"🎤{artist} - {title}🎼\n\n🆔👉 @dlmacvin_music")

    music.remove_tag('comment')
    music.remove_tag('artist')
    music.remove_tag('lyrics')
    music.remove_tag('title')
    music.remove_tag('album')
    music.remove_tag('genre')
    music.remove_tag('artwork')
    music['artwork'] = open('artwork.jpg', 'rb').read()
    music['artist'] = "@dlmacvin_music"
    music['title'] = title + "[@dlmacvin_music]"
    music['album'] = album
    music['lyrics'] = lyrics
    music['genre'] = genre 
    music['comment'] = comment
    music.save()
    caption = "🎤" + artist + " - " + title + "🎼" + "\n\n" + "#" + artist.split(f"{artist}", 0)[0].replace(" ", "_") + " #" + title.split(f"{title}", 0)[0].replace(" ", "_") + "\n\n" + "🆔👉 @dlmacvin_music"
    if (m.chat.id == -1001271917335) and ("wikiseda" in m.caption):
        await bot.send_audio(
            chat_id=m.chat.id,
            file_name=filename + ".mp3",
            caption=caption,
            thumb=open('artwork.jpg', 'rb'),
            audio="temp/file.mp3"
        )
    elif (m.chat.id == -1001516208383) and (not "wikiseda" in m.caption):
        await bot.send_audio(
            chat_id=m.chat.id,
            file_name=filename + ".mp3",
            caption=caption,
            thumb=open('artwork.jpg', 'rb'),
            audio="temp/file.mp3"
        )
    elif not m.chat.id in Musics:
        await bot.send_audio(
            chat_id=m.chat.id,
            file_name=filename + ".mp3",
            caption=caption,
            thumb=open('artwork.jpg', 'rb'),
            audio="temp/file.mp3"
        )
    

def sendVoice(chat_id,file_name,text):
    url = "https://api.telegram.org/bot%s/sendVoice"%(BOT_TOKEN)
    files = {'voice': open(file_name, 'rb')}
    data = {'chat_id' : chat_id, 'caption' : text}
    r= requests.post(url, files=files, data=data)
   


chnls = "-1001516208383 -1001166919373 -1001437520825 -1001071120514 -1001546442991 -1001322014891 -1001409508844 -1001537554747 -1001462444753 -1001146657589 -1001592624165 -1001588137496"
CHANNELS = set(int(x) for x in chnls.split())

@Bot.on_message((filters.video | filters.document) & filters.channel)
async def caption(bot, message: Message):
    media = message.video or message.document
    if (message.chat.id == -1001516208383) and (media is not None) and (media.file_name is not None):
        await message.edit(f"{media.file_name.replace('.mp4', '').replace('.mkv', '').replace('.webm', '')}\n\n🆔👉 @dlmacvin_music")
    if (media is not None) and (media.file_name is not None) and (not message.chat.id in CHANNELS):
        m = media.file_name.replace("Fragmanı", "").replace("mp4", "").replace(".", " ").replace("_", " ").replace("Fragmanlarım", "").replace("ı", "i").replace("İ", "I").replace("ö", "o").replace("Ö", "O").replace("Ü", "U").replace("ü", "u").replace("ë", "e").replace("@dlmacvin2 -", "").replace("@dlmacvin -", "").replace("Ë", "E").replace("Ä", "A").replace("ç", "c").replace("Ç", "C").replace("ş", "s").replace("Ş", "S").replace("ğ", "g").replace("Ğ", "G").replace("ä", "a")
        D = m.replace("720P", "").replace("E20", "").replace("E120", "").replace("E220", "").replace("E320", "").replace("E420", "")
        N = m
        Z = media.file_name
        fa = " "
        tz = " "
        Lo = " "
        Q = " "
        Fucc = " "
        E = None
        X = None
        Ee = None
        if "Sen Cal Kapimi" in m:
            fa += "#تو_در_خانه_ام_را_بزن"
            X = "Sen Cal Kapimi"
        if "Dokhtarane Gol Foroosh" in m:
            fa += "#دختران_گل_فروش"
            X = "Dokhtarane Gol Foroosh"
        if "Marasli" in m:
            fa += "#اهل_ماراش"
            X = "Marasli"
        if "Kalp Yarasi" in m:
            fa += "#زخم_قلب"
            X = "Kalp Yarasi"
        if "Dunya Hali" in m:
            fa += "#احوال_دنیایی"
            X = "Dunya Hali"
        if "Ver Elini Ask" in m:
            fa += "#دستت_را_بده_عشق"
            X = "Ver Elini Ask"
        if "Ezel" in m:
            fa += "#ایزل"
            X = "Ezel"
        if "Ikimizin Sirri" in m:
            fa += "#راز_ما_دو_نفر"
            X = "Ikimizin Sirri"
        if "Dirilis Ertugrul" in m:
            fa += "#قیام_ارطغرل"
            X = "Dirilis Ertugrul"
        if "Yemin" in m:
            fa += "#قسم"
            X = "Yemin"
        
        if "Ask i Memnu" in m:
            fa += "#عشق_ممنوع"
            X = "Ask i Memnu"
        if "Bozkir Arslani Celaleddin" in m:
            fa += "#جلال_الدین_خوارزمشاهی"
            X = "Bozkir Arslani Celaleddin"
        if "Kazara Ask" in m:
            fa += "#عشق_تصادفی"
            X = "Kazara Ask"
        if "Bas Belasi" in m:
            fa += "#بلای_جون"
            X = "Bas Belasi"
        if "Ask Mantik Intikam" in m:
            fa += "#عشق_منطق_انتقام"
            X = "Ask Mantik Intikam"
        if "Baht Oyunu" in m:
            fa += "#بازی_بخت"
            X = "Baht Oyunu"
        if "Ada Masali" in m:
            fa += "#قصه_جزیره"
            X = "Ada Masali"
        if "Askin Tarifi" in m:
            fa += "#طرز_تهیه_عشق"
            X = "Askin Tarifi"
        if "Yesilcam" in m:
            fa += "#سینمای_قدیم_ترکیه"
            X = "Yesilcam"
        if "Camdaki Kiz" in m:
            fa += "#دختر_پشت_پنجره"
            X = "Camdaki Kiz"
        if "Bir Zamanlar Kibris" in m:
            fa += "#روزی_روزگاری_در_قبرس"
            X = "Bir Zamanlar Kibris"
        if "Teskilat" in m:
            fa += "#تشکیلات"
            X = "Teskilat"
        if "Kardeslerim" in m:
            fa += "#خواهر_و_برادرانم"
            X = "Kardeslerim"
        if "Ogrenci Evi" in m:
            fa += "#خانه_دانشجویی"
            X = "Ogrenci Evi"
        if "Sihirli Annem" in m:
            fa += "#مادر_سحرآمیز_من"
            X = "Sihirli Annem"
        if "Yetis Zeynep" in m:
            fa += "#برس_زینب"
            X = "Yetis Zeynep"
        if "Hukumsuz" in m:
            fa += "#بی_قانون"
            X = "Hukumsuz"
        if "Saygi" in m:
            fa += "#احترام"
            X = "Saygi"
        if "Vahsi Seyler" in m:
            fa += "#چیز_های_وحشی"
            X = "Vahsi Seyler"
        if "Seref Bey" in m:
            fa += "#آقای_شرف"
            X = "Seref Bey"
        if "Gibi" in m:
            fa += "#مانند"
            X = "Gibi"
        if "Iste Bu Benim Masalim" in m:
            fa += "#این_داستان_من_است"
            X = "Iste Bu Benim Masalim"
        if "Son Yaz" in m:
            fa += "#آخرین_تابستان"
            X = "Son Yaz"
        if "Akinci" in m:
            fa += "#مهاجم"
            X = "Akinci"
        if "Kirmizi Oda" in m:
            fa += "#اتاق_قرمز"
            X = "Kirmizi Oda"
        if "Emanet" in m:
            fa += "#امانت"
            X = "Emanet"
        if "Ibo Show" in m:
            fa += "#برنامه_ایبو_شو"
            X = "Ibo Show"
        if "EDHO" in m:
            fa += "#راهزنان"
            X = "EDHO"
        if "Uyanis Buyuk Selcuklu" in m:
            fa += "#بیداری_سلجوقیان_بزرگ"
            X = "Uyanis Buyuk Selcuklu"
        if "Yasak Elma" in m:
            fa += "#سیب_ممنوعه"
            X = "Yasak Elma"
        if "Sadakatsiz" in m:
            fa += "#بی_صداقت #بی_وفا"
            X = "Sadakatsiz"
        if "Bir Zamanlar Cukurova" in m:
            fa += "#روزی_روزگاری_چوکورا"
            X = "Bir Zamanlar Cukurova"
        if "Gonul Dagi" in m:
            fa += "#کوه_دل"
            X = "Gonul Dagi"
        if "Ufak Tefek Cinayetler" in m:
            fa += "#خرده_جنایت_ها"
            X = "Ufak Tefek Cinayetler"
        if "Sibe Mamnooe" in m:
            fa += "#سیب_ممنوعه"
            X = "Sibe Mamnooe"
        if "Setare Shomali" in m:
            fa += "#ستاره_شمالی"
            X = "Setare Shomali"
        if "Otaghe Ghermez" in m:
            fa += "#اتاق_قرمز"
            X = "Otaghe Ghermez"
        if "Mojeze Doctor" in m:
            fa += "#دکتر_معجزه_گر"
            X = "Mojeze Doctor"
        if "Mucize Doktor" in m:
            fa += "#دکتر_معجزه_گر"
            X = "Mucize Doktor"
        if "Be Eshghe To Sogand" in m:
            fa += "#به_عشق_تو_سوگند"
            X = "Be Eshghe To Sogand"
        if "Eshgh Az No" in m:
            fa += "#عشق_از_نو"
            X = "Eshgh Az No"
        if "Eshghe Mashroot" in m:
            fa += "#عشق_مشروط"
            X = "Eshghe Mashroot"
        if "Cukurova" in m:
            fa += "#روزی_روزگاری_چکوروا"
            X = "Cukurova"
        if "Yek Jonun Yek Eshgh" in m:
            fa += "#یک_جنون_یک_عشق"
            X = "Yek Jonun Yek Eshgh"
        if "2020" in m:
            fa += "#2020"
            X = "2020"
        if "Hekim" in m:
            fa += "#حکیم_اوغلو"
            X = "Hekim"
        if "Godal" in m:
            fa += "#گودال"
            X = "Godal"
        if ("Cukur" in m) and not m.__contains__("Cukurova"):
            fa += "#گودال"
            X = "Cukur"
        if "Khaneh Man" in m:
            fa += "#سرنوشتت_خانه_توست"
            X = "Khaneh Man"
        if "Alireza" in m:
            fa += "#علیرضا"
            X = "Alireza"
        if "Dokhtare Safir" in m:
            fa += "#دختر_سفیر"
            X = "Dokhtare Safir"
        if "Marashli" in m:
            fa += "#ماراشلی - #اهل_ماراش"
            X = "Marashli"
        if "Zarabane Ghalb" in m:
            fa += "#ضربان_قلب"
            X = "Zarabane Ghalb"
        if "Aparteman Bigonahan" in m:
            fa += "#آپارتمان_بی_گناهان"
            X = "Aparteman Bigonahan" 
        if "Hayat Agaci" in m:
            fa += "#درخت_زندگی"
            X = "Hayat Agaci" 
        if "Ruya" in m:
            fa += "#رویا"
            X = "Ruya" 
        if "Uzak Sehrin Masali" in m:
            fa += "#داستان_شهری_دور"
            X = "Uzak Sehrin Masali"
        if "Icimizden Biri" in m:
            fa += "#یکی_از_میان_ما"
            X = "Icimizden Biri"
        if "Kocaman Ailem" in m:
            fa += "#خانواده_بزرگم"
            X = "Kocaman Ailem"
        if "Insanlik Sucu" in m:
            fa += "#جرم_انسانیت"
            X = "Insanlik Sucu"
        if "Tutsak" in m:
            fa += "#اسیر "
            X = "Tutsak"
        if "Fazilet Hanim ve Kızlari" in m:
            fa += "#فضیلت_خانم_و_دخترانش"
            X = "Fazilet Hanim ve Kızlari"
        if "Ferhat Ile Sirin" in m:
            fa += "#فرهاد_و_شیرین"
            X = "Ferhat Ile Sirin"
        if "Gel Dese Ask" in m:
            fa += "#عشق_صدا_میزند"
            X = "Gel Dese Ask"			
        if "Gibi" in m:
            fa += "#مانند"
            X = "Gibi"
        if "Halka" in m:
            fa += "#حلقه"
            X = "Halka"
        if "Hercai" in m:
            fa += "#هرجایی"
            X = "Hercai"
        if "Hizmetciler" in m:
            fa += "#خدمتکاران"
            X = "Hizmetciler"
        if "Istanbullu Gelin" in m:
            fa += "#عروس_استانبولی"
            X = "Istanbullu Gelin"
        if "Kalp Atisi " in m:
            fa += "#ضربان_قلب"
            X = "Kalp Atisi "
        if "Kara Sevda" in m:
            fa += "#کاراسودا #عشق_بی_پایان"
            X = "Kara Sevda"
        if "Kardes Cocuklari" in m:
            fa += "#خواهرزاده_ها"
            X = "Kardes Cocuklari"
        if "Kimse Bilmez" in m:
            fa += "#کسی_نمیداند"
            X = "Kimse Bilmez"
        if "Kursun" in m:
            fa += "#گلوله"
            X = "Kursun"
        if "Kuzey Yildizi Ilk Ask" in m:
            fa += "#ستاره_شمالی_عشق_اول"
            X = "Kuzey Yildizi Ilk Ask"
        if "Kuzgun" in m:
            fa += "#کلاغ #کوزگون"
            X = "Kuzgun"
        if "Meryem" in m:
            fa += "#مریم"
            X = "Meryem"
        if "Muhtesem Ikili" in m:
            fa += "#زوج_طلایی"
            X = "Muhtesem Ikili"
        if "Nefes Nefese" in m:
            fa += "#نفس_زنان"
            X = "Nefes Nefese"
        if "Ogretmen" in m:
            fa += "#معلم"
            X = "Ogretmen"
        if "Olene Kadar" in m:
            fa += "#تا_حد_مرگ"
            X = "Olene Kadar"
        if "Sahsiyet" in m:
            fa += "#شخصیت"
            X = "Sahsiyet"			
        if "Sahin Tepesi" in m:
            fa += "#تپه_شاهین"
            X = "Sahin Tepesi"
        if "Savasci" in m:
            fa += "#جنگجو"
            X = "Savasci"
        if "Sefirin Kizi" in m:
            fa += "#دختر_سفیر"
            X = "Sefirin Kizi"
        if "Sevgili Gecmis" in m:
            fa += "#گذشته_ی_عزیز"
            X = "Sevgili Gecmis"
        if "Sheref Bey" in m:
            fa += "#آقای_شرف"
            X = "Sheref Bey"
        if "Sihirlis Annem" in m:
            fa += "#مادر_جادویی_من"
            X = "Sihirlis Annem"
        if "The Protector" in m:
            fa += "#محافظ"
            X = "The Protector"
        if "Vahsi Seyler" in m:
            fa += "#چیزهای_وحشی"
            X = "Vahsi Seyler"
        if "Vurgun" in m:
            fa += "#زخمی"
            X = "Vurgun"
        if "Ya Istiklal Ya Olum" in m:
            fa += "#یا_استقلال_یا_مرگ"
            X = "Ya Istiklal Ya Olum"
        if "Yalanci" in m:
            fa += "#دروغگو"
            X = "Yalanci"
        if "Bir Ask Hikayesi" in m:
            fa += "#حکایت_یک_عشق"
            X = "Bir Ask Hikayesi"
        if "Carpisma" in m:
            fa += "#تصادف"
            X = "Carpisma"
        if "Cocuk" in m:
            fa += "#بچه"
            X = "Cocuk"
        if "Lise Devriyesi" in m:
            fa += "#گشت_مدرسه"
            X = "Lise Devriyesi"	
			
	
			
        if Z.__contains__("Fragman") or m.__contains__("Bolum") or m.__contains__("bolum") or Z.__contains__("fragman"):
            if " Bolum" in m:
                bul = " Bolum"
            elif " bolum" in m:
                bul = " bolum"
            elif not m.__contains__(" Bolum") and not m.__contains__(" bolum"):
                if "Bolum" in m:
                    bul = "Bolum"
                elif "bolum" in m:
                    bul = "bolum"
            Jn = m.split(f"{bul}")[1]
            if "2" in Jn:
                tz += "#دوم"
            elif "1" in Jn:
                tz += "#اول"
            elif "3" in Jn:
                tz += "#سوم"
            elif "4" in Jn:
                tz += "#چهارم"
            elif "5" in Jn:
                tz += "#پنجم"
            elif "6" in Jn:
                tz += "#ششم"
            if X is None:
                Ghi = m.split(f"{bul}")[-2]
                X = Ghi.rsplit(' ', 1)[0]
                Ee = Ghi.rsplit(' ', 1)[1]
                
                print(f"X = {X}")
                
                print(f"Ee = {Ee}")
                # X = X.replace(' ', '_')
                # if X.startswith("_"):
                    # X = X.split("_", 1)[1]
                Lo += f"#{X.replace(' ', '_')}"
            # if (X is not None) and (X.__contains__("a") or X.__contains__("o") or X.__contains__("i") or X.__contains__("c") or X.__contains__("b") or X.__contains__("e") or X.__contains__("l") or X.__contains__("n") or X.__contains__("m")):
            else:
                Yd = X.replace(" ", "_")
                Lo += "#" + f"{Yd}"
                V = m.replace(f"{X}", "")
                Ee = V.split(f"{bul}", -1)[0]
            
            Tzz = tz.replace("#", "")
            date = " "

            if "Ask Mantik Intikam" in m:
                date += "شنبه ساعت 4 بامداد از رسانه اینترنتی دی ال مکوین"
            if "Sen Cal Kapimi" in m:
                date += "پنجشنبه ساعت 4 بامداد از رسانه اینترنتی دی ال مکوین"
            if "Kalp Yarasi" in m:
                date += "سه شنبه ساعت 4 بامداد از رسانه اینترنتی دی ال مکوین"
            if "Bas Belasi" in m:
                date += "شنبه از رسانه اینترنتی دی ال مکوین"
            if "Uzak Sehrin Masali" in m:
                date += "بزودی از رسانه اینترنتی دی ال مکوین"
            if "Icimizden Biri" in m:
                date += "بزودی از رسانه اینترنتی دی ال مکوین"
            if "Elkizi" in m:
                date += "بزودی از رسانه اینترنتی دی ال مکوین"
            FA = fa.replace("#", "").replace("_", " ")
            MSG = f"⬇️ تیزر{Tzz} قسمت {Ee} ({FA} ) {Lo} ، بازیرنویس چسبیده"
            msg = await message.edit(f"{MSG.replace('  ', ' ').replace('720P', '').replace('1080P', '').replace('480P', '').replace('240P', '')}\n\n🔻 پخش {date}\n\n🆔👉 @dlmacvin_new")
               
        if (not m.__contains__("Bolum")) and (N.__contains__("E0") or N.__contains__("E1") or N.__contains__("E2") or N.__contains__("E3") or N.__contains__("E4") or N.__contains__("E5") or N.__contains__("E6") or N.__contains__("E7") or N.__contains__("E8") or N.__contains__("E9")):
            if '720P' in m:
                Q += '720'
            if '480P' in m:
                Q += '480'
            if '1080P' in m:
                Q += '1080'
            if '240P' in m:
                Q += '240'
            if m.__contains__("720P") or m.__contains__("1080P") or m.__contains__("240P") or m.__contains__("480P"):

                q = f"\n🔹کیفیت : {Q}"
            else:
                q = ""
            if 'E0' in N:
                O = N.split("E0")[1]
                T = O.split()[0]
                if T.startswith("0"):
                    E = f"{T.replace('0', '')}"
                else:
                    E = f"{T}"
                n = N.split("E0")[0]
            if 'E1' in N:
                O = N.split("E1")[1]
                T = O.split()[0]
                E = '1' + f"{T}"
                n = N.split("E1")[0]
            if 'E2' in N:
                O = N.split("E2")[1]
                T = O.split()[0]
                E = '2' + f"{T}"
                n = N.split("E2")[0]
            if 'E3' in N:
                O = N.split("E3")[1]
                T = O.split()[0]
                E = '3' + f"{T}"
                n = N.split("E3")[0]
            if 'E4' in N:
                O = N.split("E4")[1]
                T = O.split()[0]
                E = '4' + f"{T}"
                n = N.split("E4")[0]
            if 'E5' in N:
                O = N.split("E5")[1]
                T = O.split()[0]
                E = '5' + f"{T}"
                n = N.split("E5")[0]
            if 'E6' in N:
                O = N.split("E6")[1]
                T = O.split()[0]
                E = '6' + f"{T}"
                n = N.split("E6")[0]
            if 'E7' in N:
                O = N.split("E7")[1]
                T = O.split()[0]
                E = '7' + f"{T}"
                n = N.split("E7")[0]
            if 'E8' in N:
                O = N.split("E8")[1]
                T = O.split()[0]
                E = '8' + f"{T}"
                n = N.split("E8")[0]
            if 'E9' in N:
                O = N.split("E9")[1]
                T = O.split()[0]
                E = '9' + f"{T}"
                n = N.split("E9")[0]
            H = fa.replace("_", " ").replace("#", "")
            if not "Hard-Sub" in N:
                Fucc += f"🔺{H} قسمت {E} \n🔸 دوبله فارسی"
                Fuc = f"{Fucc}{q} \n🆔👉 @dlmacvin_new | {fa}"

                print(Fuc)
                msg = await message.edit(Fuc)
            else:
                Fucc += f"♨️ سریال{fa} ( {n}) بازیرنویس چسبیده\n👌قسمت : {E.replace('Hard-Sub', '')}"
                Fuc = f"{Fucc}{q} \n🔻تماشای آنلاین بدون فیلتر شکن: \n🆔👉 @dlmacvin_new"

                print(Fuc)
                msg = await message.edit(Fuc)
        elif (m.__contains__("0P")) and (not N.__contains__("E0") and not m.__contains__("bolum") and not m.__contains__("Fragman") and not m.__contains__("Bolum") and not N.__contains__("E1") and not N.__contains__("E2") and not N.__contains__("E3") and not N.__contains__("E4") and not N.__contains__("E5") and not N.__contains__("E6") and not N.__contains__("E7") and not N.__contains__("E8") and not N.__contains__("E9")):
            if "20" in D:
                f = D.split("20")[0]
                U = D.split("20")[1]
                K = U.split()[0]
                Y = '20' + f"{K}"
                YR = f"\n👌سال : {Y}"
            if "19" in D:
                f = D.split("19")[0]
                U = D.split("19")[1]
                K = U.split()[0]
                Y = '19' + f"{K}"
                YR = f"\n👌سال : {Y}"
           
          
            if (not D.__contains__("19")) and (not D.__contains__("20")):
                P = m.split("0P")[0]
                f = P.replace("72", "").replace("48", "").replace("108", "").replace("24", "")
                YR = f"\n👌سال :"
            if '720P' in m:
                Q += '720'
            if '480P' in m:
                Q += '480'
            if '1080P' in m:
                Q += '1080'
            if '240P' in m:
                Q += '240'
            if m.__contains__("720P") or m.__contains__("1080P") or m.__contains__("240P") or m.__contains__("480P"):
                G = f"\n🔹کیفیت : {Q}"
                q = G.replace(".1", " ").replace(".mkv", " ")
            else:
                q = ""
            YrR = f"{YR.replace('720P', '').replace('480P', '').replace('1080P', '').replace('240P', '').replace('mkv', '').replace('mp4', '')}"
            
            msg = await message.edit(f"♨️ فیلم {f.replace('Hard-Sub', '').replace(' 20', '')} بازیرنویس چسبیده{YrR} {q} \n🔻تماشای آنلاین بدون فیلتر شکن: \n🆔👉 @dlmacvin_new")
         

        # Start Auto Forward/Banner
        Copyright = "Kurulus Osman & Yemin & Son Yaz & Bir Zamanlar Kibris & Kazara Ask & Sadakatsiz & Iste Bu Benim Masalim & Hukumsuz & Gonul Dagi & Yesilcam & Ada Masali & Askin Tarifi & Baht Oyunu & Akinci & Teskilat & Saygi"
        No_Copyright = "Masumlar Apartmani & Sen Cal Kapimi & Bir Zamanlar Cukurova & Mucize Doktor & Dunya Hali & Bas Belasi & Ikimizin Sirri & Kalp Yarasi & Uyanis Buyuk Selcuklu & Kardeslerim & Emanet & EDHO & Yasak Elma & Ask Mantik Intikam & Bozkir Arslani Celaleddin"
        
        Copy = set(x for x in Copyright.split(' & '))
        NoCopy = set(x for x in No_Copyright.split(' & '))
        msgid = None
        liink = None
        Dublink = None
        kanal = None
        kap = None
        kap2 = None
        # Banner List
        if "Dunya Hali" in m:
            msgid = 2
            kanal = -1001572947427
            liink = "https://t.me/joinchat/rXqnANpb4ddmYmQ0"
        if "Sen Cal Kapimi" in m:
            msgid = 3
            kanal = -1001499596110
            Dublink = "https://t.me/joinchat/djHUcZrf3Z1lMGFk"
            liink = "https://t.me/joinchat/AAAAAFliBU5b2xvHML3pKw"
        if "Bas Belasi" in m:
            msgid = 4
            kanal = -1001531011385
            liink = "https://t.me/joinchat/CHt9Qm2i7ddjMWNk"
        if "Ikimizin Sirri" in m:
            msgid = 5
            kanal = -1001532685962
            liink = "https://t.me/joinchat/PPE9Q0Trw_A3OWNk"
        if "#زخم_قلب" in fa:
            msgid = 6
            kanal = -1001288493498
            liink = "https://t.me/joinchat/ji3XBL9w3lUwOGU8"
        if "#بیداری_سلجوقیان_بزرگ" in fa:
            msgid = 7
            kanal = -1001171502880
            liink = "https://t.me/joinchat/AAAAAEXTtyDMXmk804DQSQ"
        if "#خواهر_و_برادرانم" in fa:
            msgid = 8
            kanal = -1001395391486
            liink = "https://t.me/joinchat/InuGULJZjGQyNmY0"
        if "Emanet" in m:
            msgid = 9
            kanal = -1001270763452
            liink = "https://t.me/joinchat/AAAAAEu-T7wxLlMxliwJyw"
        if "Yasak Elma" in m:
            msgid = 11
            kanal = -1001239367474
            liink = "https://t.me/joinchat/AAAAAEnfPzLtPdGaXGMEzg"
        if "Ask Mantik Intikam" in m:
            msgid = 12
            kanal = -1001553912535
            liink = "https://t.me/joinchat/drN40_tQtfxhM2U0"
        if "Bir Zamanlar Cukurova" in m:
            msgid = 13
            kanal = -1001202280419
            liink = "https://t.me/joinchat/AAAAAEepV-MEDL0PP0ceQQ"
        if "#جلال_الدین_خوارزمشاهی" in fa:
            msgid = 14
            kanal = -1001587441079
            liink = "https://t.me/joinchat/kf7uh3Cq1bc1NDlk"
        if "EDHO" in m:
            msgid = 10
            kanal = -1001476598094
            liink = "https://t.me/joinchat/AAAAAFgDGU4Oh-eEV4LnRw"
        if "Mucize Doktor" in m:
            msgid = 37
            kanal = -1001346815849
            Dublink = "https://t.me/joinchat/P9gAggky76PbWSNG"
            liink = "https://t.me/joinchat/AAAAAFBGx2l-B8oY1cTbag"
        if "Akinci" in m:
            msgid = 30
            liink = "https://t.me/joinchat/VSCZ1_t7aF2IGPer"
        if "Teskilat" in m:
            msgid = 29
            liink = "https://t.me/joinchat/OxIJyjwjHjNlMGE0"
        if "Sadakatsiz" in m:
            msgid = 27
            liink = "https://t.me/joinchat/AAAAAFWnj9SBrHU-TrESBA"
        if "Baht Oyunu" in m:
            msgid = 15
            liink = "https://t.me/joinchat/mJW2DUgtK2I4NTc8"
        if "Gonul Dagi" in m:
            msgid = 24
            liink = "https://t.me/joinchat/AAAAAE172331Q2Zcumf_fg"
        if "Yemin" in m:
            msgid = 22
            liink = "https://t.me/joinchat/Hg0iLFonT7o0YjE0"
        if "Son Yaz" in m:
            msgid = 21
            liink = "https://t.me/joinchat/Sp5ApZRoHoye3pJe"
        if "Bir Zamanlar Kibris" in m:
            msgid = 19
            liink = "https://t.me/joinchat/ANEuc6YkrKAxN2Jk"
        if "Askin Tarifi" in m:
            msgid = 17
            liink = "https://t.me/joinchat/iy5rkCQ_KPpiZGE0"
        if "Yesilcam" in m:
            msgid = 20
            liink = "https://t.me/joinchat/8WqFLl-BjjhkYWU0"
        
        if "Eshghe Mashroot" in m:
            msgid = 36
            liink = "https://t.me/joinchat/djHUcZrf3Z1lMGFk"
        if "Ghermez" in m:
            msgid = 32
            liink = "https://t.me/joinchat/gxjiMKv7NRg0ZWI0"
        if "Saygi" in m:
            msgid = 28
        
        if "Ada Masali" in m:
            msgid = 16
        if "Iste Bu Benim Masalim" in m:
            msgid = 26
        if "Hukumsuz" in m:
            msgid = 25
        if "Be Eshghe To Sogand" in m:
            msgid = 35
            liink = "https://t.me/joinchat/WvQDR7-EQItkMjFk"
        
        if X == "Cukurova":
            msgid = 38
            liink = "https://t.me/joinchat/AAAAAFWu07lSP1xokkxQAQ"
        if "Alireza" in m:
            msgid = None
            liink = "https://t.me/joinchat/ZSbUcIaTW9UwYmFk"
        if "Aparteman Bigonahan" in m:
            msgid = 34
            liink = "https://t.me/joinchat/jH8N1M12K3A2ODY8"
        if "Masumlar Apartmani" in m:
            msgid = 34
            kanal = -1001492549082
            liink = "https://t.me/joinchat/WPZ92vFSbeyHJk-e"
            Dublink = "https://t.me/joinchat/jH8N1M12K3A2ODY8"
       
        if X == "2020":
            msgid = 31
            liink = "https://t.me/joinchat/0ShOWZms2mpjZjE8"
        if "Yek Jonun Yek Eshgh" in m:
            msgid = 33
            liink = "https://t.me/joinchat/05Yh16Cj_-UyNDA8"
        if "Mojeze Doctor" in m:
            msgid = 37
            liink = "https://t.me/joinchat/P9gAggky76PbWSNG"

        # Caption of Banner
     
        hash = '#' + f'{X.replace(" ", "_")}'
        if kanal is None:
            if (X in Copy) and (liink is None):
                kap = f"⬇️سریال {hash} ({fa.replace('#', '').replace('_', ' ') } ) ، بازیرنویس چسبیده \n✅ قسمت : {E}\n💢کل قسمت ها\n\n⬇️1080👉\n⬇️720👉\n⬇️480👉\n⬇️240👉\n\n🆔👉 @dlmacvin"
            elif (X in Copy) and (liink is not None):
                if Dublink is None:
                    kap = f"⬇️سریال {hash} ({fa.replace('#', '').replace('_', ' ') } ) ، بازیرنویس چسبیده \n✅ قسمت : {E}\n💢[کل قسمت ها]({liink})\n\n⬇️1080👉\n⬇️720👉\n⬇️480👉\n⬇️240👉\n\n🆔👉 @dlmacvin_new"
                if Dublink is not None:
                    kap = f"💢 سریال {fa.replace('#', '').replace('_', ' ') }\n💢[کل قسمت ها (دوبله فارسی)]({Dublink})\n💢[کل قسمت ها (زیرنویس چسبیده)]({liink})\n\n📦 تا قسمت {E} در کانال زیر اضافه شد👇👇👇\n{liink}\n\n🆔👉 @dlmacvin_new | {fa}"
            if (not X in Copy) and (liink is None):
                kap = f"⬇️سریال ({fa.replace('#', '').replace('_', ' ')} ) ، با دوبله فارسی \n✅تا قسمت {E}\n\n🆔👉 @dlmacvin_new"
            elif (not X in Copy) and (liink is not None):
                kap = f"⬇️سریال ({fa.replace('#', '').replace('_', ' ')} ) ، با دوبله فارسی \n✅تا قسمت {E}\n\n{liink}\n\n🆔👉 @dlmacvin_new"

        elif kanal is not None:
            if ("Duble" in m) and (Dublink is not None):
                kap = f"💢سریال {fa.replace('#', '').replace('_', ' ') } ، با دوبله فارسی \n✅ قسمت : {E}\n💢[کل قسمت ها (دوبله فارسی)]({Dublink})\n💢[کل قسمت ها (زیرنویس چسبیده)]({Dublink})\n\n⬇️1080👉\n⬇️720👉\n⬇️480👉\n⬇️240👉\n\n🆔👉 @dlmacvin_new"
                kap2 = f"💢 سریال {fa.replace('#', '').replace('_', ' ') }\n💢[کل قسمت ها (دوبله فارسی)]({Dublink})\n💢[کل قسمت ها (زیرنویس چسبیده)]({Dublink})\n\n📦 تا قسمت {E} در کانال زیر اضافه شد👇👇👇\n{liink}\n\n🆔👉 @dlmacvin_new | {fa}"
            if ("Duble" in m) and (Dublink is None):
                kap = f"⬇️سریال ({fa.replace('#', '').replace('_', ' ')} ) ، با دوبله فارسی \n✅تا قسمت {E}\n\n{liink}\n\n🆔👉 @dlmacvin_new"
                kap2 = f"⬇️سریال ({fa.replace('#', '').replace('_', ' ')} ) ، با دوبله فارسی \n✅تا قسمت {E}\n\n{liink}\n\n🆔👉 @dlmacvin_new"
            elif ("Hard-Sub" in m) and (Dublink is not None):
                kap = f"⬇️سریال {hash} ({fa.replace('#', '').replace('_', ' ') } ) ، بازیرنویس چسبیده \n✅ قسمت : {E}\n💢[کل قسمت ها]({liink})\n\n⬇️1080👉\n⬇️720👉\n⬇️480👉\n⬇️240👉\n\n🆔👉 @dlmacvin_new"
                kap2 = f"💢 سریال {fa.replace('#', '').replace('_', ' ') }\n💢[کل قسمت ها (دوبله فارسی)]({Dublink})\n💢[کل قسمت ها (زیرنویس چسبیده)]({liink})\n\n📦 تا قسمت {E} در کانال زیر اضافه شد👇👇👇\n{liink}\n\n🆔👉 @dlmacvin_new | {fa}"
            elif ("Hard-Sub" in m) and (Dublink is None):
                kap = f"⬇️سریال {hash} ({fa.replace('#', '').replace('_', ' ') } ) ، بازیرنویس چسبیده \n✅ قسمت : {E}\n💢[کل قسمت ها]({liink})\n\n⬇️1080👉\n⬇️720👉\n⬇️480👉\n⬇️240👉\n\n🆔👉 @dlmacvin_new"
                kap2 = f"⬇️سریال {hash} ({fa.replace('#', '').replace('_', ' ') } ) ، بازیرنویس چسبیده \n✅ قسمت : {E}\n💢[کل قسمت ها]({liink})\n\n⬇️1080👉\n⬇️720👉\n⬇️480👉\n⬇️240👉\n\n🆔👉 @dlmacvin_new"
                
        mkv240 = []
        mp4240 = []
        mkv480 = []
        mp4480 = []
        mkv720 = []
        mp4720 = []
        mkv1080 = []
        mp41080 = []
        F1 = None
        F2 = None
        F3 = None
        F4 = None
        # Duble Haaye 3 Ya 4 Filee
        if (message.chat.id == -1001457054266) and ((X in NoCopy) or (X in Copy)):
            if X in Copy:
                kanal = -1001457054266
            
            if "Duble" in N:
                M240 = f"{Fucc}\n🔹کیفیت : 240 \n🆔👉 @dlmacvin_new | {fa}"
                M480 = f"{Fucc}\n🔹کیفیت : 480 \n🆔👉 @dlmacvin_new | {fa}"
                M720 = f"{Fucc}\n🔹کیفیت : 720 \n🆔👉 @dlmacvin_new | {fa}"
                M1080 = f"{Fucc}\n🔹کیفیت : 1080 \n🆔👉 @dlmacvin_new | {fa}"
                
                async for mkv240p in User.search_messages(chat_id=message.chat.id, query=M240, filter='document'):
                    Fnme = mkv240p.document.file_name
                    mkv240.append(Fnme)
                async for mkv480p in User.search_messages(chat_id=message.chat.id, query=M480, filter='document'):
                    Fnme = mkv480p.document.file_name
                    mkv480.append(Fnme)
                async for mkv720p in User.search_messages(chat_id=message.chat.id, query=M720, filter='document'):
                    Fnme = mkv720p.document.file_name
                    mkv720.append(Fnme)
                async for mkv1080p in User.search_messages(chat_id=message.chat.id, query=M1080, filter='document'):
                    Fnme = mkv1080p.document.file_name
                    mkv1080.append(Fnme)

                if mkv240 and mkv720 and mkv480:
                    if mkv1080:
                        gold = "f"
                        if gold == "f":
                            F1 = await mkv240p.copy(chat_id=kanal)
                            F2 = await mkv480p.copy(chat_id=kanal)
                            F3 = await mkv720p.copy(chat_id=kanal)
                            F4 = await mkv1080p.copy(chat_id=kanal)
                        await bot.copy_message(chat_id=kanal, from_chat_id=-1001441684079, message_id=msgid, caption=kap, parse_mode='markdown')
                        await F1.copy(chat_id=kanal)
                        await F2.copy(chat_id=kanal)
                        await F3.copy(chat_id=kanal)
                        await F4.copy(chat_id=kanal)
                        await F1.delete()
                        await F2.delete()
                        await F3.delete()
                        await F4.delete()       
                    else:
                        gold = "f"
                        if gold == "f":
                            F1 = await mkv240p.copy(chat_id=kanal)
                            F2 = await mkv480p.copy(chat_id=kanal)
                            F3 = await mkv720p.copy(chat_id=kanal)
                        await bot.copy_message(chat_id=kanal, from_chat_id=-1001441684079, message_id=msgid, caption=kap, parse_mode='markdown')
                        await F1.copy(chat_id=kanal)
                        await F2.copy(chat_id=kanal)
                        await F3.copy(chat_id=kanal)
                        await F1.delete()
                        await F2.delete()
                        await F3.delete()
                    if (X in Copy) and (kap2 is not None):
                        await bot.copy_message(chat_id=kanal, from_chat_id=-1001441684079, message_id=msgid, caption=kap2, parse_mode='markdown')
            
            # Zirnevis haaye 6 Ya 8 Filee
            elif "Hard-Sub" in N:
                
                M240 = f"{Fucc}\n🔹کیفیت : 240 \n🔻تماشای آنلاین بدون فیلتر شکن: \n🆔👉 @dlmacvin_new"
                M480 = f"{Fucc}\n🔹کیفیت : 480 \n🔻تماشای آنلاین بدون فیلتر شکن: \n🆔👉 @dlmacvin_new"
                M720 = f"{Fucc}\n🔹کیفیت : 720 \n🔻تماشای آنلاین بدون فیلتر شکن: \n🆔👉 @dlmacvin_new"
                M1080 = f"{Fucc}\n🔹کیفیت : 1080 \n🔻تماشای آنلاین بدون فیلتر شکن: \n🆔👉 @dlmacvin_new"
               
                async for mkv240p in User.search_messages(chat_id=message.chat.id, query=M240, filter='document'):
                    Fnme = mkv240p.document.file_name
                    mkv240.append(Fnme)
                
                async for mp4240p in User.search_messages(chat_id=message.chat.id, query=M240, filter='video'):
                    Fnme = mp4240p.video.file_name
                    mp4240.append(Fnme)
                
                async for mkv480p in User.search_messages(chat_id=message.chat.id, query=M480, filter='document'):
                    Fnme = mkv480p.document.file_name
                    mkv480.append(Fnme)
 
                async for mp4480p in User.search_messages(chat_id=message.chat.id, query=M480, filter='video'):
                    Fnme = mp4480p.video.file_name
                    mp4480.append(Fnme)

                async for mkv720p in User.search_messages(chat_id=message.chat.id, query=M720, filter='document'):
                    Fnme = mkv720p.document.file_name
                    mkv720.append(Fnme)
                
                async for mp4720p in User.search_messages(chat_id=message.chat.id, query=M720, filter='video'):
                    Fnme = mp4720p.video.file_name
                    mp4720.append(Fnme)
                
                async for mkv1080p in User.search_messages(chat_id=message.chat.id, query=M1080, filter='document'):
                    Fnme = mkv1080p.document.file_name
                    mkv1080.append(Fnme)
                
                async for mp41080p in User.search_messages(chat_id=message.chat.id, query=M1080, filter='video'):
                    Fnme = mp41080p.video.file_name
                    mp41080.append(Fnme)
                
                if mp4240 and mp4480 and mp4720 and mkv240 and mkv720 and mkv480:
                    if mkv1080 and mp41080:
                        gold = "f"
                        if gold == "f":
                            await mp4240p.copy(chat_id=kanal)
                            await mp4480p.copy(chat_id=kanal)
                            await mp4720p.copy(chat_id=kanal)
                            await mp41080p.copy(chat_id=kanal)
                            F1 = await mkv240p.copy(chat_id=kanal)
                            F2 = await mkv480p.copy(chat_id=kanal)
                            F3 = await mkv720p.copy(chat_id=kanal)
                            F4 = await mkv1080p.copy(chat_id=kanal)
                        await bot.copy_message(chat_id=kanal, from_chat_id=-1001441684079, message_id=msgid, caption=f"{kap}", parse_mode='markdown')
                        await F1.copy(chat_id=kanal)
                        await F2.copy(chat_id=kanal)
                        await F3.copy(chat_id=kanal)
                        await F4.copy(chat_id=kanal)
                        await F1.delete()
                        await F2.delete()
                        await F3.delete()
                        await F4.delete()
                    elif not mkv1080 and not mp41080:
                        gold = "f"
                        if gold == "f":
                            await mp4240p.copy(chat_id=kanal)
                            await mp4480p.copy(chat_id=kanal)
                            await mp4720p.copy(chat_id=kanal)
                            F1 = await mkv240p.copy(chat_id=kanal)
                            F2 = await mkv480p.copy(chat_id=kanal)
                            F3 = await mkv720p.copy(chat_id=kanal)
                        await bot.copy_message(chat_id=kanal, from_chat_id=-1001441684079, message_id=msgid, caption=f"{kap}", parse_mode='markdown')
                        await F1.copy(chat_id=kanal)
                        await F2.copy(chat_id=kanal)
                        await F3.copy(chat_id=kanal)
                        await F1.delete()
                        await F2.delete()
                        await F3.delete()
                    if (X in Copy) and (kap2 is not None):
                        await bot.copy_message(chat_id=-1001457054266, from_chat_id=-1001441684079, message_id=msgid, caption=f"{kap2}", parse_mode='markdown')
                      
                      
        # Duble Haaye Tak File
        if (message.chat.id == -1001457054266):
            try:
                if "Ghermez" in media.file_name:
                    await msg.copy(chat_id=-1001166919373)
                    await bot.copy_message(chat_id=-1001457054266, from_chat_id=-1001441684079, message_id=msgid, caption=kap, parse_mode='markdown')
    
                elif media.file_name.__contains__("Cukurova") and media.file_name.__contains__("Duble"):
                    await msg.copy(chat_id=-1001437520825) 
                    await bot.copy_message(chat_id=-1001457054266, from_chat_id=-1001441684079, message_id=msgid, caption=kap, parse_mode='markdown')
    
                elif "Mojeze Doctor" in media.file_name:
                    await msg.copy(chat_id=-1001071120514)
                    await bot.copy_message(chat_id=-1001457054266, from_chat_id=-1001441684079, message_id=msgid, caption=kap, parse_mode='markdown')
    
                elif "Yek Jonun Yek Eshgh" in media.file_name:
                    await msg.copy(chat_id=-1001546442991)
                    await bot.copy_message(chat_id=-1001457054266, from_chat_id=-1001441684079, message_id=msgid, caption=kap, parse_mode='markdown')
    
                elif media.file_name.__contains__("2020") and media.file_name.__contains__("Duble"):
                    await msg.copy(chat_id=-1001322014891)
                    await bot.copy_message(chat_id=-1001457054266, from_chat_id=-1001441684079, message_id=msgid, caption=kap, parse_mode='markdown')
    
                elif "Eshghe Mashroot" in media.file_name:
                    await msg.copy(chat_id=-1001409508844)
                    await bot.copy_message(chat_id=-1001457054266, from_chat_id=-1001441684079, message_id=msgid, caption=kap, parse_mode='markdown')
    
                elif "Alireza" in media.file_name:
                    await msg.copy(chat_id=-1001537554747)
                    
                elif "Eshgh Az No" in media.file_name:
                    await msg.copy(chat_id=-1001462444753)
                    
                elif "Setare Shomali" in media.file_name:
                    await msg.copy(chat_id=-1001146657589)
                    
                elif "Be Eshghe To Sogand" in media.file_name:
                    await msg.copy(chat_id=-1001592624165)
                    await bot.copy_message(chat_id=-1001457054266, from_chat_id=-1001441684079, message_id=msgid, caption=kap, parse_mode='markdown')
    
                elif "Aparteman Bigonahan" in media.file_name:
                    await msg.copy(chat_id=-1001588137496)
                    await bot.copy_message(chat_id=-1001457054266, from_chat_id=-1001441684079, message_id=msgid, caption=kap, parse_mode='markdown')
    
            except Exception as error:
                print(error)
                   
    
# Start Clients
Bot.start()
User.start()
# Loop Clients till Disconnects
idle()
# After Disconnects,
# Stop Clients
Bot.stop()
User.stop()
