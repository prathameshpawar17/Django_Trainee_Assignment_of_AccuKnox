from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import threading
import time
from django.db import transaction

class Order(models.Model):
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} - {self.status}"

@receiver(post_save, sender=Order)
def order_post_save_sync(sender, instance, created, **kwargs):
    print(f"[Sync Test] Signal started: {time.strftime('%H:%M:%S')}")
    time.sleep(2)  # Simulate work
    print(f"[Sync Test] Signal finished: {time.strftime('%H:%M:%S')}")

@receiver(post_save, sender=Order)
def order_post_save_thread(sender, instance, created, **kwargs):
    current_thread = threading.current_thread()
    print(f"[Thread Test] Signal thread: {current_thread.name}")

@receiver(post_save, sender=Order)
def order_post_save_transaction(sender, instance, created, **kwargs):
    print(f"[Transaction Test] In transaction: {transaction.get_connection().in_atomic_block}")