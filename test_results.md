### Destination Rule Testing 
```
=== LOAD BALANCING RESULT HEALTH (Pod IP) ===
10.244.0.113: 13 requests
10.244.0.115: 13 requests
10.244.0.112: 13 requests
10.244.0.111: 11 requests

=== LOAD BALANCING RESULT HEALTH (Version) ===
v1: 24 requests
v2: 26 requests

Errors: 0
=== Test Finished ===

=== LOAD BALANCING RESULT PROCESS (Pod IP) ===
10.244.0.111: 13 requests
10.244.0.113: 13 requests
10.244.0.115: 9 requests
10.244.0.112: 10 requests

=== LOAD BALANCING RESULT PROCESS (Version) ===
v1: 26 requests
v2: 19 requests

Errors: 5
=== Test Finished ===
```

### Virtual Service Testing
```
=== LOAD BALANCING RESULT HEALTH (Pod IP) ===
10.244.0.113: 22 requests
10.244.0.111: 22 requests
10.244.0.112: 4 requests
10.244.0.115: 2 requests

=== LOAD BALANCING RESULT HEALTH (Version) ===
v1: 44 requests
v2: 6 requests

Errors: 0
=== Test Finished ===

=== LOAD BALANCING RESULT PROCESS (Pod IP) ===
10.244.0.111: 23 requests
10.244.0.113: 23 requests
10.244.0.112: 3 requests
10.244.0.115: 1 requests

=== LOAD BALANCING RESULT PROCESS (Version) ===
v1: 46 requests
v2: 4 requests

Errors: 0
=== Test Finished ===
```
