from telegram.ext import Application, MessageHandler, filters, CommandHandler, ConversationHandler
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove

BOT_TOKEN = '5576564316:AAHznAm5Mng5WCsDFXwjK7fE7BSOZtLntfI'


class FilmsBase:
    thrillers = [['The Silence of the Lambs', 'Gisaengchung', "Psycho", "Shutter Island", "Seven", "Chinatown",
                  "Zodiac", "The Devil's Advocate", "The Sixth Sense", "North by Northwest", "Reservoir Dogs"]]

    action = [['Leon', 'Lock, Stock and Two Smoking Barrels', 'Wrath of Man', 'Kill Bill: Vol. 1', 'The Terminator',
               'Enter the Dragon', 'The Dark Knight', 'Face/Off', 'John Wick', 'Casino Royale', 'The Bourne Identity']]

    drama = [['The Shawshank Redemption', 'The Green Mile', 'Time Framed', 'Forrest Gump', "Schindler's List",
              '1+1', 'The Wolf of Wall Street', 'The Truman Show', 'Joker', 'Once Upon a Time in... Hollywood',
              'The Great Gatsby']]

    western = [['Django Unchained', 'Il buono, il brutto, il cattivo', 'The Hateful Eight', 'Unforgiven',
                "C'era una volta il West", '3:10 to Yuma', 'Per qualche dollaro in più', 'The Searchers',
                'Rio Bravo', 'Butch Cassidy and the Sundance Kid']]

    criminal = [['The Godfather', 'Pulp Fiction', 'The Gentlemen', 'Snatch', 'Catch Me If You Can', "Reservoir Dogs",
                 "Ocean's Eleven", "From Dusk Till Dawn", "Scarface", "American Psycho"]]

    detectives = [["Sherlock Holmes", "Murder on the Orient Express", "Knives Out", "Primal Fear", "Dirty Harry",
                   "In the Heat of the Night", "Vertigo", "Memento", "Mulholland Dr.", "Salinui chueok"]]

    horrors = [['Alien', 'Aliens', 'The Thing', 'Saw', 'Dracula', 'Misery', 'The Exorcist', 'A Nightmare on Elm Street',
                "Rosemary's Baby", 'The Omen']]

    science_fiction = [['Inception', 'Back to the Future', 'Interstellar', 'The Dark Knight', 'The Matrix',
                        'The Fifth Element', 'Avengers: Infinity War', 'Avatar', 'Iron Man', 'The Avengers']]

    fantasy = [['Pirates of the Caribbean', 'The Lord of the Rings', 'Harry Potter', 'Groundgoh Day', 'The Hobbit',
                'Constantine', 'Bruce Almighty', 'Chen qing ling', 'Dokkaebi', "A Dog's Purpose"]]

    historical = [['Ki Hwanghu', 'Gladiator', 'Braveheart', 'Invictus', 'Geomgaek', 'The Last Duel',
                   'Babylon', 'The Last Kingdom: Seven Kings Must Die']]

    adventures = [['Pirates of the Caribbean', 'The Revenant', 'Jurassic Park', 'The Physician',
                   'Indian Jones', 'Everest', 'Ostwind', 'Spider-Man', 'Cast Away']]

    films = [thrillers, action, drama, western, criminal, detectives, horrors, science_fiction, fantasy, historical,
             adventures]


