"""No TTS service."""
import logging

from scipy.io import wavfile
import voluptuous as vol

import homeassistant.helpers.config_validation as cv
from homeassistant.components.tts import CONF_LANG, PLATFORM_SCHEMA, Provider
from homeassistant.const import CONF_HOST, CONF_PORT
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from urllib.parse import quote


_LOGGER = logging.getLogger(__name__)

SUPPORT_BEEP_OPS = ["1", "0"]

DEFAULT_BEEP = "1"

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Optional(CONF_BEEP, default=DEFAULT_BEEP): vol.In(SUPPORT_BEEP_OPS),
    }
)


def get_engine(hass, config, discovery_info=None):
    """Set up Pico speech component."""
    return NoTTSProvider(hass, config[CONF_BEEP])


class NoTTSProvider(Provider):
    """The No TTS API provider."""

    def __init__(self, hass, beep):
        """Initialize No TTS provider."""
        self._hass = hass
        self._beep = beep
        self.name = "No TTS"

    @property
    def default_language(self):
        """Return the default beep option as language."""
        return self._beep

    @property
    def supported_languages(self):
        """Return list of supported beep options as languages."""
        return SUPPORT_BEEP_OPS

    async def async_get_tts_audio(self, message, language, options=None):
        """Load No TTS beep or no beep wav."""

        """Check beep activation"""
        if language == "1":
            samplerate, data = wavfile.read('./nobeep.wav')
        else:
            samplerate, data = wavfile.read('./beep.wav')
        
        if data:
            return ("wav", data)
        return (None, None)
