
import numpy as np

def get_all_adjacent_blocks(grid,distance=1, operation=None) -> list:
    result_list = list()
    x_max,y_max = grid.shape
    for x in range(0,x_max):
            for y in range(0,y_max):
                block = get_adjacent_blocks(grid,x,y,distance)
                if operation:
                    result_list.append(operation(block))
                else:
                    result_list.append(block)
    return result_list



def get_adjacent_blocks(grid: np.matrix,x,y,distance=1) -> tuple[tuple[int,int], np.matrix]:
    """
    Extracts a rectangular block of adjacent cells from a grid centered around a given position.
    Args:
        grid (np.matrix): The input grid/matrix from which to extract the block.
        x (int): The x-coordinate (row index) of the center position.
        y (int): The y-coordinate (column index) of the center position.
        distance (int, optional): The distance from the center position to include in each direction. Defaults to 1.
    Returns:
        tuple[tuple[int,int], np.matrix]: A tuple containing:
            - A tuple of (x, y) representing the center coordinates
            - A numpy matrix containing the extracted adjacent block
    Note:
        The function automatically handles boundary conditions by clamping coordinates to valid grid indices.
        The resulting block may be smaller than (2*distance+1) x (2*distance+1) if the center is near grid edges.
    """
    x_max,y_max = grid.shape
    x_left = max(0,x-distance)
    x_right = min(x_max,x+distance+1)
    y_down = max(0,y-distance)
    y_up = min(y_max,y+distance+1)

    grid_block = grid[x_left:x_right,y_down:y_up]        
    return ((x,y), grid_block)        