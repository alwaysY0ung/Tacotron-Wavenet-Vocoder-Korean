"""
text: TTS로 변환할 텍스트
output_filename: 출력 오디오 파일 이름
output_dir: 출력 파일을 저장할 디렉토리
history_prompt: 오디오 클로닝을 위한 히스토리 프롬프트 (.npz 파일 경로)
text_temp: 텍스트 생성 온도 (기본값: 0.7)
waveform_temp: 파형 생성 온도 (기본값: 0.7)
silent: 진행 상황 표시줄 비활성화 여부 (기본값: False)
output_full: 전체 생성 결과 반환 여부 (기본값: False)
"""

import os
from bark.api import generate_audio
from bark.generation import SAMPLE_RATE # generation.py 파일에 SAMPLE_RATE 상수가 정의되어 있음. 초당 오디오 샘플링 개수
from scipy.io.wavfile import write as write_wav

def generate_tts_audio(text, output_filename, output_dir):
    try:
        os.makedirs(output_dir, exist_ok=True)
        generated_audio = generate_audio(
            text,
            history_prompt=None,
            text_temp=0.7,
            waveform_temp=0.7,
            silent=False,
            output_full=False,
        )
        output_file_path = os.path.join(output_dir, output_filename)
        write_wav(output_file_path, SAMPLE_RATE, generated_audio)
        #print(f"Done. Output audio file is saved at: '{output_file_path}'")
        return 1
    except Exception as e:
        #print(f"An error occurred: {e}")
        return 0