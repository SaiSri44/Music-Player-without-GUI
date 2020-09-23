#!/usr/bin/env python
# coding: utf-8

# In[2]:


import sys
from pygame import mixer
mixer.init()
while True :
    def music_player(playlist,language,i,opinion) :
        while True :
            if opinion == 'f' :
                  i+=1
            elif opinion == 'b':
                  i-=1
            elif opinion == 'e' :
                    mixer.music.stop()
                    sys.exit()
            elif opinion == 's' :
                    mixer.music.stop()
                    break
            elif opinion == 'r' :   
                  mixer.music.unpause()
            elif opinion =='p' :
                    mixer.music.pause()
                    opinion = input("Enter your wish  :  ")
                    continue
            if i>=len(playlist) or i<0 :
                    print("\nThere are no songs to play in the playlist\n")
                    mixer.music.stop()
                    sys.exit() 
            song = language + playlist[i]
            mixer.music.load(song)
            mixer.music.play() 
            opinion = input("Enter your wish  :  ")
    hindi_playlist= ['(LYRICS)_ PACHTAOGE SONG _ ARIJIT SINGH _ JAANI, B PRAAK _ VICKY KAUSHAL, NORA FATEHI.mp3',
 'Lyrical_ Khairiyat _ Chhichhore _ Nitesh Tiwari _ Arijit Singh _ Sushant, Shraddha _ Pritam.mp3',
 'Saree Ke Fall Sa Song hd.mp3',
 'Sunn Raha Hai Na Tu Aashiqui 2 Full Song With Lyrics _ Aditya Roy Kapur, Shraddha Kapoor.mp3',
 'Tum Hi Ho Lyrics & English Translation- Aashiqui 2 (2013).mp3']
    telugu_playlist = [
 'Chinnadana Neekosam - SenSongsmp3.Co.mp3',
 'Current Theega Video Songs __ Pilla O Pilla Video Song __ Manchu Manoj, Rakul PreetSingh.mp3',
 'Devatha - SenSongsmp3.Co.mp3',
 'Diwali Deepaanni - SenSongsmp3.Co.mp3',
 'Guruvaram -- Naasongs.Me.mp3',
 'Nee Kannu Neeli Samudram -SenSongsMp3.Co.mp3',
 'Neetho Edo - SenSongsmp3.Co.mp3',
 'Oh Priya Priya - SenSongsmp3.Co.mp3',
 'Padahaarellaina Song __ Current Theega Full Video Songs __ Sunny Leone, Manchu Manoj, Rakul Preet.mp3',
 'Psycho Saiyaan - SenSongsMp3.Co.mp3',
 'Violin Song-SenSongsMp3.Com.mp3',
 '[iSongs.info] 02 - Po Pove Yekantham.mp3',
 '[iSongs.info] 03 - Life Of Ram.mp3',
 '[iSongs.info] 05 - Luckkanna Mate Nillu.mp3']
    english_playlist = ['Alan Walker & Ava Max - Alone, Pt. II.mp3',
 'Alan Walker - Alone.mp3',
 'Alan Walker - Faded.mp3',
 'Alan Walker, K-391 & Emelie Hollow - Lily.mp3',
 'Alan Walker, Sabrina Carpenter & Farruko - On My Way.mp3',
 'Baby Justin Bieber.mp3',
 'Camila Cabello - Liar.mp3',
 'Camila Cabello - Shameless.mp3',
 'Dharia - (Uu Nai Na) Sugar And Brownies.mp3',
 'DJ Snake & Justin Bieber - Let me love you.mp3',
 'Ed Sheeran - Shape Of You [Official].mp3',
 'Ellie Goulding - Love Me Like You Do.mp3',
 'Imagine Dragons – Thunder 🎵.mp3',
 'Imran khan Satisfya - [English] Trending song color coded.mp3',
 'Love Your Voice.mp3',
 'Marshmello & Anne-Marie - FRIENDS OFFICIAL FRIENDZONE ANTHEM .mp3',
 'Otilia Bilionera ENG.mp3',
 'Serena - Safari.mp3',
 'Shawn Mendes, Camila Cabello – Señorita.mp3',
 'WHITENO1SE & Ranji Ft. Nina Nesbitt - The Moments I m Missing (Radio Edit).mp3']
    print('Press \'p\' to pause the music\n')
    print('press \'e\' to exit the programme\n')
    print('press \'r\' to resume the music\n')
    print('press \'f\' to go to next song\n')
    print('press \'b\' to get back song\n')
    print('press \'s\' to cahnge the playlist\n')
    print( "**** HERE ARE YOU PLAYLISTS *****\n1.hindi\n2.telugu\n3.english\n")
    playlist = input('choose your playlist')
    loc ="C:\\Users\\angaj\\Music\\"
    if playlist == '1' :
        music_player(hindi_playlist,loc+"hindi\\",0,None)
    elif playlist == '2':
         music_player(telugu_playlist,loc+"telugu\\",0,None)
    elif playlist == '3' :
        music_player(english_playlist,loc+"english\\",0,None)
                     
        

