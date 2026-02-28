import unittest
from codequest.deep_space_messages import decode_message

class TestDeepSpaceMessages(unittest.TestCase):
    def test_sample_cases(self):
        test_cases = [
            ("dksieidik25nckdso15jklalfue21", "you"),
            ("aksleodnc1xsoeidmc18oeod5", "are"),
            ("utapszm14peu15owauet20", "not"),
            ("spepdoclqmen1oeudle12peeo15ae14epep5", "alone")
        ]

        for i, (msg, expected) in enumerate(test_cases):
            with self.subTest(i=i, msg=msg):
                actual_result = decode_message(msg)
                self.assertEqual(
                    actual_result, 
                    expected, 
                    f"Failed on case {i+1}"
                )

if __name__ == '__main__':
    unittest.main()