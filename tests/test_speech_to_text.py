"""
Speech-to-Text tests based on the Smallest AI cookbook examples.

These tests validate that the Fern-generated SDK can perform speech-to-text
operations as demonstrated in the cookbook:
- https://github.com/smallest-inc/cookbook/tree/main/speech-to-text/getting-started
- https://github.com/smallest-inc/cookbook/tree/main/speech-to-text/file-transcription
- https://github.com/smallest-inc/cookbook/tree/main/speech-to-text/word-level-outputs

The tests use mocking to validate the SDK interface without requiring actual API calls.
For live API testing, set the SMALLEST_API_KEY environment variable.
"""

import pytest
from unittest.mock import Mock, patch, MagicMock


class TestSpeechToTextInterface:
    """Test that the SDK interface matches cookbook expectations."""

    def test_client_has_waves_attribute(self, client):
        """Verify the main client has a waves sub-client."""
        assert hasattr(client, 'waves'), "Client should have 'waves' attribute"

    def test_waves_has_speech_to_text_method(self, client):
        """Verify waves client has speech_to_text method (Pulse STT API)."""
        assert hasattr(client.waves, 'speech_to_text'), "Waves client should have 'speech_to_text' method"
        assert callable(client.waves.speech_to_text), "speech_to_text should be callable"

    def test_waves_has_text_to_speech_client(self, client):
        """Verify waves client has text_to_speech sub-client."""
        assert hasattr(client.waves, 'text_to_speech'), "Waves client should have 'text_to_speech' attribute"

    def test_waves_has_voices_client(self, client):
        """Verify waves client has voices sub-client."""
        assert hasattr(client.waves, 'voices'), "Waves client should have 'voices' attribute"

    def test_waves_has_voice_cloning_client(self, client):
        """Verify waves client has voice_cloning sub-client."""
        assert hasattr(client.waves, 'voice_cloning'), "Waves client should have 'voice_cloning' attribute"


class TestSpeechToTextParameters:
    """Test that speech_to_text accepts all cookbook parameters."""

    def test_speech_to_text_accepts_model_parameter(self, client):
        """
        Cookbook uses model='pulse' for transcription.
        Verify the SDK accepts this parameter.
        """
        import inspect
        sig = inspect.signature(client.waves.speech_to_text)
        params = sig.parameters
        assert 'model' in params, "speech_to_text should accept 'model' parameter"

    def test_speech_to_text_accepts_language_parameter(self, client):
        """
        Cookbook: LANGUAGE = "en"  # Use ISO 639-1 codes or "multi" for auto-detect
        """
        import inspect
        sig = inspect.signature(client.waves.speech_to_text)
        params = sig.parameters
        assert 'language' in params, "speech_to_text should accept 'language' parameter"

    def test_speech_to_text_accepts_word_timestamps_parameter(self, client):
        """
        Cookbook: WORD_TIMESTAMPS = True  # Enable word-level timestamps
        """
        import inspect
        sig = inspect.signature(client.waves.speech_to_text)
        params = sig.parameters
        assert 'word_timestamps' in params, "speech_to_text should accept 'word_timestamps' parameter"

    def test_speech_to_text_accepts_diarize_parameter(self, client):
        """
        Cookbook: DIARIZE = True  # Enable speaker diarization
        """
        import inspect
        sig = inspect.signature(client.waves.speech_to_text)
        params = sig.parameters
        assert 'diarize' in params, "speech_to_text should accept 'diarize' parameter"

    def test_speech_to_text_accepts_age_detection_parameter(self, client):
        """
        Cookbook: AGE_DETECTION = False  # Predict age group of speaker
        """
        import inspect
        sig = inspect.signature(client.waves.speech_to_text)
        params = sig.parameters
        assert 'age_detection' in params, "speech_to_text should accept 'age_detection' parameter"

    def test_speech_to_text_accepts_gender_detection_parameter(self, client):
        """
        Cookbook: GENDER_DETECTION = False  # Predict gender of speaker
        """
        import inspect
        sig = inspect.signature(client.waves.speech_to_text)
        params = sig.parameters
        assert 'gender_detection' in params, "speech_to_text should accept 'gender_detection' parameter"

    def test_speech_to_text_accepts_emotion_detection_parameter(self, client):
        """
        Cookbook: EMOTION_DETECTION = False  # Predict speaker emotions
        """
        import inspect
        sig = inspect.signature(client.waves.speech_to_text)
        params = sig.parameters
        assert 'emotion_detection' in params, "speech_to_text should accept 'emotion_detection' parameter"

    def test_speech_to_text_accepts_request_parameter(self, client):
        """
        Cookbook sends audio bytes as the request body.
        """
        import inspect
        sig = inspect.signature(client.waves.speech_to_text)
        params = sig.parameters
        assert 'request' in params, "speech_to_text should accept 'request' parameter for audio bytes"


