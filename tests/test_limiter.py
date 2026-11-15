import unittest
from limiter import TokenBucket, SlidingWindow
class LimiterTests(unittest.TestCase):
    def test_bucket_refills(self):
        b=TokenBucket(2,1); self.assertTrue(b.allow(now=0)); self.assertTrue(b.allow(now=0))
        self.assertFalse(b.allow(now=0)); self.assertTrue(b.allow(now=1))
    def test_window_expires_old_event(self):
        w=SlidingWindow(1,10); self.assertTrue(w.allow(0)); self.assertFalse(w.allow(5)); self.assertTrue(w.allow(10))
    def test_invalid_config(self):
        with self.assertRaises(ValueError): TokenBucket(0,1)
if __name__=="__main__": unittest.main()
