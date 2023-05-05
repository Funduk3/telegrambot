from data import db_session
from data import anime, films, series


def main():
    db_session.global_init("db/database.db")
    films_genres = ['thrillers', 'action', 'drama', 'western', 'criminal', 'detectives', 'horrors', 'science_fiction',
                    'fantasy', 'historical', 'adventures']
    films_titles = [['The Silence of the Lambs', 'Gisaengchung', "Psycho", "Shutter Island", "Seven", "Chinatown",
                     "Zodiac", "The Devil's Advocate", "The Sixth Sense", "North by Northwest", "Reservoir Dogs"],
                    ['Leon', 'Lock, Stock and Two Smoking Barrels', 'Wrath of Man', 'Kill Bill: Vol. 1',
                     'The Terminator',
                     'Enter the Dragon', 'The Dark Knight', 'Face/Off', 'John Wick', 'Casino Royale',
                     'The Bourne Identity'],
                    ['The Shawshank Redemption', 'The Green Mile', 'Time Framed', 'Forrest Gump', "Schindler's List",
                     '1+1', 'The Wolf of Wall Street', 'The Truman Show', 'Joker', 'Once Upon a Time in... Hollywood',
                     'The Great Gatsby'],
                    ['Django Unchained', 'Il buono, il brutto, il cattivo', 'The Hateful Eight', 'Unforgiven',
                     "C'era una volta il West", '3:10 to Yuma', 'Per qualche dollaro in più', 'The Searchers',
                     'Rio Bravo', 'Butch Cassidy and the Sundance Kid'],
                    ['The Godfather', 'Pulp Fiction', 'The Gentlemen', 'Snatch', 'Catch Me If You Can',
                     "Reservoir Dogs",
                     "Ocean's Eleven", "From Dusk Till Dawn", "Scarface", "American Psycho"],
                    ["Sherlock Holmes", "Murder on the Orient Express", "Knives Out", "Primal Fear", "Dirty Harry",
                     "In the Heat of the Night", "Vertigo", "Memento", "Mulholland Dr.", "Salinui chueok"],
                    ['Alien', 'Aliens', 'The Thing', 'Saw', 'Dracula', 'Misery', 'The Exorcist',
                     'A Nightmare on Elm Street',
                     "Rosemary's Baby", 'The Omen'],
                    ['Inception', 'Back to the Future', 'Interstellar', 'The Dark Knight', 'The Matrix',
                     'The Fifth Element', 'Avengers: Infinity War', 'Avatar', 'Iron Man', 'The Avengers'],
                    ['Pirates of the Caribbean', 'The Lord of the Rings', 'Harry Potter', 'Groundgoh Day',
                     'The Hobbit',
                     'Constantine', 'Bruce Almighty', 'Chen qing ling', 'Dokkaebi', "A Dog's Purpose"],
                    ['Ki Hwanghu', 'Gladiator', 'Braveheart', 'Invictus', 'Geomgaek', 'The Last Duel',
                     'Babylon', 'The Last Kingdom: Seven Kings Must Die'],
                    ['Pirates of the Caribbean', 'The Revenant', 'Jurassic Park', 'The Physician',
                     'Indian Jones', 'Everest', 'Ostwind', 'Spider-Man', 'Cast Away']
                    ]

    series_titles = [['Hannibal', 'Dexter', 'Dark', 'Lie to Me', 'Twin Peaks', 'Fargo', 'Bridge',
                      'Chernobyl: Exclusion Zone', 'Method', 'Mr. Robot'],
                     ['Prison Break', 'La casa de papel', 'Wayne', 'The Boys', 'Daredevil', 'Peacemaker',
                      'The Mandalorian',
                      'Arrow', 'Warrior', 'Strike Back', 'Person of Interest'],
                     ["House, M.D", "Shameless", "Trigger", "Peaky Blinders", "Zero patient", "Why Women Kill",
                      "The Queen's Gambit", "The Good Doctor", "Euphoria", "Desperate Housewives"],
                     ['Yellowstone', "1923", "1883", "Deadwood", "Longmire", "Godless", "Hell on Wheels",
                      "Wild Wild West",
                      'Lonesome Dove', 'The English'],
                     ["Breaking Bad", "Blue Lights", "Better Call Saul", "The Sopranos", "Poker Face", "True Detective",
                      'Luther', 'Mayor of Kingstown', 'The Wire', "Tulsa King"],
                     ['Sherlock', 'Broadchurch', 'Big Little Lies', 'How to Get Away with Murder', 'liquidation',
                      "Miss Fisher's Murder Mysteries", "The Blacklist", "Midsomer Murders", "Mindhunter",
                      "Blue Bloods"],
                     ['The Walking Dead', 'Stranger Things', 'American Horror Story', 'Ash vs Evil Dead',
                      'Tales from the Crypt', 'From', 'Preacher', 'Penny Dreadful'],
                     ['Doctor Who', 'Black Mirror', 'The Boys', 'Forever', 'The X Files', 'Lost', 'Resident Alien',
                      'Misfits', 'The Mandalorian', 'The Last of Us', 'Peacemaker'],
                     ['Game of Thrones', 'Dokkaebi', 'The 10th Kingdom', 'Supernatural', 'House of the Dragon',
                      'Merlin',
                      'Wednesday', 'The Originals', 'Teen Wolf', 'Grimm', 'The Witcher'],
                     ['Ki Hwanghu', 'Rurikovich. History of the First Dynasty', 'Vikings', 'Band of Brothers',
                      'Boardwalk Empire', 'Spartacus', 'Peaky Blinders', 'Marco Polo'],
                     ['Lupin', 'The Witcher', 'Sweet Tooth', 'Black Sails', 'Marco Polo', 'His Dark Materials',
                      'Mandalorian', 'Firefly', 'The Musketeers']]

    db_sess = db_session.create_session()
    for i in range(len(films_genres)):
        f = films.Films()
        f.genre = films_genres[i]
        f.titles = '; '.join(films_titles[i])
        db_sess.add(f)

        s = series.Series()
        s.genre = films_genres[i]
        s.titles = '; '.join(series_titles[i])
        db_sess.add(s)
        db_sess.commit()

    anime_genres = ['senens_heroic', 'senens_schools', 'senens_severe_world', 'senens_new', 'senens_well_known',
                    'senens_fights', 'comedy', 'cyberpunk', 'fur', 'sport', 'dark', 'ranobe', 'fantasy', 'dark_fantasy']

    anime_titles = [['My Hero Academia', 'One Punch Man', 'Mob Psycho 100'],
                    ['Assassination Classroom', 'Great Teacher Onizuka',
                     'Classroom of the Elite', 'Danganronpa: The Animation'],
                    ['Attack on Titan', 'Vinland Saga', 'Berserk', 'Claymore', 'Akame ga Kill!'],
                    ['Demon Slayer', 'Jujutsu Kaisen', 'Dororo', 'To Your Eternity', 'Chainsaw Man'],
                    ['One Piece', 'Naruto', 'Dragon Ball Z', 'Hunter x Hunter', 'Fullmetal Alchemist',
                     "JoJo's Bizarre Adventure", 'Tower of God', 'Bleach'],
                    ['Tokyo Revengers', 'Steins;Gate', 'ERASED', 'Re:ZERO -Starting Life in Another World-'],
                    ['Spy x Family', 'Hinamatsuri', 'Kakushigoto', 'Barakamon'],
                    ['Psycho-Pass', 'Terror in Resonance', 'ID: INVADED', 'Ghost in the Shell: Stand Alone Complex',
                     'Cyberpunk 2077'], ['Neon Genesis Evangelion', 'DARLING in the FRANXX', 'Bokurano', 'Heroic Age'],
                    ['Slam Dunk', 'Haikyu!!', 'Blue Lock', "Kuroko's Basketball", 'Yuri!!! On ICE'],
                    ['Hellsing', 'D.Gray-man', 'Gungrave', 'Chrono Crusade', 'Death Note'],
                    ['No Game, No Life', 'Kakegurui', 'GATE', 'Amagi Brilliant Park'],
                    ['The Seven Deadly Sins', 'Fairy Tail', 'Black Clover', 'Magi: The Labyrinth of Magic',
                     'Plunderer', 'Edens Zero'],
                    ['Tokyo Ghoul', 'Seraph of the End: Vampire Reign', 'Parasyte: The Maxim']
                    ]

    for i in range(len(anime_genres)):
        a = anime.Anime()
        a.genre = anime_genres[i]
        a.titles = '; '.join(anime_titles[i])
        db_sess.add(a)
        db_sess.commit()


if __name__ == '__main__':
    main()
