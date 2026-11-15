"""Two in-memory rate-limit algorithms for API gateways."""
from collections import deque
from dataclasses import dataclass, field
from time import monotonic

@dataclass
class TokenBucket:
    capacity: int
    refill_per_second: float
    tokens: float = field(init=False)
    updated: float = field(default_factory=monotonic)
    def __post_init__(self):
        if self.capacity < 1 or self.refill_per_second <= 0: raise ValueError("capacity and refill rate must be positive")
        self.tokens=float(self.capacity)
    def allow(self, cost: float=1, now: float|None=None) -> bool:
        if cost <= 0 or cost > self.capacity: return False
        current=monotonic() if now is None else now
        elapsed=max(0,current-self.updated)
        self.tokens=min(self.capacity,self.tokens+elapsed*self.refill_per_second); self.updated=current
        if self.tokens < cost: return False
        self.tokens-=cost; return True

@dataclass
class SlidingWindow:
    limit: int
    window_seconds: float
    events: deque = field(default_factory=deque)
    def __post_init__(self):
        if self.limit < 1 or self.window_seconds <= 0: raise ValueError("limit and window must be positive")
    def allow(self, now: float) -> bool:
        while self.events and self.events[0] <= now-self.window_seconds: self.events.popleft()
        if len(self.events)>=self.limit: return False
        self.events.append(now); return True
