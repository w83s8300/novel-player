from gtts import gTTS
import pyttsx3

def  output_gTTS(text,name):
    # 創建語音實例
    tts = gTTS(text=text, lang="zh-tw")
    # 儲存語音檔案
    tts.save(f"./save/{name}.mp3")
    
def  output_pyttsx3(text,name):
    # 初始化
    engine = pyttsx3.init()
    # 語速控制
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-30)
    # 音量控制
    volume = engine.getProperty('volume')
    engine.setProperty('volume', volume-0.25)
    engine.save_to_file(text, f"./save/{name}.mp3")
    engine.runAndWait()
