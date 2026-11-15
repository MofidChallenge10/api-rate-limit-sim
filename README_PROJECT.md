# API Rate Limit Simulator
Compare an in-memory token bucket with a fixed-duration sliding event window.

## Run
```bash
python -m unittest discover -s tests -v
```

The classes accept explicit timestamps for deterministic simulations. TokenBucket refills continuously; SlidingWindow expires events at the window boundary. These are teaching/reference implementations, not distributed production limiters.
