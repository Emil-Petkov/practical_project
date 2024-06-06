import os

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from gtts import gTTS

pygame.mixer.init()


print("""
 __        __         _                                   
 \ \      / /   ___  | |   ___    ___    _ __ ___     ___ 
  \ \ /\ / /   / _ \ | |  / __|  / _ \  | '_ ` _ \   / _ \\
   \ V  V /   |  __/ | | | (__  | (_) | | | | | | | |  __/
    \_/\_/     \___| |_|  \___|  \___/  |_| |_| |_|  \___|
                                                          
  _                                                       
 | |_    ___                                              
 | __|  / _ \                                             
 | |_  | (_) |                                            
  \__|  \___/                                             
                                                          
  ____                _        _     _                    
 |  _ \      __ _    | | __   (_)   | |_      __ _        
 | |_) |    / _` |   | |/ /   | |   | __|    / _` |       
 |  _ <    | (_| |   |   <    | |   | |_    | (_| |       
 |_| \_\    \__,_|   |_|\_\   |_|    \__|    \__,_|       
                                                    
""")
def text_to_speech(text, lang):
    tts = gTTS(text=text, lang=lang)
    filename = "temp.mp3"
    tts.save(filename)
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue
    pygame.mixer.music.unload()
    os.remove(filename)


def print_and_speak(text, lang):
    print(text)
    text_to_speech(text, lang)


def choose_language():
    print("Моля изберете език, като въведете цифрата 1 или 2 / Please choose a language by entering the number 1 or 2")
    print("1: Български")
    print("2: English")
    while True:
        choice = input("Вашият избор / Your choice: ")
        if choice == '1':
            return 'bg'
        elif choice == '2':
            return 'en'
        else:
            print("\nНевалиден избор, моля опитайте отново / Invalid choice, please try again.")


facts = {
    'bg': {
        1: "Население",
        2: "История",
        3: "География",
        4: "Религия",
        5: "Икономика",
        6: "Инфраструктура",
        7: "Културни и природни забележителности",
        8: "Интересни факти за с. Ракита"
    },

    'en': {
        1: "Population",
        2: "History",
        3: "Geography",
        4: "Religion",
        5: "Economy",
        6: "Infrastructure",
        7: "Cultural and Natural Landmarks",
        8: "Interesting facts about Rakita"
    }
}

