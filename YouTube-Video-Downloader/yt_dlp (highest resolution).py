import yt_dlp
import os
import sys

script_dir = os.path.dirname(os.path.abspath(__file__))
ffmpeg_path = os.path.join(script_dir, "ffmpeg.exe")


if not os.path.exists(ffmpeg_path):
    print(f"❌ HATA: ffmpeg.exe bulunamadı!\nAranan yer: {ffmpeg_path}")
    sys.exit()


url = input("Video Linkini Yapıştır: ")

print("\n İndiriliyor ")

# Ayarlar:
ydl_opts = {
    # 1. görüntü ve sesi indir
    'format': 'bestvideo+bestaudio/best',

    # MP4
    'merge_output_format': 'mp4',

    #  FFmpeg'i göster
    'ffmpeg_location': ffmpeg_path,

    #AAC formatına çevir (For Windows)
    'postprocessor_args': {
        'merger': ['-c:a', 'aac', '-b:a', '192k']
    },

    # 5. Dosya isim ayarı ve üzerine yazma izni
    'outtmpl': '%(title)s.%(ext)s',
    'overwrites': True,
}

print("\n İndirme başlıyor... ")

try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print("\n✅ İndirme Tamamlandı! ")

except Exception as e:
    print(f"\n❌ Hata: {e}")
    print("Not: Eğer hata 'ffmpeg' ile ilgiliyse, bilgisayarına ffmpeg kurman gerek.")
