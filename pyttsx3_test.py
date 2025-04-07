import pyttsx3

text = "你好，世界"
# 初始化
engine = pyttsx3.init()

voices = engine.getProperty('voices')
# 語速控制
rate = engine.getProperty('rate')
print(rate)
engine.setProperty('rate', rate-70)
# 音量控制
volume = engine.getProperty('volume')
print(volume)
engine.setProperty('volume', volume-0.25)
engine.say(text)
# engine.save_to_file(text, 'chinese.mp3')
engine.runAndWait()