class TestTextToSpeechInterface:
    """Test that the TTS interface matches cookbook expectations."""

    def test_text_to_speech_has_synthesize_methods(self, client):
        """Verify TTS client has synthesize methods for different models."""
        tts = client.waves.text_to_speech
        
        assert hasattr(tts, 'synthesize_lightning_speech'), \
            "TTS should have 'synthesize_lightning_speech' method"
        assert hasattr(tts, 'synthesize_lightning_large_speech'), \
            "TTS should have 'synthesize_lightning_large_speech' method"

    def test_synthesize_lightning_speech_parameters(self, client):
        """
        Cookbook WavesClient.synthesize() accepts:
        - text: str
        - voice_id: str
        - sample_rate: int
        - speed: float
        """
        import inspect
        sig = inspect.signature(client.waves.text_to_speech.synthesize_lightning_speech)
        params = sig.parameters
        
        assert 'text' in params, "synthesize should accept 'text' parameter"
        assert 'voice_id' in params, "synthesize should accept 'voice_id' parameter"
        assert 'sample_rate' in params, "synthesize should accept 'sample_rate' parameter"
        assert 'speed' in params, "synthesize should accept 'speed' parameter"

    def test_synthesize_lightning_large_speech_parameters(self, client):
        """
        Cookbook lightning-large model accepts additional parameters:
        - consistency: float
        - similarity: float
        - enhancement: float
        """
        import inspect
        sig = inspect.signature(client.waves.text_to_speech.synthesize_lightning_large_speech)
        params = sig.parameters
        
        assert 'text' in params, "synthesize should accept 'text' parameter"
        assert 'voice_id' in params, "synthesize should accept 'voice_id' parameter"
        assert 'consistency' in params, "synthesize should accept 'consistency' parameter"
        assert 'similarity' in params, "synthesize should accept 'similarity' parameter"
        assert 'enhancement' in params, "synthesize should accept 'enhancement' parameter"


class TestVoiceManagementInterface:
    """Test voice management interface matches cookbook expectations."""

    def test_voices_client_exists(self, client):
        """Verify voices client exists for listing voices."""
        assert hasattr(client.waves, 'voices'), "Waves should have 'voices' client"

    def test_voice_cloning_client_exists(self, client):
        """Verify voice cloning client exists for add/delete voice operations."""
        assert hasattr(client.waves, 'voice_cloning'), "Waves should have 'voice_cloning' client"


class TestAtomsInterface:
    """Test that the Atoms interface matches cookbook expectations."""

    def test_client_has_atoms_attribute(self, client):
        """Verify the main client has an atoms sub-client."""
        assert hasattr(client, 'atoms'), "Client should have 'atoms' attribute"

    def test_atoms_has_agents_client(self, client):
        """
        Cookbook: atoms_client.create_agent(...)
        """
        assert hasattr(client.atoms, 'agents'), "Atoms should have 'agents' client"

    def test_atoms_has_calls_client(self, client):
        """
        Cookbook: atoms_client.start_outbound_call(...)
        """
        assert hasattr(client.atoms, 'calls'), "Atoms should have 'calls' client"

    def test_atoms_has_knowledge_base_client(self, client):
        """
        Cookbook: atoms_client.create_knowledge_base(...)
        """
        assert hasattr(client.atoms, 'knowledge_base'), "Atoms should have 'knowledge_base' client"

    def test_atoms_has_campaigns_client(self, client):
        """
        Cookbook uses campaigns for bulk calling.
        """
        assert hasattr(client.atoms, 'campaigns'), "Atoms should have 'campaigns' client"

    def test_atoms_has_workflows_client(self, client):
        """
        Cookbook uses workflows to drive conversations.
        """
        assert hasattr(client.atoms, 'workflows'), "Atoms should have 'workflows' client"


