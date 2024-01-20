from textSummarizer.pipeline.stage_01_data_ingestion import (
    DataIngestionTrainingPipeline,
)
from textSummarizer.pipeline.stage_02_data_validation import (
    DataValidationTrainingPipeline,
)
from textSummarizer.logging import logger

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f"{STAGE_NAME} Started")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f"{STAGE_NAME} Completed")
except Exception as e:
    logger.error(f"{STAGE_NAME} Failed with exception: {e}")
    raise e

STAGE_NAME = "Data Validation Stage"

try:
    logger.info(f"{STAGE_NAME} Started")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f"{STAGE_NAME} Completed")
except Exception as e:
    logger.error(f"{STAGE_NAME} Failed with exception: {e}")
    raise e