class SeriesBase:
    thrillers = [['Hannibal', 'Dexter', 'Dark', 'Lie to Me', 'Twin Peaks', 'Fargo', 'Bridge',
                  'Chernobyl: Exclusion Zone', 'Method', 'Mr. Robot']]

    action = [['Prison Break', 'La casa de papel', 'Wayne', 'The Boys', 'Daredevil', 'Peacemaker', 'The Mandalorian',
               'Arrow', 'Warrior', 'Strike Back', 'Person of Interest']]

    drama = [["House, M.D", "Shameless", "Trigger", "Peaky Blinders", "Zero patient", "Why Women Kill",
              "The Queen's Gambit", "The Good Doctor", "Euphoria", "Desperate Housewives"]]

    western = [['Yellowstone', "1923", "1883", "Deadwood", "Longmire", "Godless", "Hell on Wheels", "Wild Wild West",
                'Lonesome Dove', 'The English']]

    criminal = [["Breaking Bad", "Blue Lights", "Better Call Saul", "The Sopranos", "Poker Face", "True Detective",
                 'Luther', 'Mayor of Kingstown', 'The Wire', "Tulsa King"]]

    detectives = [['Sherlock', 'Broadchurch', 'Big Little Lies', 'How to Get Away with Murder', 'liquidation',
                   "Miss Fisher's Murder Mysteries", "The Blacklist", "Midsomer Murders", "Mindhunter", "Blue Bloods"]]

    horrors = [['The Walking Dead', 'Stranger Things', 'American Horror Story', 'Ash vs Evil Dead',
                'Tales from the Crypt', 'From', 'Preacher', 'Penny Dreadful']]

    science_fiction = [['Doctor Who', 'Black Mirror', 'The Boys', 'Forever', 'The X Files', 'Lost', 'Resident Alien',
                        'Misfits', 'The Mandalorian', 'The Last of Us', 'Peacemaker']]

    fantasy = [['Game of Thrones', 'Dokkaebi', 'The 10th Kingdom', 'Supernatural', 'House of the Dragon', 'Merlin',
                'Wednesday', 'The Originals', 'Teen Wolf', 'Grimm', 'The Witcher']]

    historical = [['Ki Hwanghu', 'Rurikovich. History of the First Dynasty', 'Vikings', 'Band of Brothers',
                   'Boardwalk Empire', 'Spartacus', 'Peaky Blinders', 'Marco Polo']]

    adventures = [['Lupin', 'The Witcher', 'Sweet Tooth', 'Black Sails', 'Marco Polo', 'His Dark Materials',
                   'Mandalorian', 'Firefly', 'The Musketeers']]

    series = [thrillers, action, drama, western, criminal, detectives, horrors, science_fiction, fantasy, historical,
              adventures]


class AnimeBase:
    senens = [['My Hero Academia', 'One Punch Man', 'Mob Psycho 100'],
              ['Assassination Classroom', 'Great Teacher Onizuka',
               'Classroom of the Elite', 'Danganronpa: The Animation'],
              ['Attack on Titan', 'Vinland Saga', 'Berserk', 'Claymore', 'Akame ga Kill!'],
              ['Demon Slayer', 'Jujutsu Kaisen', 'Dororo', 'To Your Eternity', 'Chainsaw Man'],
              ['One Piece', 'Naruto', 'Dragon Ball Z', 'Hunter x Hunter', 'Fullmetal Alchemist',
               "JoJo's Bizarre Adventure", 'Tower of God', 'Bleach'],
              ['Tokyo Revengers', 'Steins;Gate', 'ERASED', 'Re:ZERO -Starting Life in Another World-']],
    comedy = [['Spy x Family', 'Hinamatsuri', 'Kakushigoto', 'Barakamon']]
    cyberpunk = [
        ['Psycho-Pass', 'Terror in Resonance', 'ID: INVADED', 'Ghost in the Shell: Stand Alone Complex',
         'Cyberpunk 2077']]
    fur = [['Neon Genesis Evangelion', 'DARLING in the FRANXX', 'Bokurano', 'Heroic Age']]
    sport = [['Slam Dunk', 'Haikyu!!', 'Blue Lock', "Kuroko's Basketball", 'Yuri!!! On ICE']]
    dark = [['Hellsing', 'D.Gray-man', 'Gungrave', 'Chrono Crusade', 'Death Note']]
    ranobe = [['No Game, No Life', 'Kakegurui', 'GATE', 'Amagi Brilliant Park']]
    fantasy = [['The Seven Deadly Sins', 'Fairy Tail', 'Black Clover', 'Magi: The Labyrinth of Magic',
                'Plunderer', 'Edens Zero']]
    dark_fantasy = [['Tokyo Ghoul', 'Seraph of the End: Vampire Reign', 'Parasyte: The Maxim']]

    anime = [senens, comedy, cyberpunk, fur, sport, dark, ranobe, fantasy, dark_fantasy]


