from datetime import datetime, timedelta
from apscheduler.schedulers.background import BackgroundScheduler
from .models import Item

def remove_purchased_items():
    cutoff_time = datetime.utcnow() - timedelta(minutes=1)
    Item.objects.filter(purchased=True, timestamp__lt=cutoff_time).delete()

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(remove_purchased_items, 'interval', minutes=1)
    scheduler.start()
