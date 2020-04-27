import pytube
from moviepy.editor import *
import os,wget
# color
p = '\x1b[0m'
m = '\x1b[91m'
h = '\x1b[92m'
k = '\x1b[93m'
b = '\x1b[94m'
u = '\x1b[95m'
#end
logo='''
%s __   __ %s _______ %s ______  %s _______ %s _     _ %s __    _ 
%s|  | |  |%s|       |%s|      | %s|       |%s| | _ | |%s|  |  | |
%s|  |_|  |%s|_     _|%s|  _    |%s|   _   |%s| || || |%s|   |_| |
%s|       | %s |   |  %s| | |   |%s|  | |  |%s|       |%s|       |
%s|_     _|  %s|   |  %s| |_|   |%s|  |_|  |%s|       |%s|  _    |
 %s |   |    %s|   |  %s|       |%s|       |%s|   _   |%s| | |   |
%s  |___|    %s|___|  %s|______| %s|_______|%s|__| |__|%s|_|  |__|%s
'''%( m, h, k, b, u, k, m, h, k, b, u, k, m, h, k, b, u, k, m, h, k, b, u, k, m, h, k, b, u, k, m, h, k, b, u, k, m, h, k, b, u, k, p)
def download(url):
	global vid
	vid = pytube.YouTube(url)
	print('  %s[%s?%s]%s judul : %s%s'%(k,u,k,b,h,vid.title))
	print('  %s[%s?%s]%s format : %s'%(k,u,k,b,h))
	nol=0
	for i in vid.streams:
		global quality
		if i.type == 'audio':
			quality = i.abr
		elif i.type == 'video':
			quality = i.resolution
		print('\t%s%s.%s%s %skualitas :%s %s'%(k,nol,u,i.mime_type,b,h,quality))
		nol+=1
	while True:
		pil=int(input('  %s[%s?%s]%s format  :%s'%(k,u,k,b,p)))
		sv = input('  %s[%s?%s]%s simpan :%s'%(k,u,k,b,p))
		if sv in ['',' ']:
			print(' [!] Nama Tidak Di dukung')
		elif nol > pil:
			wget.download(vid.streams[pil].url,'%s.%s'%(sv,vid.streams[pil].subtype))
			print('  %s[%s+%s]%s tersimpan : %s %s.%s%s'%(k,u,k,b,h,sv,vid.streams[pil].subtype,p))
			print(' %s[%s?%s]%s apakah ingin di konversi ke mp3'%(k,u,k,b))
			yt = input(' %s[%s?%s]%s Y/T ? : %s'%(k,u,k,b,p))
			if yt in ['Y','y']:
				xvid = VideoFileClip('%s.mp4'%(sv))
				xvid.audio.write_audiofile('%s.mp3'%(sv))
				print(' %s[%s+%s] %stersimpan : %s.mp3%s'%(k,u,k,h,sv,p))
			break
		else:
			print(' %s[x] salah bro%s'%(m,p))
if __name__ == '__main__':
	os.system('clear')
	print(logo)
	download(input('  %s[%s?%s] %surl : %s'%(k,u,k,h,p)))