async def help_command(update, context):
    await update.message.reply_text(f"This bot is able to offer similar works for your request. "
                                    f"To use the bot /start\n"
                                    f"P.S. this is the subjective opinion of the author or rating lists")


async def start_command(update, context):
    await update.message.reply_text(f"You can find the work you need by searching /name_find \n"
                                    f"Or look at similar creation by genre /genres_find")


# ----------------------------------------------------------------------------------------------------------------------


async def name_find_command(update, context):
    await update.message.reply_text(f"Enter the name of the movie, series or anime in English",
                                    reply_markup=ReplyKeyboardRemove())
    return 1


async def input_command(update, context):
    global answer_data
    income = update.message.text
    db = AnimeBase.anime + FilmsBase.films + SeriesBase.series
    output = []
    for genre in db:
        if genre != AnimeBase.senens:
            genre_name = genre[0]
            for name in genre_name:
                for el in name:
                    if income.lower() in el.lower():
                        output.append(el)
        else:
            for names in genre:
                for name in names:
                    for el in name:
                        if income.lower() in el.lower():
                            output.append(el)
    if not output:
        await update.message.reply_text(f"Sorry, nothing found\nTry another query /name_find")
    else:
        if len(output) >= 10:
            output = output[:10]
        answer_data = '\n'.join(output) + '\nWanna see resembling? If so, /resembling_find'
        await update.message.reply_text(answer_data)
    return ConversationHandler.END


async def resembling_find(update, context):
    db = AnimeBase.anime + FilmsBase.films + SeriesBase.series
    answer = []
    input_command_result = answer_data.split('\nWanna see resembling? If so, /resembling_find')[:-1]
    for elem in input_command_result:
        for genre in db:
            for names in genre:
                for name in names:
                    for el in name:
                        if elem.lower() in el.lower():
                            answer.append(name)

    answer = '\n'.join(answer[0])
    await update.message.reply_text(f"{answer}")


async def stop(update, context):
    await update.message.reply_text("Hope you found what you were looking for!")
    return ConversationHandler.END


# ---------------------------------------------------------------------------------------------

async def anime(update, context):
    await update.message.reply_text('Choose a genre and the bot will show popular titles', reply_markup=anime_markup)


async def films(update, context):
    await update.message.reply_text('Choose a genre and the bot will show high-rated films', reply_markup=films_markup)


async def series(update, context):
    await update.message.reply_text('Choose a genre and the bot will show high-rated series',
                                    reply_markup=series_markup)


async def genres_find_command(update, context):
    await update.message.reply_text(f"This is a genre search \nChoose what you wanna search",
                                    reply_markup=genres_find_markup)


# ----------------------------------------------------------------------------------------------

async def thrillers_films(update, context):
    db = FilmsBase
    lst = '\n'.join(db.thrillers[0])
    await update.message.reply_text(f"{lst}\nHope you found what you were looking for!",
                                    reply_markup=ReplyKeyboardRemove())


async def action_films(update, context):
    db = FilmsBase
    lst = '\n'.join(db.action[0])
    await update.message.reply_text(f"{lst}\nHope you found what you were looking for!",
                                    reply_markup=ReplyKeyboardRemove())


async def drama_films(update, context):
    db = FilmsBase
    lst = '\n'.join(db.drama[0])
    await update.message.reply_text(f"{lst}\nHope you found what you were looking for!",
                                    reply_markup=ReplyKeyboardRemove())


async def western_films(update, context):
    db = FilmsBase
    lst = '\n'.join(db.western[0])
    await update.message.reply_text(f"{lst}\nHope you found what you were looking for!",
                                    reply_markup=ReplyKeyboardRemove())


async def criminal_films(update, context):
    db = FilmsBase
    lst = '\n'.join(db.criminal[0])
    await update.message.reply_text(f"{lst}\nHope you found what you were looking for!",
                                    reply_markup=ReplyKeyboardRemove())


async def detectives_films(update, context):
    db = FilmsBase
    lst = '\n'.join(db.detectives[0])
    await update.message.reply_text(f"{lst}\nHope you found what you were looking for!",
                                    reply_markup=ReplyKeyboardRemove())


