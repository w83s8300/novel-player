from gtts_test import gTTS
# 輸入要轉換的文字
text = input("請輸入要轉換為語音的文字：")

# 創建語音實例
tts = gTTS(text=text, lang="zh-tw")

# 儲存語音檔案
tts.save("output.mp3")