detailed_facts = {
    'bg': {
        1: {
            "Категория": "Население",
            "Подкатегории": {
                1: {
                    "Заглавие": "Брой на населението",
                    "Текст": "По данни от последното преброяване населението наброява 804 души към (15 март 2024 г.)"
                }
            }
        },
        2: {
            "Категория": "История",
            "Подкатегории": {
                1: {
                    "Заглавие": "Училище",
                    "Текст": "Има данни за съществуване на училище още през 1850 г."
                },
                2: {
                    "Заглавие": "Прогимназия",
                    "Текст": "В Ракита още през 1894 година е открита прогимназия, в която се учат много ученици от околните селища. Това е първата прогимназия в района."
                },
                3: {
                    "Заглавие": "Читалище",
                    "Текст": "Читалището е основано през 1902 – 1903. Сегашният му наследник – читалище „Н. Й. Вапцаров“ се помещава в сградата на кметството."
                }
            }
        },
        3: {
            "Категория": "География",
            "Подкатегории": {
                1: {
                    "Заглавие": "Разположение",
                    "Текст": "Селото се намира на около 41 km югозападно от гр. Плевен по главен път София-Русе, на територията на община Червен бряг. "
                             "До с. Ракита може да се стигне с автомобилен транспорт, отбивайки се вдясно от разклона при село Радомирци, община Червен бряг, на главен път София-Русе."
                },
                2: {
                    "Заглавие": "Релеф",
                    "Текст": "Надморската височина е около 150 – 200 m, климатът не се различава от останалата част от региона. "
                             "Има изграден малък изкуствен водоем-язовир, носещ името „Соватски дол“, намиращ се югоизточно от селото по пътя за гр. Тетевен, в гориста местност с преобладаваща дъбова гора."
                }
            }
        },
        4: {
            "Категория": "Религии",
            "Подкатегории": {
                1: {
                    "Заглавие": "Източно православие",
                    "Текст": "Почитат се всички източноправославни празници, което отразява дълбоките корени на християнството в региона."
                },
                2: {
                    "Заглавие": "Църква Св. Параскева",
                    "Текст": "В селото има църква на името на св. Параскева (света Петка)."
                },
                3: {
                    "Заглавие": "Събор",
                    "Текст": "В края на октомври, на Петковден, се провежда съборът на селото. "
                             "Денят е избран заради света Петка, която е покровителка на селото и на която е посветена църквата."
                }
            }
        },
        5: {
            "Категория": "Икономика",
            "Подкатегории": {
                1: {
                    "Заглавие": "Земеделие и животновъдство",
                    "Текст": "Преобладаващите отрасли в селото и региона са земеделието и животновъдството."
                },
                2: {
                    "Заглавие": "ВЕЦ",
                    "Текст": "В непосредствена близост до с. Ракита в североизточна посока има изградена ВЕЦ с инсталирана мощност 2x2,6 MW. Електроцентралата ползва вода от т.нар. Витска напоителна система, която преминава през землището на Ракита."
                }
            }
        },
        6: {
            "Категория": "Инфраструктура",
            "Подкатегории": {
                1: {
                    "Заглавие": "Инфраструктура",
                    "Текст": "Селото има сравнително добра инфраструктура – мобилна връзка, интернет, ток, вода (целогодишно)."
                },
                2: {
                    "Заглавие": "Транспорт",
                    "Текст": "Съществува автобусен транспорт до градовете Червен бряг и Плевен. От с. Телиш, което е на разстояние от 7 km, може да се направи връзка с пътнически влак в направленията София, Русе и Варна."
                }
            }
        },
        7: {
            "Категория": "Културни и природни забележителности",
            "Подкатегории": {
                1: {
                    "Заглавие": "Паметници и исторически обекти",
                    "Текст": "Три надгробни могили в землището на селото. Антични селища в района на селото и в местността „Умника“. В покрайнините на селото в североизточна, източна и югоизточна посока е минавал римски път с калдъръм от редени камъни. Могилата – градище в местността „Черковното“. Паметник на загиналите жители на Ракита във войните през 20-ти век. Паметна плоча на част от загиналите войни във войните – намира се в селското гробище. Паметен знак на артилеристи от лейбгвардията, участвали в боевете при Телиш 24 – 28 октомври 1877 г."
                },
                2: {
                    "Заглавие": "Природни забележителности",
                    "Текст": "Местността „Езерото“ с множество пещери и карстови извори. От там селото се снабдява с питейна вода целогодишно, тъй като водоизточникът не пресъхва и през най-сухите години. Скален мост „Седларката“. Малко по-нагоре от Седларката се намира равна пещера, която започва сред полето във фуниевиден слог, така че не се вижда от пръв поглед. Дълга е повече от километър. Има стеснения и големи зали, множество сталагмити и сталактити, вътрешна река и пропаст. Водата на реката излиза на повърхността в пещерата под Седларката. През 60-те години там е имало мандра на ТКЗС. Понастоящем входът на пещерата в полето е засипан с пръст, за да се предотврати нещастен случай на деца, влизащи в пещерата."
                }
            }
        },
        8: {
            "Категория": "Интересни факти за с. Ракита",
            "Подкатегории": {
                1: {
                    "Заглавие": "Васил Левски",
                    "Текст": "На мястото на сегашната поща е била къщата на Дошо Йотов, в която се е укривал Васил Иванов Кунчев (Левски), организирайки революционните дела в региона."
                },
                2: {
                    "Заглавие": "Римски път",
                    "Текст": "По калдъръмения римски път от редени камъни, минаващ в покрайнините на селото е минавал Александър Велики по време на своите завоевания."

                }
            }
        }
    },
    'en': {
        1: {
            "Category": "Population",
            "Subcategories": {
                1: {
                    "Title": "Population Count",
                    "Text": "According to the latest census, the population counts 804 people as of (March 15, 2024)."
                }
            }
        },
        2: {
            "Category": "History",
            "Subcategories": {
                1: {
                    "Title": "School",
                    "Text": "There are records of a school existing since 1850."
                },
                2: {
                    "Title": "Secondary School",
                    "Text": "In Rakita, a secondary school was opened in 1894, where many students from surrounding settlements studied. This is the first secondary school in the area."
                },
                3: {
                    "Title": "Community Center",
                    "Text": "The community center was founded in 1902-1903. Its current successor, the community center 'N. Y. Vaptsarov', is housed in the building of the mayor's office."
                }
            }
        },
        3: {
            "Category": "Geography",
            "Subcategories": {
                1: {
                    "Title": "Location",
                    "Text": "The village is located about 41 km southwest of Pleven city on the main road Sofia-Ruse, in the territory of Cherven Bryag municipality. "
                            "Rakita village can be reached by car, turning right from the junction at Radomirtsi village, Cherven Bryag municipality, on the main road Sofia-Ruse."
                },
                2: {
                    "Title": "Terrain",
                    "Text": "The altitude is about 150-200 m, the climate does not differ from the rest of the region. "
                            "There is a small artificial reservoir called 'Sovatski Dol', located southeast of the village on the road to Teteven, in a forested area with predominant oak forest."
                }
            }
        },
        4: {
            "Category": "Religions",
            "Subcategories": {
                1: {
                    "Title": "Eastern Orthodoxy",
                    "Text": "All Eastern Orthodox holidays are celebrated, reflecting the deep roots of Christianity in the region."
                },
                2: {
                    "Title": "Church of St. Paraskeva",
                    "Text": "There is a church in the village named after St. Paraskeva (St. Petka)."
                },
                3: {
                    "Title": "Festival",
                    "Text": "At the end of October, on Petkovden, the village's festival is held. "
                            "The day is chosen in honor of St. Petka, the patron saint of the village, to whom the church is dedicated."
                }
            }
        },
        5: {
            "Category": "Economy",
            "Subcategories": {
                1: {
                    "Title": "Agriculture and Animal Husbandry",
                    "Text": "The predominant sectors in the village and the region are agriculture and animal husbandry."
                },
                2: {
                    "Title": "Hydroelectric Power Plant",
                    "Text": "In the immediate vicinity of Rakita village to the northeast, there is a hydroelectric power plant with an installed capacity of 2x2.6 MW. The power plant uses water from the so-called Vitska irrigation system, which passes through Rakita's land."
                }
            }
        },
        6: {
            "Category": "Infrastructure",
            "Subcategories": {
                1: {
                    "Title": "Infrastructure",
                    "Text": "The village has relatively good infrastructure - mobile connection, internet, electricity, water (year-round)."
                },
                2: {
                    "Title": "Transport",
                    "Text": "There is bus transport to the cities of Cherven Bryag and Pleven. From Telish village, which is 7 km away, there is a connection to passenger trains in the directions of Sofia, Ruse, and Varna."
                }
            }
        },
        7: {
            "Category": "Cultural and Natural Landmarks",
            "Subcategories": {
                1: {
                    "Title": "Monuments and Historical Sites",
                    "Text": "Three burial mounds in the village's land. Ancient settlements in the area of the village and the 'Umnika' area. A Roman road with cobblestones passed through the outskirts of the village in the northeast, east, and southeast directions. The mound - fortress in the 'Cherkovnoto' area. Monument to the fallen residents of Rakita in the wars of the 20th century. Memorial plaque for some of the soldiers who died in the wars - located in the village cemetery. Memorial sign for artillerymen from the guards who participated in the battles near Telish on October 24-28, 1877."
                },
                2: {
                    "Title": "Natural Landmarks",
                    "Text": "The 'Lake' area with numerous caves and karst springs. The village is supplied with drinking water from there year-round, as the water source does not dry up even in the driest years. Stone bridge 'Sedlarkata'. A little further up from Sedlarkata, there is a flat cave that starts in the field in a funnel-shaped ditch, so it is not visible at first glance. It is more than a kilometer long. There are narrow passages and large halls, numerous stalagmites and stalactites, an underground river, and a chasm. The river water surfaces in the cave below Sedlarkata. In the 1960s, there was a dairy farm of the cooperative farm (TKZS) there. Currently, the cave entrance in the field is filled with soil to prevent accidents with children entering the cave."
                }
            }
        },
        8: {
            "Category": "Interesting Facts about Rakita",
            "Subcategories": {
                1: {
                    "Title": "Vasil Levski",
                    "Text": "On the site of the current post office was the house of Dosho Yotov, where Vasil Ivanov Kunchev (Levski) hid, organizing revolutionary activities in the region."
                },
                2: {
                    "Title": "Roman Road",
                    "Text": "Along the cobblestone Roman road, made of laid stones and passing through the outskirts of the village, Alexander the Great passed during his conquests."
                }
            }
        }
    }
}


