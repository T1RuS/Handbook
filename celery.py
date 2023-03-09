from celery import Celery
from celery.schedules import crontab

app = Celery()

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls test('hello') every 10 seconds.
    sender.add_periodic_task(10.0, test.s('hello'), name='add every 10')

    # Calls test('world') every 30 seconds
    sender.add_periodic_task(30.0, test.s('world'), expires=10)

    # Executes every Monday morning at 7:30 a.m.
    sender.add_periodic_task(
        crontab(hour=7, minute=30, day_of_week=1),
        test.s('Happy Mondays!'),
    )

@app.task
def test(arg):
    print(arg)

@app.task
def add(x, y):
    z = x + y
    print(z)





-----------------------------------------------------------





from celery import shared_task
from django_celery_beat.models import PeriodicTask

from .models import Order


@shared_task(name="repeat_order_make")
def repeat_order_make(order_id):
  order = Order.objects.get(pk=order_id)
  if order.status != '0':
    print('Статус получен!')
    task = PeriodicTask.objects.get(name='Repeat order {}'.format(order_id))
    task.enabled = False
    task.save()
  else:
    # Необходимая логика при повторной отправке заказа
    print('Я должна повторно оформлять заказ каждые 10 секунд')
    
    
    
    
-----------------------------------------------------------

    
    
    
    import json

from django.utils import timezone
from django.core.management.base import BaseCommand, CommandError
from django_celery_beat.models import PeriodicTask, IntervalSchedule
from setups.models import Order

class Command(BaseCommand):
  def add_arguments(self, parser):
    parser.add_argument('status', type=str)
    parser.add_argument('order_id', nargs=1, type=int)

  def handle(self, *args, **options):
    status = options['status']
    order = Order.objects.get(pk=options['order_id'][0])
    if status == '0':
      PeriodicTask.objects.create(
          name='Repeat order {}'.format(options['order_id']),
          task='repeat_order_make',
          interval=IntervalSchedule.objects.get(every=10, period='seconds'),
          args=json.dumps([options['order_id'][0]]),
          start_time=timezone.now(),
        )
    else:
      order.update(status=status)
      order.refresh_from_db()
      # Необходимая логика после удачного получения статуса
      print('Статус вашего заказа -> {}'.format(order.status))
