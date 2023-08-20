import pymysql



url2="https://www.youtube.com/embed/"
url = "https://www.youtube.com/watch?v=WerCpkTJQTM"
video_id = url.split('=')[-1]
print(url2+''+video_id)
  