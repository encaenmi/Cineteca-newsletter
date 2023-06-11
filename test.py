import os
from utils import *

info_for_text_test = [{
    'cineteca_title': 'Holy Spider',
    'cineteca_director': 'Ali Abbasi',
    'cineteca_year': 2022,
    'cineteca_showtime': '2023-06-11 20:45',
    'result_title': 'Holy Spider',
    'release_date': '2022-07-13',
    'rating': 7.45,
    'popularity': 18.529,
    'overview':
    'A journalist descends into the dark underbelly of the Iranian holy city of Mashhad as she investigates the serial killings of sex workers by the so called "Spider Killer", who believes he is cleansing the streets of sinners.',
    'votes': 189
}, {
    'cineteca_title': 'Beau Is Afraid',
    'cineteca_director': 'Ari Aster',
    'cineteca_year': 2023,
    'cineteca_showtime': '2023-06-11 14:00',
    'result_title': 'Beau Is Afraid',
    'release_date': '2023-03-11',
    'rating': 7.176,
    'popularity': 37.996,
    'overview':
    'A paranoid man embarks on an epic odyssey to get home to his mother.',
    'votes': 270
}, {
    'cineteca_title': 'Blondi',
    'cineteca_director': 'Dolores Fonzi',
    'cineteca_year': 2023,
    'cineteca_showtime': '2023-06-11 18:15',
    'result_title': 'Blondi',
    'release_date': '2023-06-01',
    'rating': 0.0,
    'popularity': 7.045,
    'overview':
    "Blondi and Mirko live together, listen to the same music, watch the same films, like to smoke pot and share the same friends. But, even though they seem to be the same age, Blondi is Mirko's mother.",
    'votes': 0
}, {
    'cineteca_title': 'Ts onot',
    'cineteca_director':
    'Kaori Oda. Con: Voces de Araceli del Rosario Chulim Tun y Juan de la Rosa Mibmay',
    'cineteca_year': 2019,
    'cineteca_showtime': '2023-06-11 14:45',
    'result_title': 'Cenote',
    'release_date': '2019-10-12',
    'rating': 4.438,
    'popularity': 4.198,
    'overview':
    'Cenotes—sources of water that in ancient Mayan civilization were said to connect the real world and the afterlife. The past and present of the people living in and around them intersect, and distant memories echo throughout immersive scenes of light and darkness.',
    'votes': 8
}, {
    'cineteca_title': 'ColOZio',
    'cineteca_director': 'Artemio Narro',
    'cineteca_year': 2020,
    'cineteca_showtime': '2023-06-11 12:00',
    'result_title': 'ColOZio',
    'release_date': '2020-01-24',
    'rating': 5.818,
    'popularity': 0.684,
    'overview':
    "In 1994, Mexican presidential candidate Colosio garnered attention for his democratic ideology and anti-corruption stance until he was shot through the head in Tijuana. The wondrous ColOZio, which is partly based on true events, starts three days prior with a prophecy to tripping friends Diego and Gael: save Colosio from death. The duo's dancing in a kaleidoscopic animated, almost 10-minute-long title sequence subsequently sets the tone for a playful, delightfully over-the-top road movie. Expect mythical apparitions, cartoony chases and plenty of drink and drugs.",
    'votes': 11
}, {
    'cineteca_title': 'Eami',
    'cineteca_director': 'Paz Encina',
    'cineteca_year': 2022,
    'cineteca_showtime': '2023-06-11 18:45',
    'result_title': 'Eami',
    'release_date': '2022-01-26',
    'rating': 5.3,
    'popularity': 2.148,
    'overview':
    'Eami means ‘forest’ in Ayoreo. It also means ‘world’.  The story happens in the Paraguayan Chaco, the territory with the highest deforestation rate in the world. 25,000 hectares of forest are being deforested a month in this territory which would mean an average of 841 hectares a day or 35 hectares per hour. The forest barely lives and this only due to a reserve that the Totobiegosode people achieved in a legal manner. They call Chaidi this place which means ancestral land or the place where we always lived and it is part of the "Ayoreo Totobiegosode Natural and Cultural Heritage". Before this, they had to live through the traumatic situation of leaving the territory behind and surviving a war. It is the story of the Ayoreo Totobiegosode people, told from the point of view of Asoja, a bird-god with the ability to bring an omniscient- temporal gaze, who becomes the narrator of this story developed in a crossing between documentary and fiction.',
    'votes': 3
}, {
    'cineteca_title': 'El film justifica los medios',
    'cineteca_director': 'Jacobo del Castillo',
    'cineteca_year': 2021,
    'cineteca_showtime': '2023-06-11 16:30',
    'result_title': 'El Film Justifica los Medios',
    'release_date': '2021-09-24',
    'rating': 0.0,
    'popularity': 1.465,
    'overview':
    'Through the recovery and re-montage of various film fragments and the commentary of three filmmakers - Carlos Álvarez, Marta Rodríguez, and Carlos Sánchez - a historical and aesthetic journey is proposed through a foundational moment for filmmaking in Colombia (1965-1975), whose images constitute a revolution on the screen. This documentary journey tells how, at a time when the film industry was just being consolidated, a generation of young filmmakers brought about a moment of rupture, subverting official cinema by taking the media to experiment, denounce and narrate other realities in Colombia at the end of the 1960s.',
    'votes': 0
}, {
    'cineteca_title': 'Le procès',
    'cineteca_director': 'Orson Welles',
    'cineteca_year': 1962,
    'cineteca_showtime': '2023-06-11 18:30',
    'result_title': 'The Trial',
    'release_date': '1962-12-21',
    'rating': 7.486,
    'popularity': 8.733,
    'overview':
    'Josef K wakes up in the morning and finds the police in his room. They tell him that he is on trial but nobody tells him what he is accused of. In order to find out about the reason for this accusation and to protest his innocence, he tries to look behind the façade of the judicial system. But since this remains fruitless, there seems to be no chance for him to escape from this Kafkaesque nightmare.',
    'votes': 403
}, {
    'cineteca_title': 'El sembrador',
    'cineteca_director': 'Melissa Elizondo',
    'cineteca_year': 2018,
    'cineteca_showtime': '2023-06-11 13:15',
    'result_title': 'The Sower',
    'release_date': '2018-10-25',
    'rating': 7.3,
    'popularity': 0.948,
    'overview':
    'Bartolomé, a teacher in a multigrade school on the mountains of Chiapas in Mexico, knows well that pedagogy is not based on textbooks and cannot fit behind the four walls of a classroom. A true sower of knowledge unravels his philosophy and method and becomes a beacon of hope for the creation of a humanistic model of education based on curiosity and love for the outside world.',
    'votes': 18
}, {
    'cineteca_title': 'En corps',
    'cineteca_director': 'Cédric Klapisch',
    'cineteca_year': 2022,
    'cineteca_showtime': '2023-06-11 15:30',
    'result_title': 'Rise',
    'release_date': '2022-03-30',
    'rating': 7.537,
    'popularity': 8.868,
    'overview':
    'Elise thought she had the perfect life: an ideal boyfriend and a promising career as a ballet dancer. It all falls apart the day she catches him cheating on her with her stage backup; and after she suffers an injury on stage, it seems like she might not be able to dance ever again.  A heartwarming and inspiring story that tells us how sometimes, the worst thing that could happen may turn out to be the best.',
    'votes': 298
}, {
    'cineteca_title': 'Syk pike',
    'cineteca_director': 'Kristoffer Borgli',
    'cineteca_year': 2022,
    'cineteca_showtime': '2023-06-11 20:30',
    'result_title': 'Sick of Myself',
    'release_date': '2022-09-30',
    'rating': 7.1,
    'popularity': 13.484,
    'overview':
    'Signe and Thomas are in an unhealthy, competitive relationship that takes a vicious turn when Thomas suddenly breaks through as a contemporary artist. In response, Signe makes a desperate attempt to regain her status by creating a new persona hell-bent on attracting attention and sympathy.',
    'votes': 44
}, {
    'cineteca_title': 'Esquí',
    'cineteca_director': 'Manque La Banca',
    'cineteca_year': 2021,
    'cineteca_showtime': '2023-06-11 19:00',
    'result_title': 'Ski',
    'release_date': '2021-03-05',
    'rating': 7.0,
    'popularity': 0.642,
    'overview':
    'Otto Meiling is the German alpinist who manufactured the first skis and contributed to establish the biggest ski resort of Latin America in Patagonia, Argentina at the beginning of the 20th century. Carlos Echeverría is a film director that started a documentary about him but did not finish it for dark reasons. Esperanza is the current under-20 national ski champion and during her training she meets Miguel, a ski lift operator. Through Miguel’s eyes, we discover the world of the people who work there so others can practice the sport of skiing. Most of the workers are Mapuche descendants and have never skied. The relationship between these characters shows the hidden universe of labour relations that are generated during the ski peak season.',
    'votes': 1
}, {
    'cineteca_title': 'Hijo de monarcas',
    'cineteca_director': 'Alexis Gambis',
    'cineteca_year': 2020,
    'cineteca_showtime': '2023-06-11 16:15',
    'result_title': 'Son of Monarchs',
    'release_date': '2021-10-15',
    'rating': 5.2,
    'popularity': 2.368,
    'overview':
    'A Mexican biologist living in New York returns to his hometown, nestled in the majestic butterfly forests of Michoacán. The journey forces him to confront past traumas and reflect on his hybrid identity, sparking a personal metamorphosis.',
    'votes': 5
}, {
    'cineteca_title': 'Home Is Somewhere Else',
    'cineteca_director': 'Carlos Hagerman',
    'cineteca_year': 2022,
    'cineteca_showtime': '2023-06-11 14:45',
    'result_title': 'Home Is Somewhere Else',
    'release_date': '2022-06-13',
    'rating': 9.25,
    'popularity': 2.418,
    'overview':
    'Accessing the "American Dream" is still not possible for everyone, even less so for those from immigrant backgrounds: for undocumented youths, their hopes for the future coexist with permanent fear of possible deportation. This is a window inside the hearts and minds of these young dreamers, and the undocumented.',
    'votes': 2
}, {
    'cineteca_title': 'De uskyldige',
    'cineteca_director': 'Eskil Vogt',
    'cineteca_year': 2021,
    'cineteca_showtime': '2023-06-11 16:00',
    'result_title': 'The Innocents',
    'release_date': '2021-09-03',
    'rating': 7.005,
    'popularity': 19.76,
    'overview':
    'Four children become friends during the summer holidays, and out of sight of the adults they discover they have hidden powers. While exploring their newfound abilities in the nearby forests and playgrounds, their innocent play takes a dark turn and strange things begin to happen.',
    'votes': 390
}, {
    'cineteca_title': 'La nuit du 12',
    'cineteca_director': 'Dominik Moll',
    'cineteca_year': 2022,
    'cineteca_showtime': '2023-06-11 20:30',
    'result_title': 'The Night of the 12th',
    'release_date': '2022-07-13',
    'rating': 7.081,
    'popularity': 11.128,
    'overview':
    "Young and ambitious Captain Vivés has just been appointed group leader at the Grenoble Criminal Squad when Clara's murder case lands on his desk. Vivés and his team investigate Clara's complex life and relations, but what starts as a professional and methodical immersion into the victim's life soon turns into a haunting obsession.",
    'votes': 382
}, {
    'cineteca_title': 'Chhello Show (Last Film Show)',
    'cineteca_director': 'Pan Nalin',
    'cineteca_year': 2021,
    'cineteca_showtime': '2023-06-11 17:30',
    'result_title': 'Last Film Show',
    'release_date': '2022-01-06',
    'rating': 7.25,
    'popularity': 9.415,
    'overview':
    'A 9-year-old boy in a remote village in India begins a lifelong love affair with cinema when he bribes his way into a rundown movie palace and spends a summer watching movies from the projection booth.',
    'votes': 16
}, {
    'cineteca_title': 'Laila in Haifa',
    'cineteca_director': 'Amos Gitai',
    'cineteca_year': 2020,
    'cineteca_showtime': '2023-06-11 20:00',
    'result_title': 'Laila in Haifa',
    'release_date': '2021-09-01',
    'rating': 4.5,
    'popularity': 0.745,
    'overview':
    'The film was shot entirely in a nightclub, with an adjoining contemporary art gallery, whose customers are both Israelis and Palestinians, in one of Israel’s most open cities, Haifa. A long night in a place where the most diverse people meet: Jews, Muslims, gays, heterosexuals, transvestites; and three women, who in that multifaceted microcosm, a gathering peaceful hideout, can find shelter from male bullying and arrogance.',
    'votes': 3
}, {
    'cineteca_title': 'The Warriors',
    'cineteca_director': 'Walter Hill',
    'cineteca_year': 1979,
    'cineteca_showtime': '2023-06-11 13:00',
    'result_title': 'The Warriors',
    'release_date': '1979-02-09',
    'rating': 7.679,
    'popularity': 19.749,
    'overview':
    "Prominent gang leader Cyrus calls a meeting of New York's gangs to set aside their turf wars and take over the city. At the meeting, a rival leader kills Cyrus, but a Coney Island gang called the Warriors is wrongly blamed for Cyrus' death. Before you know it, the cops and every gangbanger in town is hot on the Warriors' trail.",
    'votes': 1860
}, {
    'cineteca_title': 'Los plebes',
    'cineteca_director': 'Emmanuel Massú y Eduardo Giralt',
    'cineteca_year': 2021,
    'cineteca_showtime': '2023-06-11 14:00',
    'result_title': 'Los plebes',
    'release_date': '2021-03-21',
    'rating': 7.0,
    'popularity': 1.209,
    'overview':
    'A young group of millennial sicarios loiters around Sinaloa while trying to cope with growing up, their work and desires for the future.',
    'votes': 2
}, {
    'cineteca_title': 'Made in Bangladesh',
    'cineteca_director': 'Rubaiyat Hossain',
    'cineteca_year': 2019,
    'cineteca_showtime': '2023-06-11 15:15',
    'result_title': 'Made in Bangladesh',
    'release_date': '2019-11-28',
    'rating': 6.4,
    'popularity': 1.991,
    'overview':
    'Shimu, 23, works in a clothing factory in Dhaka, Bangladesh. Faced with difficult conditions at work, she decides to start a union with her co-workers. Despite threats from the management and disapproval of her husband, Shimu is determined to go on. Together the women must fight and find a way to register their union.',
    'votes': 12
}, {
    'cineteca_title': 'No son horas de olvidar',
    'cineteca_director': 'David Castañón Medina',
    'cineteca_year': 2020,
    'cineteca_showtime': '2023-06-11 16:15',
    'result_title': 'No Son Horas de Olvidar',
    'release_date': '2020-10-30',
    'rating': 0.0,
    'popularity': 0.6,
    'overview':
    "Juana, Laura, Fahriye and Carlos use occupational therapy to elaborate fictional reconstructions of episodes of their lives in order to fight against their Alzheimer's disease.",
    'votes': 0
}, {
    'cineteca_title': 'Nómadas',
    'cineteca_director': 'Emiliano Ruprah',
    'cineteca_year': 2019
}, {
    'cineteca_title': 'Un monde',
    'cineteca_director': 'Laura Wandel',
    'cineteca_year': 2020,
    'cineteca_showtime': '2023-06-11 15:45',
    'result_title': 'A Bigger World',
    'release_date': '2019-10-30',
    'rating': 6.5,
    'popularity': 3.43,
    'overview':
    'In an attempt to move on from the death of Paul, the love of her life, Korine leaves Paris to undertake a project in Mongolia. But after meeting the shaman, Oyun, her trip takes a different direction. Korine has a rare gift that Oyun intends to unveil. She agrees to initiate herself in the practice of Shamanism, leading her to discover an ancient and forgotten culture, but most importantly herself.',
    'votes': 52
}, {
    'cineteca_title': 'Sanguinetti',
    'cineteca_director': 'Christian Díaz Pardo',
    'cineteca_year': 2019
}, {
    'cineteca_title': 'Firebird',
    'cineteca_director': 'Peeter Reban',
    'cineteca_year': 2021,
    'cineteca_showtime': '2023-06-11 14:00',
    'result_title': 'Firebird',
    'release_date': '2021-11-25',
    'rating': 7.0,
    'popularity': 11.63,
    'overview':
    'At the height of the Cold War, a troubled soldier forms a forbidden love triangle with a daring fighter pilot and his female comrade amid the dangerous surroundings of a Soviet Air Force Base.',
    'votes': 63
}, {
    'cineteca_title': 'Sundown',
    'cineteca_director': 'Michel Franco',
    'cineteca_year': 2022,
    'cineteca_showtime': '2023-06-11 14:15',
    'result_title': 'Sundown',
    'release_date': '2022-04-08',
    'rating': 6.327,
    'popularity': 7.48,
    'overview':
    'When a distant emergency disrupts a vacation in Acapulco, simmering tensions rise to the fore between scions of a wealthy British family.',
    'votes': 78
}, {
    'cineteca_title': 'Trigal',
    'cineteca_director': 'Anabel Caso',
    'cineteca_year': 2022,
    'cineteca_showtime': '2023-06-11 14:15',
    'result_title': 'Wheatfield',
    'release_date': '2022-10-25',
    'rating': 4.667,
    'popularity': 0.608,
    'overview':
    'During the summer, thirteen-year-old Sofia moves to the country house, where her cousin Cristina is waiting for her to spend the vacations. During these days of games and discoveries, the two will be immersed in a love triangle with a man almost twenty years older. Its outcome will mark the passage from puberty to adolescence for both of them.',
    'votes': 3
}, {
    'cineteca_title': 'Feature Film About Life',
    'cineteca_director': 'Dovile Sarutyte',
    'cineteca_year': 2021,
    'cineteca_showtime': '2023-06-11 16:45',
    'result_title': 'Feature Film About Life',
    'release_date': '2021-11-24',
    'rating': 8.0,
    'popularity': 1.04,
    'overview':
    'It is highly probable that before their own death, everyone has to organise someone else’s funeral. This is by far not an easy task. In addition to the searing grief, dying also brings a number of tasks that are at once utterly alien and intensely time-critical. The main character of this film, Dovile, who unexpectedly has to bury her father, has to face the bedlam of exactly such a challenge. Overnight, the young girl has to become a skilful organiser of a family event, while also being a specialist on coffins, urns, wreaths and funeral feasts. Dovile’s journey towards organising a perfect funeral is inevitably full of hardship and mishaps, accompanied mainly by black humour and comical situations.',
    'votes': 3
}, {
    'cineteca_title': 'Volverte a ver',
    'cineteca_director': 'Carolina Corral Paredes',
    'cineteca_year': 2020,
    'cineteca_showtime': '2023-06-11 20:15',
    'result_title': 'To See You Again',
    'release_date': '2020-06-10',
    'rating': 0.0,
    'popularity': 0.6,
    'overview':
    'In 2016 the Mexican District Attorney secretly buried more than 100 murdered bodies during the war against drug trafficking. They kept it hidden until a group of women, mothers, discovered it while searching for their missing children. One of them retrieves the body of her brother. "To See You Again" narrates the participation of Mexican women as they exhume what remains of the corpses and learn about forensic work. They help us discover the crimes committed by the state when burying the bodies.',
    'votes': 0
}, {
    'cineteca_title': 'Remedios Varo. Misterio y revelación',
    'cineteca_director': 'Tufic Makhlouf Akl',
    'cineteca_year': 2013,
    'cineteca_showtime': '2023-06-11 18:30',
    'result_title': 'Remedios Varo: Mystery and Revelation',
    'release_date': '2013-01-01',
    'rating': 9.0,
    'popularity': 0.6,
    'overview':
    'The magical world of Remedios Varo, a singular and unclassifiable artist, that André Breton claimed as a surréaliste. Born in Anglès, Spain, in 1908, Remedios was marked by two wars (Spanish Civil War and the Second World War) and for an intense relationship of amour fou with the poet Benjamin Péret who considered her his muse and the woman of his dreams. Exiled in Mexico from 1941 until her death in 1963, she developed in this country the pictorial imagery and the technical virtuoso which identify her as a weaver of dreams in a world of medieval reminiscences, populated by creatures and fantastic objects connected with the cosmos.',
    'votes': 1
}, {
    'cineteca_title': 'Suzume no tojimari',
    'cineteca_director': 'Makoto Shinkai',
    'cineteca_year': 2022,
    'cineteca_showtime': '2023-06-11 12:30',
    'result_title': 'Suzume',
    'release_date': '2022-11-11',
    'rating': 7.887,
    'popularity': 412.029,
    'overview':
    'Suzume, 17, lost her mother as a little girl. On her way to school, she meets a mysterious young man. But her curiosity unleashes a calamity that endangers the entire population of Japan, and so Suzume embarks on a journey to set things right.',
    'votes': 428
}, {
    'cineteca_title': 'Raising Arizona',
    'cineteca_director': 'Joel Coen',
    'cineteca_year': 1987,
    'cineteca_showtime': '2023-06-11 18:00',
    'result_title': 'Raising Arizona',
    'release_date': '1987-03-01',
    'rating': 7.035,
    'popularity': 11.139,
    'overview':
    "When a childless couple of an ex-con and an ex-cop decide to help themselves to one of another family's quintuplets, their lives become more complicated than they anticipated.",
    'votes': 1798
}, {
    'cineteca_title': 'Historia de mi muerte',
    'cineteca_director': 'Albert Serra',
    'cineteca_year': 2013,
    'cineteca_showtime': '2023-06-11 17:30',
    'result_title': 'Story of My Death',
    'release_date': '2013-10-23',
    'rating': 7.1,
    'popularity': 0.907,
    'overview':
    'Casanova meets a new servant who will witness his last moments in life, from a castle with its libertine 18th century atmosphere to the poor, shadowy Northern lands. There, his rationalist way of thinking and mundane world will succumb to a violent and romantic force, represented by Count Dracula.',
    'votes': 21
}, {
    'cineteca_title': 'India Song',
    'cineteca_director': 'Marguerite Duras',
    'cineteca_year': 1975,
    'cineteca_showtime': '2023-06-11 21:00',
    'result_title': 'India Song',
    'release_date': '1975-06-04',
    'rating': 6.331,
    'popularity': 4.105,
    'overview':
    'India, 1937. Anne-Marie Stretter is the wife of the French ambassador and leads a solitary yet privileged life in Calcutta. The tedium of her existence is relieved by numerous illicit love affairs with government officials, young men who find her an object of desire and fascination. The Vice Consul is driven insane by his love for her and, expelled from the ambassador’s palace, cries like a sick animal. Life continues for Anne-Marie Stretter, the same tedious existence…',
    'votes': 62
}, {
    'cineteca_title': 'Onna bakari no yoru',
    'cineteca_director': 'Kinuyo Tanaka',
    'cineteca_year': 1961,
    'cineteca_showtime': '2023-06-11 20:30',
    'result_title': 'Girls of the Night',
    'release_date': '1961-09-04',
    'rating': 7.2,
    'popularity': 1.96,
    'overview':
    "In the late 1950's prostitution was banned in Japan and if a woman was found exercising this profession they were sent to a reformatory. This is a story of one of these brave women Kuniko who is released from the reformatory and tries to build a new life.",
    'votes': 8
}]


def main_test_function():
    #print(prepare_text(info_for_text_test))
    main()
    return


main_test_function()
