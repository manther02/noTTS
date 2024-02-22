"""No TTS service."""
import logging

import voluptuous as vol

import homeassistant.helpers.config_validation as cv
from homeassistant.components.tts import CONF_LANG, PLATFORM_SCHEMA, Provider


_LOGGER = logging.getLogger(__name__)

SUPPORTED_LANGUAGES = ["1", "0"]

DEFAULT_LANG = "1"

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Optional(CONF_LANG, default=DEFAULT_LANG): vol.In(SUPPORTED_LANGUAGES),
    }
)


def get_engine(hass, config, discovery_info=None):
    """Set up Pico speech component."""
    return NoTTSProvider(hass, config[CONF_LANG])


class NoTTSProvider(Provider):
    """The No TTS API provider."""

    def __init__(self, hass, lang):
        """Initialize No TTS provider."""
        self._hass = hass
        self._lang = lang
        self.name = "No TTS"

    @property
    def default_language(self):
        """Return the default beep option as language."""
        return DEFAULT_LANG

    @property
    def supported_languages(self):
        """Return list of supported beep options as languages."""
        return SUPPORTED_LANGUAGES

    async def async_get_tts_audio(self, message, language, options=None):
        """Load No TTS beep or no beep wav."""

        """Check beep activation""
        if language == "1":
            samplerate, data = wavfile.read('./nobeep.wav')
        else:
            samplerate, data = wavfile.read('./beep.wav')
        """
        data = ""
        
        if data:
            return ("wav", data)
        return (None, None)
