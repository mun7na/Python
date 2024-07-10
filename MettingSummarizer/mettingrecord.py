from pvrecorder import PvRecorder
import wave, struct

for index, device in enumerate(PvRecorder.get_available_devices()):
    print(f"[{index}] {device}")

    recoder = PvRecorder(device_index=-1, frame_length=512)
    audio = []
    path = 'audio_recording.wav'

    try:
        recoder.start()

        while True:
            frame = recoder.read()
            audio.extend(frame)
    except KeyboardInterrupt:
        recoder.stop()
        with wave.open(path, 'w') as f:
            f.setparams((1, 2, 16000, 512, "NONE", "NONE"))
            f.writeframes(struct.pack("h" * len(audio), *audio) )
    finally :
        recoder.delete()