# Spec: Daily Check-in Streaks (CoachLoop coaching app)

Version 0.1. Owner: Product. Status: Draft.

## Purpose
Clients log a short daily check-in (mood, sleep, one win). A visible streak rewards
consistency so coaches can spot who is slipping.

## Clauses

### CS-01: What counts as a check-in
A check-in counts when the client submits at least a mood rating (1 to 5).
Sleep and "one win" are optional.

### CS-02: One per day
Only one check-in counts per calendar day. Extra submissions that day edit the
existing check-in; they never add to the streak.

### CS-03: Streak calculation
The streak is the number of consecutive calendar days, ending today or yesterday,
with a counted check-in. Days are measured in the **client's local time zone**.
If neither today nor yesterday has a check-in, the streak is 0.

### CS-04: Grace day
Once per rolling 7 days, a single missed day does not break the streak (it does not
add to it either). Grace is applied automatically.

### CS-05: Coach alert
If a client with a streak of 5 or more misses 2 consecutive days, their coach gets
one in-app alert. No more than one alert per client per week.

### CS-06: Privacy
Coaches see streak length and check-in dates, never the free-text "one win" unless
the client marks it shareable.

## Out of scope (v0.1)
Badges, leaderboards, push notifications to clients.