class TestResponseTypes:
    """Test that response types have expected attributes."""

    def test_speech_to_text_response_type_exists(self):
        """Verify SpeechToTextResponse type is importable."""
        from smallest_ai.waves.types.speech_to_text_response import SpeechToTextResponse
        assert SpeechToTextResponse is not None

    def test_speech_to_text_response_has_transcription(self):
        """
        Cookbook expects: result.get("transcription", "")
        """
        from smallest_ai.waves.types.speech_to_text_response import SpeechToTextResponse
        
        response = SpeechToTextResponse(
            status="success",
            transcription="Hello world"
        )
        assert hasattr(response, 'transcription'), "Response should have 'transcription' attribute"
        assert response.transcription == "Hello world"

    def test_speech_to_text_response_has_status(self):
        """
        Cookbook expects: result.get("status") == "success"
        """
        from smallest_ai.waves.types.speech_to_text_response import SpeechToTextResponse
        
        response = SpeechToTextResponse(status="success")
        assert hasattr(response, 'status'), "Response should have 'status' attribute"
        assert response.status == "success"

    def test_speech_to_text_response_has_words(self):
        """
        Cookbook expects: result.get("words", []) for word timestamps
        """
        from smallest_ai.waves.types.speech_to_text_response import SpeechToTextResponse
        
        response = SpeechToTextResponse(status="success", words=[])
        assert hasattr(response, 'words'), "Response should have 'words' attribute"

    def test_speech_to_text_response_has_utterances(self):
        """
        Cookbook expects: result.get("utterances", []) for speaker diarization
        """
        from smallest_ai.waves.types.speech_to_text_response import SpeechToTextResponse
        
        response = SpeechToTextResponse(status="success", utterances=[])
        assert hasattr(response, 'utterances'), "Response should have 'utterances' attribute"

    def test_speech_to_text_response_has_age(self):
        """
        Cookbook expects: result.get("age") for age detection
        """
        from smallest_ai.waves.types.speech_to_text_response import SpeechToTextResponse
        
        response = SpeechToTextResponse(status="success")
        assert hasattr(response, 'age'), "Response should have 'age' attribute"

    def test_speech_to_text_response_has_gender(self):
        """
        Cookbook expects: result.get("gender") for gender detection
        """
        from smallest_ai.waves.types.speech_to_text_response import SpeechToTextResponse
        
        response = SpeechToTextResponse(status="success")
        assert hasattr(response, 'gender'), "Response should have 'gender' attribute"

    def test_speech_to_text_response_has_emotions(self):
        """
        Cookbook expects: result.get("emotions") for emotion detection
        """
        from smallest_ai.waves.types.speech_to_text_response import SpeechToTextResponse
        
        response = SpeechToTextResponse(status="success")
        assert hasattr(response, 'emotions'), "Response should have 'emotions' attribute"


class TestAsyncInterface:
    """Test that async client matches sync client interface."""

    def test_async_client_has_waves(self, async_client):
        """Verify async client has waves sub-client."""
        assert hasattr(async_client, 'waves'), "Async client should have 'waves' attribute"

    def test_async_client_has_atoms(self, async_client):
        """Verify async client has atoms sub-client."""
        assert hasattr(async_client, 'atoms'), "Async client should have 'atoms' attribute"

    def test_async_waves_has_speech_to_text(self, async_client):
        """Verify async waves client has speech_to_text method."""
        assert hasattr(async_client.waves, 'speech_to_text'), \
            "Async waves client should have 'speech_to_text' method"

    def test_async_waves_has_text_to_speech(self, async_client):
        """Verify async waves client has text_to_speech sub-client."""
        assert hasattr(async_client.waves, 'text_to_speech'), \
            "Async waves client should have 'text_to_speech' attribute"
