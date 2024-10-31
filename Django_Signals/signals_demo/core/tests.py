from django.test import TestCase
from django.db import transaction
import threading
import time
from .models import Order

class SignalTests(TestCase):
    def test_synchronous_signal(self):
        print("\n=== Testing Signal Synchronicity ===")
        print(f"Main execution started: {time.strftime('%H:%M:%S')}")
        Order.objects.create(status='pending')
        print(f"Main execution finished: {time.strftime('%H:%M:%S')}")

    def test_signal_thread(self):
        print("\n=== Testing Signal Thread ===")
        main_thread = threading.current_thread()
        print(f"Main thread: {main_thread.name}")
        Order.objects.create(status='pending')

    def test_signal_transaction(self):
        print("\n=== Testing Signal Transaction ===")
        with transaction.atomic():
            print(f"Main transaction state: {transaction.get_connection().in_atomic_block}")
            Order.objects.create(status='pending')