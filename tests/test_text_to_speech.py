"""
Text-to-Speech tests based on the Smallest AI cookbook examples.

These tests validate that the Fern-generated SDK can perform text-to-speech
operations as demonstrated in the cookbook:
- https://github.com/smallest-inc/smallest-python-sdk (WavesClient examples)

The tests validate the SDK interface matches cookbook expectations.
"""

import pytest
from unittest.mock import Mock, patch


class TestTextToSpeechModels:
    """Test that all TTS models from the cookbook are available."""

    def test_lightning_model_available(self, client):
        """
        Cookbook: model="lightning" (default)
        """
        tts = client.waves.text_to_speech
        assert hasattr(tts, 'synthesize_lightning_speech'), \
            "TTS should support 'lightning' model via synthesize_lightning_speech"

    def test_lightning_large_model_available(self, client):
        """
        Cookbook: model="lightning-large"
        """
        tts = client.waves.text_to_speech
        assert hasattr(tts, 'synthesize_lightning_large_speech'), \
            "TTS should support 'lightning-large' model via synthesize_lightning_large_speech"

    def test_lightning_v2_model_available(self, client):
        """
        Cookbook: model="lightning-v2"
        """
        tts = client.waves.text_to_speech
        assert hasattr(tts, 'synthesize_lightningv2speech'), \
            "TTS should support 'lightning-v2' model via synthesize_lightningv2speech"

    def test_lightning_v31_model_available(self, client):
        """
        Cookbook: model="lightning-v3.1"
        """
        tts = client.waves.text_to_speech
        assert hasattr(tts, 'synthesize_lightning_v31speech'), \
            "TTS should support 'lightning-v3.1' model via synthesize_lightning_v31speech"


class TestTextToSpeechParameters:
    """Test that TTS methods accept all cookbook parameters."""

    def test_lightning_accepts_text(self, client):
        """
        Cookbook: waves_client.synthesize(text="Hello world")
        """
        import inspect
        sig = inspect.signature(client.waves.text_to_speech.synthesize_lightning_speech)
        assert 'text' in sig.parameters

    def test_lightning_accepts_voice_id(self, client):
        """
        Cookbook: voice_id="emily" (default)
        """
        import inspect
        sig = inspect.signature(client.waves.text_to_speech.synthesize_lightning_speech)
        assert 'voice_id' in sig.parameters

    def test_lightning_accepts_sample_rate(self, client):
        """
        Cookbook: sample_rate=24000 (default)
        """
        import inspect
        sig = inspect.signature(client.waves.text_to_speech.synthesize_lightning_speech)
        assert 'sample_rate' in sig.parameters

    def test_lightning_accepts_speed(self, client):
        """
        Cookbook: speed=1.0 (default)
        """
        import inspect
        sig = inspect.signature(client.waves.text_to_speech.synthesize_lightning_speech)
        assert 'speed' in sig.parameters

    def test_lightning_accepts_language(self, client):
        """
        Cookbook: language parameter for number pronunciation
        """
        import inspect
        sig = inspect.signature(client.waves.text_to_speech.synthesize_lightning_speech)
        assert 'language' in sig.parameters

    def test_lightning_accepts_output_format(self, client):
        """
        Cookbook: output_format for audio format selection
        """
        import inspect
        sig = inspect.signature(client.waves.text_to_speech.synthesize_lightning_speech)
        assert 'output_format' in sig.parameters


class TestLightningLargeParameters:
    """Test lightning-large specific parameters from cookbook."""

    def test_accepts_consistency(self, client):
        """
        Cookbook: consistency=0.5 (controls word repetition/skipping)
        """
        import inspect
        sig = inspect.signature(client.waves.text_to_speech.synthesize_lightning_large_speech)
        assert 'consistency' in sig.parameters

    def test_accepts_similarity(self, client):
        """
        Cookbook: similarity=0 (controls similarity to reference audio)
        """
        import inspect
        sig = inspect.signature(client.waves.text_to_speech.synthesize_lightning_large_speech)
        assert 'similarity' in sig.parameters

    def test_accepts_enhancement(self, client):
        """
        Cookbook: enhancement=1 (enhances speech quality)
        """
        import inspect
        sig = inspect.signature(client.waves.text_to_speech.synthesize_lightning_large_speech)
        assert 'enhancement' in sig.parameters

    def test_accepts_pronunciation_dicts(self, client):
        """
        Cookbook: pronunciation_dicts for custom pronunciation
        """
        import inspect
        sig = inspect.signature(client.waves.text_to_speech.synthesize_lightning_large_speech)
        assert 'pronunciation_dicts' in sig.parameters