async def horror_films(update, context):
    db = FilmsBase
    lst = '\n'.join(db.horrors[0])
    await update.message.reply_text(f"{lst}\nHope you found what you were looking for!",
                                    reply_markup=ReplyKeyboardRemove())


async def science_fiction_films(update, context):
    db = FilmsBase
    lst = '\n'.join(db.science_fiction[0])
    await update.message.reply_text(f"{lst}\nHope you found what you were looking for!",
                                    reply_markup=ReplyKeyboardRemove())


async def fantasy_films(update, context):
    db = FilmsBase
    lst = '\n'.join(db.fantasy[0])
    await update.message.reply_text(f"{lst}\nHope you found what you were looking for!",
                                    reply_markup=ReplyKeyboardRemove())


async def historical_films(update, context):
    db = FilmsBase
    lst = '\n'.join(db.historical[0])
    await update.message.reply_text(f"{lst}\nHope you found what you were looking for!",
                                    reply_markup=ReplyKeyboardRemove())


async def adventures_films(update, context):
    db = FilmsBase
    lst = '\n'.join(db.adventures[0])
    await update.message.reply_text(f"{lst}\nHope you found what you were looking for!",
                                    reply_markup=ReplyKeyboardRemove())


# ----------------------------------------------------------------------------------------------

async def thrillers_series(update, context):
    db = SeriesBase
    lst = '\n'.join(db.thrillers[0])
    await update.message.reply_text(f"{lst}\nHope you found what you were looking for!",
                                    reply_markup=ReplyKeyboardRemove())


async def action_series(update, context):
    db = SeriesBase
    lst = '\n'.join(db.action[0])
    await update.message.reply_text(f"{lst}\nHope you found what you were looking for!",
                                    reply_markup=ReplyKeyboardRemove())


async def drama_series(update, context):
    db = SeriesBase
    lst = '\n'.join(db.drama[0])
    await update.message.reply_text(f"{lst}\nHope you found what you were looking for!",
                                    reply_markup=ReplyKeyboardRemove())


async def western_series(update, context):
    db = SeriesBase
    lst = '\n'.join(db.western[0])
    await update.message.reply_text(f"{lst}\nHope you found what you were looking for!",
                                    reply_markup=ReplyKeyboardRemove())


async def criminal_series(update, context):
    db = SeriesBase
    lst = '\n'.join(db.criminal[0])
    await update.message.reply_text(f"{lst}\nHope you found what you were looking for!",
                                    reply_markup=ReplyKeyboardRemove())


async def detectives_series(update, context):
    db = SeriesBase
    lst = '\n'.join(db.detectives[0])
    await update.message.reply_text(f"{lst}\nHope you found what you were looking for!",
                                    reply_markup=ReplyKeyboardRemove())


async def horror_series(update, context):
    db = SeriesBase
    lst = '\n'.join(db.horrors[0])
    await update.message.reply_text(f"{lst}\nHope you found what you were looking for!",
                                    reply_markup=ReplyKeyboardRemove())


async def science_fiction_series(update, context):
    db = SeriesBase
    lst = '\n'.join(db.science_fiction[0])
    await update.message.reply_text(f"{lst}\nHope you found what you were looking for!",
                                    reply_markup=ReplyKeyboardRemove())


async def fantasy_series(update, context):
    db = SeriesBase
    lst = '\n'.join(db.fantasy[0])
    await update.message.reply_text(f"{lst}\nHope you found what you were looking for!",
                                    reply_markup=ReplyKeyboardRemove())


async def historical_series(update, context):
    db = SeriesBase
    lst = '\n'.join(db.historical[0])
    await update.message.reply_text(f"{lst}\nHope you found what you were looking for!",
                                    reply_markup=ReplyKeyboardRemove())


async def adventures_series(update, context):
    db = SeriesBase
    lst = '\n'.join(db.adventures[0])
    await update.message.reply_text(f"{lst}\nHope you found what you were looking for!",
                                    reply_markup=ReplyKeyboardRemove())


# ---------------------------------------------------------------------------------------------

