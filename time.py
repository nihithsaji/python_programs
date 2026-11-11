class Time:
    def __init__(self, h, m, s):
        self._hour = h
        self._minute = m
        self._second = s

    def __add__(self, t):
        h = self._hour + t._hour
        m = self._minute + t._minute
        s = self._second + t._second

        if s >= 60:
            m = m + (s // 60)
            s = s % 60

        if m >= 60:
            h = h + (m // 60)
            m = m % 60

        return Time(h, m, s)

    def display(self):
        print("Time:", self._hour, ":", self._minute, ":", self._second)


t1 = Time(2,45,50)
t2 = Time(1,30,20)

print("First Time:")
t1.display()

print("Second Time:")
t2.display()

t3 = t1 + t2

print("Addition of Two Times:")
t3.display()
