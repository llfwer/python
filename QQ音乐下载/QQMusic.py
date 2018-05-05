# coding=utf-8
import base64
import json
import os
from random import random
from time import time

import requests


class Song(object):
    # 这个是九位的随机数，没有什么特殊意义，用其他方法生成也一样
    guid = int(random() * 2147483647) * int(time() * 1000) % 10000000000
    headers = {
        "cookie": 'pgv_pvi=6725760000; pgv_si=s4324782080; pgv_pvid=%s; qqmusic_fromtag=66' % guid,
    }

    def __init__(self, media_mid, song_mid, title, singer=[], album={}, data={}):
        self.filename = "C400%s.m4a" % media_mid
        self.song_mid = song_mid
        self.title = title
        self.vkey = ""
        self.music_url = ""
        self.singer = singer
        self.album = album
        self.data = data
        self.save_title = ''.join(
            map(lambda x: '_' if x in '?*/\\<>:"|' else x, title))
        if data['action']['msg'] != 3:
            self.status = 0
        else:
            self.status = 1

    def _get_vkey(self):
        ''' 获取指定歌曲的vkey值 '''
        url = 'https://c.y.qq.com/base/fcgi-bin/fcg_music_express_mobile3.fcg?'
        url += 'format=json&platform=yqq&cid=205361747&songmid=%s&filename=%s&guid=%s' \
               % (self.song_mid, self.filename, self.guid)
        rst = requests.get(url)
        self.vkey = json.loads(rst.text)['data']['items'][0]['vkey']
        return self.vkey

    def get_music_url(self):
        ''' 获取指定歌曲的播放地址 '''
        try:
            self._get_vkey()
        except json.decoder.JSONDecodeError:
            self._get_vkey()
        url = 'http://dl.stream.qqmusic.qq.com/%s?' % self.filename
        self.music_url = url + \
                         'vkey=%s&guid=%s&fromtag=30' % (self.vkey, self.guid)
        return self.music_url

    def save(self, path=os.path.join(os.path.abspath('./'), 'song')):
        ''' 将此歌曲保存至本地 '''
        print('download:', self.title, end=' ------ ')
        if not os.path.exists(path):
            print('目录', path, '不存在')
            return False

        self.get_music_url()

        media_data = requests.get(self.music_url, headers=self.headers)
        if media_data.status_code != 200:
            print('歌曲或网络错误')
            return False
        with open(os.path.join(path, self.save_title + '.m4a'), 'wb') as fr:
            fr.write(media_data.content)
        print('歌曲下载完成')
        return True

    def lrc_save(self, path=os.path.join(os.path.abspath('./'), 'song')):
        ''' 保存歌词 '''
        print('download lrc:', self.title, end=' ------ ')
        headers = {
            "Referer": "https://y.qq.com/portal/player.html",
            "Cookie": "skey=@LVJPZmJUX; p",
        }
        lrc_data = requests.get(
            'https://c.y.qq.com/lyric/fcgi-bin/fcg_query_lyric_new.fcg?g_tk=753738303&songmid=' + self.song_mid,
            headers=headers)
        if lrc_data.status_code != 200:
            print('歌词不存在或网络错误')
            return False

        lrc_dict = json.loads(lrc_data.text[18:-1])
        lrc_data = base64.b64decode(lrc_dict['lyric'])
        with open(os.path.join(path, self.save_title + '.lrc'), 'w') as fr:
            try:
                fr.write(lrc_data)
            except TypeError:
                fr.write(bytes.decode(lrc_data))

        # 若有翻译歌词
        if lrc_dict.get('trans'):
            lrc_data = base64.b64decode(lrc_dict['trans'])
            with open(os.path.join(path, self.save_title + '-trans.lrc'), 'w') as fr:
                try:
                    fr.write(lrc_data)
                except TypeError:
                    fr.write(bytes.decode(lrc_data))
        print('歌词下载完成')
        return True

    def __str__(self):
        try:
            return '{}{} - {}  < {} >'.format('<失效> ' if self.status else '', self.title,
                                              ' / '.join(map(lambda x: x['name'], self.singer)), self.album['name'])
        except UnicodeEncodeError:
            return '{}{} - {}  < {} >'.format('<失效> ' if self.status else '', self.title.encode('utf-8'),
                                              ' / '.join(map(lambda x: x['name'].encode('utf-8'), self.singer)),
                                              self.album['name'].encode('utf-8'))


class SongList(object):
    """ 歌曲列表 """

    def __init__(self, song_list=[]):
        self.song_list = song_list
        self.current = 0

    def add(self, song):
        assert isinstance(song, Song)
        self.song_list.append(song)

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.song_list) <= self.current:
            raise StopIteration
        value = self.song_list[self.current]
        self.current += 1
        return value

    def __getitem__(self, index):
        return self.song_list[index]

    def __str__(self):
        string = []
        index = 0
        for i in self.song_list:
            string.append('{}. {}'.format(index, i))
            index += 1
        return '\n'.join(string)

    def save(self, path=os.path.join(os.path.abspath('./'), 'song')):
        for song in self.song_list:
            song.save(path=path)

    def lrc_save(self, path=os.path.join(os.path.abspath('./'), 'song')):
        for song in self.song_list:
            song.lrc_save(path=path)


class QQMusic(object):
    def search_song(self, key_word, page=1, num=20):
        ''' 根据关键词查找歌曲 '''
        url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp'
        url += '?new_json=1&aggr=1&cr=1&flag_qc=0&p=%d&n=%d&w=%s' \
               % (page, num, key_word)
        rst = requests.get(url)
        data_list = json.loads(rst.text[9:-1])['data']['song']['list']
        song_list = []
        for line in data_list:
            media_mid = line['file']['media_mid']
            song_mid = line['mid']
            title = line['title']
            singer = line['singer']
            album = line['album']
            song = Song(media_mid=media_mid, song_mid=song_mid,
                        title=title, singer=singer, album=album, data=line)
            song_list.append(song)
        return SongList(song_list)


if __name__ == '__main__':
    qqmusic = QQMusic()
    key_word = input('key_word: ')
    song_list = qqmusic.search_song(key_word)
    print(song_list)
    # song_list.add(song_list[0])
    # print(song_list)
    # song_list.save()
    # song_list[0].save()
    # song_list[0].lrc_save()
