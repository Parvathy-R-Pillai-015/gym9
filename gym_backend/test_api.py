import requests
import json

response = requests.get('http://127.0.0.1:8000/api/trainer/3/users/')
print('Status:', response.status_code)

data = response.json()
print('Success:', data.get('success'))
print('Total Users:', data.get('total'))

print('\nUsers:')
for u in data.get('users', []):
    print(f"  - {u['name']} ({u['email']}) - {u['remaining_days']} days left")
    print(f"    Payment: {u['payment_amount']}, Attendance: {u['total_attendance']}")
