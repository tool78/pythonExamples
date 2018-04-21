from mystuff import MyStuff
from song import Song

# dict style
# mystuff['apples']

# module style
# mystuff.apples()
# print mystuff.tangerine

# class style
thing = MyStuff()
thing.apples()
print thing.tangerine

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
