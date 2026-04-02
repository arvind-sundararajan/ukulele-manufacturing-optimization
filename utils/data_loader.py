```json
{
    "utils/data_loader.py": {
        "content": "
import logging
from typing import List, Dict
from pydantic import BaseModel
from sklearn.model_selection import train_test_split
from langwatch.ai import StateGraph

# Define a logger
logger = logging.getLogger(__name__)

class UkuleleData(BaseModel):
    """Ukulele data model"""
    non_stationary_drift_index: float
    stochastic_regime_switch: bool
    manufacturing_yield: int

def load_ukulele_data(data_path: str) -> List[Dict]:
    """
    Load ukulele data from a file.

    Args:
    - data_path (str): Path to the data file.

    Returns:
    - List[Dict]: List of dictionaries containing ukulele data.

    Raises:
    - FileNotFoundError: If the data file is not found.
    """
    try:
        # Load data from file
        with open(data_path, 'r') as file:
            data = [UkuleleData(**line) for line in file]
        logger.info('Data loaded successfully')
        return data
    except FileNotFoundError:
        logger.error('Data file not found')
        raise

def split_data(data: List[Dict], test_size: float = 0.2) -> tuple:
    """
    Split data into training and testing sets.

    Args:
    - data (List[Dict]): List of dictionaries containing ukulele data.
    - test_size (float): Proportion of data to use for testing.

    Returns:
    - tuple: Training and testing data sets.
    """
    try:
        # Split data into training and testing sets
        train_data, test_data = train_test_split(data, test_size=test_size)
        logger.info('Data split successfully')
        return train_data, test_data
    except Exception as e:
        logger.error(f'Data split failed: {e}')
        raise

def create_state_graph(data: List[Dict]) -> StateGraph:
    """
    Create a state graph from the data.

    Args:
    - data (List[Dict]): List of dictionaries containing ukulele data.

    Returns:
    - StateGraph: State graph representing the data.
    """
    try:
        # Create a state graph
        state_graph = StateGraph()
        for item in data:
            state_graph.add_state(item.non_stationary_drift_index, item.stochastic_regime_switch)
        logger.info('State graph created successfully')
        return state_graph
    except Exception as e:
        logger.error(f'State graph creation failed: {e}')
        raise

if __name__ == '__main__':
    # Simulate the 'Rocket Science' problem
    data_path = 'ukulele_data.csv'
    data = load_ukulele_data(data_path)
    train_data, test_data = split_data(data)
    state_graph = create_state_graph(train_data)
    logger.info('Rocket Science problem simulated successfully')
",
        "commit_message": "feat: implement specialized data_loader logic"
    }
}
```