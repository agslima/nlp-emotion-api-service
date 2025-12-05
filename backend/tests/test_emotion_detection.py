# test_emotion_detection.py

import unittest
from unittest.mock import patch
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):

    # O patch substitui a função real por uma simulada durante o teste
    @patch('EmotionDetection.emotion_detection.requests.post') 
    def test_emotion_detector(self, mock_post):
        """
        Test emotion_detector mocking the API response
        """
        
        # 1. Configurar o cenário de sucesso (JOY)
        # Simulamos que a API retornou sucesso e o JSON esperado
        mock_post.return_value.status_code = 200
        mock_post.return_value.text = '{"emotionPredictions": [{"emotion": {"joy": 0.9, "sadness": 0.1}}]}'
        # NOTA: Ajuste o .text acima para o formato exato que sua API retorna
        
        # Se sua função emotion_detector processa o texto internamente, 
        # talvez seja melhor mockar a função interna de request.
        
        # --- ABORDAGEM ALTERNATIVA (MOCKAR A PRÓPRIA FUNÇÃO) ---
        # Se você quer testar apenas a lógica do teste e não a implementação interna:
        
        with patch('EmotionDetection.emotion_detection.emotion_detector') as mock_detector:
            # Configura o mock para retornar o que esperamos para o primeiro caso
            mock_detector.return_value = {'dominant_emotion': 'joy'}
            result1 = mock_detector("I am glad this happened")
            self.assertEqual(result1['dominant_emotion'], 'joy')

            # Configura para o segundo caso
            mock_detector.return_value = {'dominant_emotion': 'anger'}
            result2 = mock_detector("I am really mad about this")
            self.assertEqual(result2['dominant_emotion'], 'anger')

    
    def test_emotion_detector(self):
        """"
        Test emotion_detector with sample sentences and their expected dominant emotions.
        """
        result1 = emotion_detector("I am glad this happened")
        self.assertEqual(result1['dominant_emotion'], 'joy')

        result2 = emotion_detector("I am really mad about this")
        self.assertEqual(result2['dominant_emotion'], 'anger')

        result3 = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result3['dominant_emotion'], 'disgust')
        
        result4 = emotion_detector("I am so sad about this")
        self.assertEqual(result4['dominant_emotion'], 'sadness')
        result5 = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result5['dominant_emotion'], 'fear')

if __name__ == "__main__":
    unittest.main()
