"""
Pytest configuration and fixtures for Smallest AI SDK cookbook tests.

These tests validate that the Fern-generated SDK can perform the same
operations as the examples in the Smallest AI cookbook.
"""

import os
import pytest


@pytest.fixture
def api_key():
    """Get the Smallest AI API key from environment."""
    key = os.environ.get("SMALLEST_API_KEY")
    if not key:
        pytest.skip("SMALLEST_API_KEY environment variable not set")
    return key


@pytest.fixture
def client(api_key):
    """Create a SmallestAI client instance."""
    from smallest_ai import SmallestAI
    return SmallestAI(token=api_key)


@pytest.fixture
def async_client(api_key):
    """Create an AsyncSmallestAI client instance."""
    from smallest_ai import AsyncSmallestAI
    return AsyncSmallestAI(token=api_key)


@pytest.fixture
def sample_audio_bytes():
    """
    Generate a simple WAV audio file with silence for testing.
    This creates a minimal valid WAV file that can be used for API testing.
    """
    import struct
    import io
    
    sample_rate = 16000
    duration_seconds = 1
    num_samples = sample_rate * duration_seconds
    
    audio_data = io.BytesIO()
    audio_data.write(b'RIFF')
    audio_data.write(struct.pack('<I', 36 + num_samples * 2))
    audio_data.write(b'WAVE')
    audio_data.write(b'fmt ')
    audio_data.write(struct.pack('<I', 16))
    audio_data.write(struct.pack('<H', 1))
    audio_data.write(struct.pack('<H', 1))
    audio_data.write(struct.pack('<I', sample_rate))
    audio_data.write(struct.pack('<I', sample_rate * 2))
    audio_data.write(struct.pack('<H', 2))
    audio_data.write(struct.pack('<H', 16))
    audio_data.write(b'data')
    audio_data.write(struct.pack('<I', num_samples * 2))
    
    for _ in range(num_samples):
        audio_data.write(struct.pack('<h', 0))
    
    return audio_data.getvalue()
