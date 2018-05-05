from QQMusic import QQMusic

qq_music = QQMusic()
song_list = qq_music.search_song('最幸福的不过是想要的都能拥有')
print(song_list)
song_list.save()
