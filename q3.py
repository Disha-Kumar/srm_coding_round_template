"""
Q3: Event Overload Detector

You are analyzing activity logs from a system where users trigger events over time.

Each event contains:
- a `user_id` (integer)
- a `timestamp` (in seconds)

A user is considered **overloaded** if they generate **too many events in a
short period of time**.

Specifically, a user is overloaded if **three or more of their events occur
within any 10-second time window**.

Your task is to identify all such users.

Return a set containing the `user_id`s of all overloaded users.

If no user is overloaded, return an empty set.

Examples:
---------
Input:
events = [
    (1, 10),  # user 1 at time 10
    (1, 12),  # user 1 at time 12
    (1, 18),  # user 1 at time 18
    (2, 5),   # user 2 at time 5
    (2, 20),  # user 2 at time 20
    (3, 1),   # user 3 at time 1
    (3, 2),   # user 3 at time 2
    (3, 3)    # user 3 at time 3
]

Output: {1, 3}

Explanation:
- User 1: Events at [10, 12, 18]
  - From 10 to 18 is 8 seconds, contains 3 events → OVERLOADED
- User 2: Events at [5, 20]
  - Only 2 events, not overloaded
- User 3: Events at [1, 2, 3]
  - From 1 to 3 is 2 seconds, contains 3 events → OVERLOADED

Note: The window is "within 10 seconds", meaning timestamps[j] - timestamps[i] < 10
"""


from collections import defaultdict

def find_overloaded_users(events, threshold=10, window=60):
    user_events = defaultdict(list)

    for user_id, time in events:
        user_events[user_id].append(time)

    overloaded_users = []

    for user_id, times in user_events.items():
        times.sort()
        left = 0

        for right in range(len(times)):
            while times[right] - times[left] > window:
                left += 1

            if right - left + 1 > threshold:
                overloaded_users.append(user_id)
                break

    return sorted(overloaded_users)



if __name__ == "__main__":
    # Test your solution here
    events = [
        (1, 10), (1, 12), (1, 18),
        (3, 1), (3, 2), (3, 3)
    ]
    print(find_overloaded_users(events))  # Should print: {1, 3}

    print(find_overloaded_users([]))  # Should print: set()

    print(find_overloaded_users([(1, 1), (1, 20), (1, 40)]))  # Should print: set()