async def senens(update, context):
    await update.message.reply_text('There are a lot of shonen, so choose the most suitable piece from '
                                    'suggested list',
                                    reply_markup=senens_markup)


async def comedy(update, context):
    db = AnimeBase
    lst = '\n'.join(db.comedy[0])
    await update.message.reply_text(f"{lst}\nHope you found what you were looking for!",
                                    reply_markup=ReplyKeyboardRemove())


async def cyberpunk(update, context):
    db = AnimeBase
    lst = '\n'.join(db.cyberpunk[0])
    await update.message.reply_text(f"{lst}\nHope you found what you were looking for!",
                                    reply_markup=ReplyKeyboardRemove())


async def fur(update, context):
    db = AnimeBase
    lst = '\n'.join(db.fur[0])
    await update.message.reply_text(f"{lst}\nHope you found what you were looking for!",
                                    reply_markup=ReplyKeyboardRemove())


async def sport(update, context):
    db = AnimeBase
    lst = '\n'.join(db.sport[0])
    await update.message.reply_text(f"{lst}\nHope you found what you were looking for!",
                                    reply_markup=ReplyKeyboardRemove())


async def dark(update, context):
    db = AnimeBase
    lst = '\n'.join(db.dark[0])
    await update.message.reply_text(f"{lst}\nHope you found what you were looking for!",
                                    reply_markup=ReplyKeyboardRemove())


async def ranobe(update, context):
    db = AnimeBase
    lst = '\n'.join(db.ranobe[0])
    await update.message.reply_text(f"{lst}\nHope you found what you were looking for!",
                                    reply_markup=ReplyKeyboardRemove())


async def fantasy(update, context):
    db = AnimeBase
    lst = '\n'.join(db.fantasy[0])
    await update.message.reply_text(f"{lst}\nHope you found what you were looking for!",
                                    reply_markup=ReplyKeyboardRemove())


async def dark_fantasy(update, context):
    db = AnimeBase
    lst = '\n'.join(db.dark_fantasy[0])
    await update.message.reply_text(f"{lst}\nHope you found what you were looking for!",
                                    reply_markup=ReplyKeyboardRemove())


# ------------------------------------------------------------------------------------------------

async def heroic(update, context):
    db = AnimeBase
    lst = '\n'.join(db.senens[0])
    await update.message.reply_text(f"{lst}\nHope you found what you were looking for!",
                                    reply_markup=ReplyKeyboardRemove())


async def schools(update, context):
    db = AnimeBase
    lst = '\n'.join(db.senens[1])
    await update.message.reply_text(f"{lst}\nHope you found what you were looking for!",
                                    reply_markup=ReplyKeyboardRemove())


async def severe_world(update, context):
    db = AnimeBase
    lst = '\n'.join(db.senens[2])
    await update.message.reply_text(f"{lst}\nHope you found what you were looking for!",
                                    reply_markup=ReplyKeyboardRemove())


async def new(update, context):
    db = AnimeBase
    lst = '\n'.join(db.senens[3])
    await update.message.reply_text(f"{lst}\nHope you found what you were looking for!",
                                    reply_markup=ReplyKeyboardRemove())


async def well_known(update, context):
    db = AnimeBase
    lst = '\n'.join(db.senens[4])
    await update.message.reply_text(f"{lst}\nHope you found what you were looking for!",
                                    reply_markup=ReplyKeyboardRemove())


async def fights(update, context):
    db = AnimeBase
    lst = '\n'.join(db.senens[5])
    await update.message.reply_text(f"{lst}\nHope you found what you were looking for!",
                                    reply_markup=ReplyKeyboardRemove())


