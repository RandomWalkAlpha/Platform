from celery import Celery

from data.model import DataModel
from workflow.computing.engine import ComputingEngine

app = Celery('engine', backend='redis://localhost:6379/0', broker='redis://localhost:6379/0')
app.register_task(ComputingEngine())


@app.task(bind=True, base=ComputingEngine)
def parse(self, model: DataModel):
    model.update('queuing')
    expression = model.expression
    model.update('executing')
    result, _ = self.compute(expression)
    self.to_redis(result, model.signal, model.expression)


"""
Startup 'celery' first.
# command: celery -A cmd_manager worker --loglevel=info
"""

if __name__ == '__main__':
    app.start()
