# Smallest AI SDK Cookbook Tests

These tests validate that the Fern-generated Python SDK can perform the same operations as demonstrated in the [Smallest AI Cookbook](https://github.com/smallest-inc/cookbook).

## Test Coverage

The tests cover the following cookbook examples:

### Speech-to-Text (Pulse STT API)
- Basic transcription (`getting-started/`)
- File transcription with advanced features (`file-transcription/`)
- Word-level timestamps and speaker diarization (`word-level-outputs/`)

### Text-to-Speech (Waves API)
- Lightning model synthesis
- Lightning Large model with advanced parameters
- Lightning v2 and v3.1 models
- Streaming TTS

### Voice Management
- List available voices
- Voice cloning (add/delete voices)
- Pronunciation dictionaries

### Atoms (Voice Agents)
- Agent CRUD operations
- Outbound calls
- Knowledge base management
- Campaigns for bulk calling
- Workflows

## Running the Tests

### Prerequisites

1. Install the SDK and test dependencies:
```bash
pip install smallest-ai pytest pytest-asyncio
```

Or install from requirements.txt:
```bash
pip install -r tests/requirements.txt
```

2. Set your API key (optional, for live API tests):
```bash
export SMALLEST_API_KEY="your-api-key"
```

### Run Tests

Run all tests:
```bash
pytest tests/ -v
```

Run specific test file:
```bash
pytest tests/test_speech_to_text.py -v
pytest tests/test_text_to_speech.py -v
pytest tests/test_atoms.py -v
```

Run tests without API key (interface tests only):
```bash
pytest tests/ -v -k "not live"
```

## Test Structure

- `conftest.py` - Pytest fixtures and configuration
- `test_speech_to_text.py` - Speech-to-text interface tests
- `test_text_to_speech.py` - Text-to-speech interface tests
- `test_atoms.py` - Voice agent (Atoms) interface tests

## Notes

These tests primarily validate that the SDK interface matches the cookbook expectations. They test:
- Client structure (sub-clients for waves, atoms)
- Method availability (speech_to_text, synthesize, etc.)
- Parameter acceptance (language, word_timestamps, diarize, etc.)
- Response type structure (transcription, words, utterances, etc.)

For live API testing, set the `SMALLEST_API_KEY` environment variable.