class TestStreamingMethods:
    """Test streaming TTS methods from cookbook."""

    def test_stream_lightning_large_available(self, client):
        """
        Cookbook: TextToAudioStream for real-time TTS
        """
        tts = client.waves.text_to_speech
        assert hasattr(tts, 'stream_lightning_large_speech'), \
            "TTS should support streaming via stream_lightning_large_speech"

    def test_stream_lightningv2_available(self, client):
        """
        Cookbook: Streaming with lightning-v2 model
        """
        tts = client.waves.text_to_speech
        assert hasattr(tts, 'stream_lightningv2speech'), \
            "TTS should support streaming via stream_lightningv2speech"

    def test_stream_lightning_v31_available(self, client):
        """
        Cookbook: Streaming with lightning-v3.1 model
        """
        tts = client.waves.text_to_speech
        assert hasattr(tts, 'stream_lightning_v31speech'), \
            "TTS should support streaming via stream_lightning_v31speech"


class TestVoiceOperations:
    """Test voice management operations from cookbook."""

    def test_voices_client_has_list_method(self, client):
        """
        Cookbook: client.get_voices() to list available voices
        Fern SDK: client.waves.voices.get_waves_voices(model="lightning")
        """
        voices = client.waves.voices
        assert hasattr(voices, 'get_waves_voices'), \
            "Voices client should have 'get_waves_voices' method"

    def test_voice_cloning_client_has_add_method(self, client):
        """
        Cookbook: client.add_voice(display_name="My Voice", file_path="my_voice.wav")
        Fern SDK: client.waves.voice_cloning.add_voice_to_model(display_name="...", file=...)
        """
        voice_cloning = client.waves.voice_cloning
        assert hasattr(voice_cloning, 'add_voice_to_model'), \
            "Voice cloning client should have 'add_voice_to_model' method"

    def test_voice_cloning_client_has_delete_method(self, client):
        """
        Cookbook: client.delete_voice(voice_id)
        Fern SDK: client.waves.voice_cloning.delete_voice_clone(voice_id="...")
        """
        voice_cloning = client.waves.voice_cloning
        assert hasattr(voice_cloning, 'delete_voice_clone'), \
            "Voice cloning client should have 'delete_voice_clone' method"


class TestPronunciationDictionaries:
    """Test pronunciation dictionary operations."""

    def test_pronunciation_dictionaries_client_exists(self, client):
        """
        Cookbook: pronunciation_dicts parameter in TTS
        """
        assert hasattr(client.waves, 'pronunciation_dictionaries'), \
            "Waves should have 'pronunciation_dictionaries' client"


class TestAsyncTextToSpeech:
    """Test async TTS interface matches cookbook AsyncWavesClient."""

    def test_async_tts_has_synthesize_methods(self, async_client):
        """
        Cookbook: AsyncWavesClient with async synthesize methods
        """
        tts = async_client.waves.text_to_speech
        
        assert hasattr(tts, 'synthesize_lightning_speech'), \
            "Async TTS should have 'synthesize_lightning_speech'"
        assert hasattr(tts, 'synthesize_lightning_large_speech'), \
            "Async TTS should have 'synthesize_lightning_large_speech'"

    def test_async_tts_has_stream_methods(self, async_client):
        """
        Cookbook: Async streaming TTS
        """
        tts = async_client.waves.text_to_speech
        
        assert hasattr(tts, 'stream_lightning_large_speech'), \
            "Async TTS should have 'stream_lightning_large_speech'"
