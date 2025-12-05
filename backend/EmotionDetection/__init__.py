"""
Este módulo inicializa o pacote EmotionDetection.
Ele expõe a função emotion_detector para uso externo.
"""

# pylint: disable=invalid-name

from .emotion_detection import emotion_detector

__all__ = ["emotion_detector"]
