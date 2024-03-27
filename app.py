from isd.pipeline.training_pipeline import TrainPipeline
import os
os.environ['WANDB_DISABLED'] = 'true'
obj=TrainPipeline()
obj.run_pipeline()