def display_subtopics(topic_id, lang):
    subtopics_key = "Подкатегории" if lang == 'bg' else "Subcategories"
    category_key = "Категория" if lang == 'bg' else "Category"
    title_key = "Заглавие" if lang == 'bg' else "Title"
    text_key = "Текст" if lang == 'bg' else "Text"

    subtopics = detailed_facts[lang][topic_id][subtopics_key]
    while True:
        print(f"\n{detailed_facts[lang][topic_id][category_key]}")
        if lang == 'bg':
            print("Изберете подтема за повече информация:")
        else:
            print("Choose a subtopic for more information:")

        for key, value in subtopics.items():
            print(f"{key}: {value[title_key]}")

        if lang == 'bg':
            print("0: Връщане към основното меню")
            sub_choice = input("\nВашият избор: ")
        else:
            print("0: Return to the main menu")
            sub_choice = input("\nYour choice: ")

        try:
            sub_choice = int(sub_choice)
        except ValueError:
            if lang == 'bg':
                print("Невалиден избор, моля опитайте отново.")
            else:
                print("Invalid choice, please try again.")
            continue

        if sub_choice == 0:
            break
        elif sub_choice in subtopics:
            print_and_speak(subtopics[sub_choice][text_key], lang)
            if lang == 'bg':
                continue_choice = input(
                    "\nИскате ли да научите още факти по тази тема? (напишете 1 за да продължите или 0 за край): ")
            else:
                continue_choice = input(
                    "\nDo you want to learn more facts on this topic? (type 1 to continue or 0 to stop): ")

            if continue_choice == '1':
                continue
            elif continue_choice == '0':
                break
            else:
                if lang == 'bg':
                    print("Невалиден избор, моля опитайте отново.")
                else:
                    print("Invalid choice, please try again.")

        else:
            if lang == 'bg':
                print("Невалиден избор, моля опитайте отново.")
            else:
                print("Invalid choice, please try again.")


def main():
    lang = choose_language()
    while True:
        if lang == 'bg':
            print("\nИзберете категория за село Ракита:\n")
        else:
            print("\nChoose a category for the village of Rakita:\n")

        for key, value in facts[lang].items():
            print(f"{key}: {value}")

        if lang == 'bg':
            print("0: Изход")
            choice = input("\nВашият избор: ")
        else:
            print("0: Exit")
            choice = input("\nYour choice: ")

        try:
            choice = int(choice)
        except ValueError:
            if lang == 'bg':
                print("Невалиден избор, моля опитайте отново.")
            else:
                print("Invalid choice, please try again.")
            continue

        if choice == 0:
            break
        elif choice in facts[lang]:
            display_subtopics(choice, lang)
        else:
            if lang == 'bg':
                print("Невалиден избор, моля опитайте отново.")
            else:
                print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
