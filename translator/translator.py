from googletrans import Translator
import time

print("""
Azerbaijani (az)
Albanian (sq)
Amharic (am)
Arabic (ar)
Armenian (hy)
Afrikaans (af)
Basque (eu)
Bashkir (ba)
Belarusian (be)
Bengali (bn)
Bosnian (bs)
Bulgarian (bg)
Walloon (wa)
Vietnamese (vi)
Galician (gl)
Upper Sorbian (hsb)
Greek (el)
Georgian (ka)
Gujarati (gu)
Danish (da)
Hebrew (he)
Yiddish (yi)
Indonesian (id)
Irish (ga)
Icelandic (is)
Spanish (es)
Italian (it)
Yoruba (yo)
Kazakh (kk)
Kannada (kn)
Catalan (ca)
Kyrgyz (ky)
Simplified Chinese (zh-CN)
Traditional Chinese (zh-TW)
Korean (ko)
Kosovan (sq-KS)
Kurdish (ku)
Khmer (km)
Latvian (lv)
Lithuanian (lt)
Luxembourgish (lb)
Macedonian (mk)
Malay (ms)
Malayalam (ml)
Maltese (mt)
Maori (mi)
Marathi (mr)
Mari (mhr)
Mongolian (mn)
German (de)
Nepali (ne)
Dutch (nl)
Norwegian (no)
Punjabi (pa)
Papiamento (pap)
Persian (fa)
Polish (pl)
Portuguese (pt)
Pashto (ps)
Romanian (ro)
Russian (ru)
Samoan (sm)
Serbian (sr)
Sindhi (sd)
Slovak (sk)
Slovenian (sl)
Swahili (sw)
Sundanese (su)
Tajik (tg)
Thai (th)
Tamil (ta)
""")


def translate_text(source_lang, target_lang, text):
    translator = Translator()
    try:
        translated_text = translator.translate(text, src=source_lang, dest=target_lang)
        print(translated_text.text)

    except Exception as e:
        print("Translation error:", str(e))


print("""____________________________________________________
Welcome to my translator : )\n
____________________________________________________""")

while True:
    source_lang = input("\nEnter the code the language you want to translate from: ")
    target_lang = input("Enter the code of the language in which you want the translation to be made: ")
    text = input("\nEnter the text to be translated: ")
    translate_text(source_lang, target_lang, text)

    command = input("\nDo you want to continue? (y/n): ").lower()
    if command == "y":
        continue

    elif command == "n":
        print("Have a good day!")
        time.sleep(5)
        break
    else:
        print("Invalid command! The program will close after 5 seconds.")
        time.sleep(5)
        break
