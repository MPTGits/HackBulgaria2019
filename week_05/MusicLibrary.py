class Song:
    def __init__(self,title,artist,album,length):
        self.title=title
        self.artist=artist
        self.album=album
        self._length=length

    def __str__(self):
        return self.artist+'-'+self.title+' from '+ self.album+'-'+self._length

    def __eq__(self,other):
        return str(self)==str(other)

    def __hash__(self):
        return hash(str(self))


    def length(self,seconds=False,minutes=False,hours=False):
        if not (seconds or minutes or hours):
            return len(str(self))
        filter_time=self._length.split(':')
        multiplier=1
        final_result=0
        starting_point=0
        if minutes==True:
            starting_point=1
        if hours==True:
            starting_point=2
        filter_time.reverse()
        for time in filter_time[starting_point::]:
            final_result+=multiplier*int(time)
            multiplier=multiplier*60
        return final_result

lp_song=Song('Numb','Linkin Park','LP','1:30:20')
lp_song2=Song('In the End','Linkin Park','LP','3:20')
skilet=Song('Monster','Skillet','SK','2:40')
# print(test1==test2)

from functools import reduce
import copy
import random 
import json

class Playlist:

    def __init__(self,name,repeat=False,shuffle=False):
        self.name=name
        self.repeat=repeat
        self.shuffle=shuffle
        self.playlist=[]
        self.idx=0

    def __iter__(self):
       return self

    def __next__(self):
        self.idx += 1
        try:
            if self.idx==len(self.playlist) and self.repeat:
                self.idx=0
            if self.shuffle:
                return self.playlist[random.randint(0, len(self.playlist)-1)]
            return self.playlist[self.idx-1]
        except IndexError:
            self.idx=0
            raise StopIteration

    def pprint(self):
        str_playlist=''
        str_playlist+='-'*55+'\n'
        str_playlist+='|Artist'+' '*12+'|Song'+' '*14+ '| Length'+' '*8+'|'+'\n'
        str_playlist+='-'*55+'\n'
        for song in self.playlist:
            str_playlist+='|'+song.artist[:14:] +'...'+' '*4+'|'+song.  title[:14:]+'...' +' '*10+ '|'+song._length+'|'+'\n'
        return str_playlist

    def add_song(self,song):
        if isinstance(song,Song):
            if song not in self.playlist:
                self.playlist.append(song)

    def remove_song(self,song):
        if isinstance(song,Song):
            if song in self.playlist:
                self.playlist.remove(song)
    
    def total_length(self):
        lenght_of_all_songs=reduce(lambda x,y:x.length(False,True)+y.length(False,True),self.playlist)
        return 'Your playlist is '+str(lenght_of_all_songs)+' minutes long!'

    def artists(self):
        artists_songs={}
        temp_playlist=copy.deepcopy(self.playlist)
        for song in temp_playlist:
            current_artist=song.artist
            for song in temp_playlist:
                if song.artist==current_artist:
                    artists_songs[current_artist]=artists_songs.get(current_artist,0)+1
            temp_playlist=list(filter(lambda x:x.artist!=current_artist,temp_playlist))
        return artists_songs

    def next_song(self):
        return next(self)


    def save(self):
        json_string_playlist = json.dumps(str(self.__dict__))
        name=self.name.split()
        playlist_name=[letter.replace(' ', '_') for letter in name]
        with open(''.join(playlist_name)+'.json','w+') as f:
                json.dump(json_string_playlist, f)
    #Tried to cast the dict to an object but I couldn't find a propper way to do it
    @staticmethod
    def load(path):
        with open(path,'r') as f:
            data=json.load(f)
        return eval(data)



palylisto=Playlist('rock hard',True,True)

palylisto.add_song(lp_song)
palylisto.add_song(lp_song2)
palylisto.add_song(skilet)

#palylisto.remove_song(lp_song)

# print(palylisto.total_length())
# print(str(palylisto))
#print(palylisto.artists())

# print(palylisto.next_song())
# print(palylisto.next_song())
# print(palylisto.next_song())
# print(palylisto.next_song())

palylisto.save()

