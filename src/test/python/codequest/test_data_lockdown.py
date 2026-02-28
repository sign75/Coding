import unittest
from codequest.data_lockdown import filter_logs

class TestDataLockdown(unittest.TestCase):
    def test_sample_cases(self):
        test_cases = [
            (
                [
                    "www.google.com 128",
                    "www.dropbox.com 1424",
                    "www.cnn.com 142",
                    "codequest.global.lmco.com 212",
                    "www.australia.gov.au 4120",
                    "filetransfer.us.lmco.com 2186"
                ],
                [
                    "www.dropbox.com 1424",
                    "www.australia.gov.au 4120"
                ]
            )
        ]

        for i, (logs, expected) in enumerate(test_cases):
            with self.subTest(i=i):
                actual_result = filter_logs(logs)
                self.assertEqual(
                    actual_result, 
                    expected, 
                    f"Failed on case {i+1}"
                )

if __name__ == '__main__':
    unittest.main()