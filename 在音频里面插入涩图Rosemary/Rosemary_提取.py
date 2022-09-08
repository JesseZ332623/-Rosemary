import wave

#打开生成好的，藏有其他文件的歌曲（File name:Afetr_xxxx.wav）。
with wave.open('After_Piano_1.wav','rb') as f:
    wav_data=f.readframes(-1)

#提取wav_data中特殊位置的数据
extract_data=bytearray()
for index in range(0,len(wav_data),4):
    extract_data+=(wav_data[index]).to_bytes(1,byteorder='little')

#得到被隐藏的大小
file_len=int.from_bytes(extract_data[0:3],'little')

#重新生成被隐藏的文件（File name:Result_xxxxxx）
with open('Result_Rosemary.jpg','wb') as f:
    f.write(extract_data[3:file_len+3])