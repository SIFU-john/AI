from clarifai.client.model import Model

def text_to_speech(input_text, api_key):
    inference_params = dict(voice="alloy", speed=1.0, api_key=api_key)
    model_prediction = Model(
        "https://clarifai.com/openai/tts/models/openai-tts-1"
    ).predict_by_bytes(
        input_text.encode(), input_type="text", inference_params=inference_params
    )
    audio_base64 = model_prediction.outputs[0].data.audio.base64
    return audio_base64