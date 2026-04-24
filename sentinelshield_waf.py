import re

def detect_attack(request):
    patterns = {
        "SQL Injection": r"(\'|\"|--|#| OR | AND )",
        "XSS": r"<script>.*</script>",
    }
    for attack, pattern in patterns.items():
        if re.search(pattern, request, re.IGNORECASE):
            return attack
    return "Normal"

req = input("Enter HTTP request: ")
result = detect_attack(req)
print("Detection:", result)