def main():
    global genres_find_markup, anime_markup, senens_markup, films_markup, series_markup
    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("start", start_command))

    application.add_handler(CommandHandler("genres_find", genres_find_command))

    application.add_handler(CommandHandler("anime", anime))
    application.add_handler(CommandHandler("films", films))
    application.add_handler(CommandHandler("series", series))
    genres_find_reply_keyboard = [['/anime', '/films', '/series']]
    genres_find_markup = ReplyKeyboardMarkup(genres_find_reply_keyboard, one_time_keyboard=False)

    application.add_handler(CommandHandler("thrillers_films", thrillers_films))
    application.add_handler(CommandHandler("action_films", action_films))
    application.add_handler(CommandHandler("drama_films", drama_films))
    application.add_handler(CommandHandler("western_films", western_films))
    application.add_handler(CommandHandler("criminal_films", criminal_films))
    application.add_handler(CommandHandler("detectives_films", detectives_films))
    application.add_handler(CommandHandler("horror_films", horror_films))
    application.add_handler(CommandHandler("science_fiction_films", science_fiction_films))
    application.add_handler(CommandHandler("fantasy_films", fantasy_films))
    application.add_handler(CommandHandler("historical_films", historical_films))
    application.add_handler(CommandHandler("adventures_films", adventures_films))
    films_reply_keyboard = [['/thrillers_films', '/action_films', '/drama_films', '/western_films'],
                            ['/criminal_films', '/detectives_films', '/horror_films', '/science_fiction_films'],
                            ['/fantasy_films', '/historical_films', '/adventures_films']]
    films_markup = ReplyKeyboardMarkup(films_reply_keyboard, one_time_keyboard=False)

    application.add_handler(CommandHandler("thrillers_series", thrillers_series))
    application.add_handler(CommandHandler("action_series", action_series))
    application.add_handler(CommandHandler("drama_series", drama_series))
    application.add_handler(CommandHandler("western_series", western_series))
    application.add_handler(CommandHandler("criminal_series", criminal_series))
    application.add_handler(CommandHandler("detectives_series", detectives_series))
    application.add_handler(CommandHandler("horror_series", horror_series))
    application.add_handler(CommandHandler("science_fiction_series", science_fiction_series))
    application.add_handler(CommandHandler("fantasy_series", fantasy_series))
    application.add_handler(CommandHandler("historical_series", historical_series))
    application.add_handler(CommandHandler("adventures_series", adventures_series))
    series_reply_keyboard = [['/thrillers_series', '/action_series', '/drama_series', '/western_series'],
                             ['/criminal_series', '/detectives_series', '/horror_series', '/science_fiction_series'],
                             ['/fantasy_series', '/historical_series', '/adventures_series']]
    series_markup = ReplyKeyboardMarkup(series_reply_keyboard, one_time_keyboard=False)

    application.add_handler(CommandHandler("senens", senens))
    application.add_handler(CommandHandler("comedy", comedy))
    application.add_handler(CommandHandler("cyberpunk", cyberpunk))
    application.add_handler(CommandHandler("fur", fur))
    application.add_handler(CommandHandler("sport", sport))
    application.add_handler(CommandHandler("dark", dark))
    application.add_handler(CommandHandler("ranobe", ranobe))
    application.add_handler(CommandHandler("fantasy", fantasy))
    application.add_handler(CommandHandler("dark_fantasy", dark_fantasy))
    anime_reply_keyboard = [['/senens', '/comedy', '/cyberpunk'],
                            ['/fur', '/sport', '/dark'],
                            ['/ranobe', '/fantasy', '/dark_fantasy']]
    anime_markup = ReplyKeyboardMarkup(anime_reply_keyboard, one_time_keyboard=False)

    application.add_handler(CommandHandler("heroes", heroic))
    application.add_handler(CommandHandler("schools", schools))
    application.add_handler(CommandHandler("severe_world", severe_world))
    application.add_handler(CommandHandler("new", new))
    application.add_handler(CommandHandler("well_known", well_known))
    application.add_handler(CommandHandler("fights", fights))
    senens_reply_keyboard = [['/heroes', '/schools', '/severe_world'],
                             ['/new', '/well_known', '/fights']]
    senens_markup = ReplyKeyboardMarkup(senens_reply_keyboard, one_time_keyboard=False)

    application.add_handler(CommandHandler("resembling_find", resembling_find))
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('name_find', name_find_command)],

        states={
            1: [MessageHandler(filters.TEXT & ~filters.COMMAND, input_command)]
        },

        fallbacks=[CommandHandler('stop', stop)]
    )

    application.add_handler(conv_handler)
    application.run_polling()


if __name__ == '__main__':
    main()
