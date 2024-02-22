# Home Assistant Component for no TTS.

[![hacs_badge](https://img.shields.io/badge/HACS-default-orange.svg)](https://github.com/custom-components/hacs)

This is a component for Home Assistant which fakes the TTS system but instead just plays a beep sound.

# Installation

## HACS

Install it in the `Integrations` tab on the [Home Asssistant Community Store](https://github.com/custom-components/hacs).

## Manual way
To use it, copy the `notts` folder inside your `config/custom_components` folder on your home assistant installation first.


# Configuration

Add following config to your yaml if you are using the Supervisor Addon

ATENTION: The beep is temporarily disabled.

```yaml
tts:
  - platform: notts
    beep: "1" to beep or "0" for no beep
```
