from transformers import WhisperProcessor, WhisperForConditionalGeneration
import librosa
import torch
device = "cuda:0" if torch.cuda.is_available() else "cpu"

# processor = WhisperProcessor.from_pretrained("openai/whisper-large")
# model = WhisperForConditionalGeneration.from_pretrained("openai/whisper-large").to(device)
# # model.config.forced_decoder_ids = WhisperProcessor.get_decoder_prompt_ids(language="english", task="transcribe")
# model.config.forced_decoder_ids = None

y, sr = librosa.load('behaviortrapmegan.mp3')
y_resamp = librosa.resample(y, orig_sr=sr, target_sr=16000)

# input_features = processor(y_resamp, sampling_rate=16000, return_tensors="pt").input_features.to(device)
# # generate token ids
# predicted_ids = model.generate(input_features)
# # transcription = processor.batch_decode(predicted_ids, skip_special_tokens=False)
#
# transcription = processor.batch_decode(predicted_ids, skip_special_tokens=True)



from transformers import pipeline
pipe = pipeline(
  "automatic-speech-recognition",
  model="openai/whisper-medium",
  stride_length_s=30,
  device=device,
)

# ds = load_dataset("hf-internal-testing/librispeech_asr_dummy", "clean", split="validation")
# sample = ds[0]["audio"]

prediction = pipe({"array" : y_resamp.copy(), "sampling_rate" : 16000}, batch_size=8)["text"]
import ipdb
ipdb.set_trace()
# " Mr. Quilter is the apostle of the middle classes, and we are glad to welcome his gospel."

# we can also return timestamps for the predictions
# prediction = pipe(sample.copy(), batch_size=8, return_timestamps=True)["chunks"]
# [{'text': ' Mr. Quilter is the apostle of the middle classes and we are glad to welcome his gospel.',
#   'timestamp': (0.0, 5.44)}]
